import axios from 'axios';
import React from 'react';
import Select from 'react-select'


export default class extends React.Component {
    // TODO remote filtering (stop fetching all data at once)
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    state = {
        isLoading: false,
        options: []
    };

    fetchOptions(url) {
        this.setState({isLoading: true});
        axios.get(url)
            .then(response => {
                let data = [];
                response.data.forEach(element => {
                    data.push({value: element.id, label: element.name})
                });
                this.setState({options: data});
            }).finally(() => {
                this.setState({isLoading: false});
        })
    }

    componentDidMount() {
        this.fetchOptions(this.props.optionsUrl);
    }

    /**
     * Lift changes up when onChange property is set.
     * @param selected Selected items.
     * @param action
     */
    handleChange(selected, action) {
        try {
            this.props.onChange(selected, action);
        } catch (error) {
            if (!(error instanceof TypeError)) {
                throw error;
            }
        }
    }

    render() {
        let label;
        if (this.props.label) {
            label = <p>{this.props.label}</p>;
        }

        return (
            <div>
                {label}
                <Select
                    isLoading={this.state.isLoading}
                    isMulti
                    onChange={this.handleChange}
                    options={this.state.options}
                    placeholder='All'/>
            </div>
        )
    }
}

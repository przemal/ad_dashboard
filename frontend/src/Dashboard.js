import React from 'react';
import MultiSelect from './components/MultiSelect'
import './Dashboard.css';


const API_URL = 'http://localhost:8000/api/';


export default class extends React.Component {
    constructor(props) {
        super(props);
        this.onCampaignChange = this.onCampaignChange.bind(this);
        this.onSourceChange = this.onSourceChange.bind(this);
    }

    state = {
        selectedCampaigns: [],
        selectedSources: []
    };

    onCampaignChange(selected, action) {
        this.setState({selectedCampaigns: selected});
    }

    onSourceChange(selected, action) {
        this.setState({selectedSources: selected});
    }

    render() {
        return (
            <div className='Dashboard'>
                <div className='SidePanel'>
                    <h2>Filter dimension values</h2>
                    <div className='Filters'>
                        <div>
                            <MultiSelect
                                label='Datasource'
                                optionsUrl={API_URL + 'sources'}
                                onChange={this.onSourceChange}/>
                            <MultiSelect
                                label='Campaign'
                                optionsUrl={API_URL + 'campaigns'}
                                onChange={this.onCampaignChange}/>
                        </div>
                        <div>
                            <button className='ApplyFilters'>
                                Apply
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

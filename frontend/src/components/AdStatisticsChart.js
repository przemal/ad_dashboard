import axios from 'axios';
import React from 'react';
import {
    CartesianGrid,
    Legend,
    LineChart,
    Line,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis
} from 'recharts';


export default class extends React.Component {
    state = {
        data: []
    };

    commaSeparatedParams(params) {
        let commaSeparated = {};
        if (params !== undefined) {
            for (let [key, value] of Object.entries(params)) {
                commaSeparated[key] = value.join(',')
            }
        }
        return commaSeparated;
    }

    fetchData(url, params) {
        if (!(url)) {
            return;
        }
        axios.get(url, {params: this.commaSeparatedParams(params)})
            .then(response => {
                this.setState({data: response.data});
            })
    }

    componentDidMount() {
        this.fetchData(this.props.dataUrl, this.props.dataParams);
    }

    componentDidUpdate(prevProps) {
        if (JSON.stringify(this.props.dataParams) == JSON.stringify(prevProps.dataParams)  // TODO deep compare
            && this.props.dataUrl === prevProps.dataUrl) {
            return; // nothing to do
        }
        this.fetchData(this.props.dataUrl, this.props.dataParams);
    }

    render() {
        return (
            <ResponsiveContainer width='100%' height={400}>
                <LineChart data={this.state.data}>
                    <CartesianGrid stroke='#eaeaea' vertical={false}/>
                    <XAxis dataKey='date'/>
                    <YAxis
                        yAxisId='left'
                        dataKey='total_clicks'
                        axisLine={false}
                        tickLine={false}/>
                    <YAxis
                        yAxisId='right'
                        dataKey='total_impressions'
                        axisLine={false}
                        tickLine={false}
                        orientation='right'/>
                    <Line
                        yAxisId='left'
                        type='linear'
                        dataKey='total_clicks'
                        name='Clicks'
                        dot={false}
                        stroke='#224e6f'/>
                    <Line
                        yAxisId='right'
                        type='linear'
                        dataKey='total_impressions'
                        name='Impressions'
                        dot={false}
                        stroke='#4fade3'/>
                    <Legend/>
                    <Tooltip/>
                </LineChart>
            </ResponsiveContainer>
        );
    }
}

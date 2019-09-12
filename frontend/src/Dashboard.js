import React from 'react';
import AdStatisticsChart from './components/AdStatisticsChart'
import MultiSelect from './components/MultiSelect'
import './Dashboard.css';


const API_URL = 'http://localhost:8000/api/';
const DAILY_STATISTICS_URL = API_URL + 'statistics/daily';


export default class extends React.Component {
    constructor(props) {
        super(props);
        this.onCampaignChange = this.onCampaignChange.bind(this);
        this.onSourceChange = this.onSourceChange.bind(this);
        this.updateChart = this.updateChart.bind(this);
    }

    componentDidMount() {
        this.updateChart();
    }

    state = {
        filtersSummary: '',
        selectedCampaigns: [],
        selectedSources: []
    };

    onCampaignChange(selected, action) {
        this.setState({selectedCampaigns: selected});
    }

    onSourceChange(selected, action) {
        this.setState({selectedSources: selected});
    }

    filterSummary(name, array) {
            let summary = '';
            if (array && array.length > 0) {
                summary += `${name} ` + array.map(e => `"${e.label}"`).join(' and ');
            } else {
                summary += `All ${name}s`;
            }
            return summary;
    }

    selectedFilters() {
        let filters = {};
        function setFilterValues(name, array) {
            if (array && array.length > 0) {
                filters[name] = array.map(e => e.value);
            }
        }
        setFilterValues('campaigns', this.state.selectedCampaigns);
        setFilterValues('sources', this.state.selectedSources);
        return filters;
    }

    updateChart() {
        this.setState({
            filters: this.selectedFilters(),
            filtersSummary:
                this.filterSummary('Datasource', this.state.selectedSources) + '; '
                + this.filterSummary('Campaign', this.state.selectedCampaigns)});
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
                            <button
                                className='ApplyFilters'
                                onClick={this.updateChart}>
                                Apply
                            </button>
                        </div>
                    </div>
                </div>
                <main>
                    <h2>{this.state.filtersSummary}</h2>
                    <AdStatisticsChart
                        dataUrl={DAILY_STATISTICS_URL}
                        dataParams={this.state.filters}/>
                </main>
            </div>
        )
    }
}

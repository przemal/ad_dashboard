let apiUrl;
if (process.env.NODE_ENV === 'development') {
    apiUrl = 'http://localhost:8000/';
} else {
    apiUrl = window.location.href;
}
apiUrl += 'api/';

export const API_URL = apiUrl;
export const DAILY_STATISTICS_URL = apiUrl + 'statistics/daily';

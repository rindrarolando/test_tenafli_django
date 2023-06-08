import requests
from django.http import JsonResponse


def top_5_states(request):
    state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                   'KY',
                   'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                   'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
                   ]
    # List of state abbreviations

    results = []
    for state_code in state_codes:
        url = f'https://api.schooldigger.com/v2.0/schools/?st={state_code}&appID=dd585cec&appKey=9278b51cd09b7d2a25ce3b2520580065'
        response = requests.get(url)
        data = response.json()

        schools = data['schoolList'][:20]  # Sample 20 schools from each state
        african_american_percentages = []
        for school in schools:
            yearly_details = school['schoolYearlyDetails']
            if yearly_details:
                latest_details = yearly_details[-1]  # Assuming the latest details are at the end of the list
                percentage = latest_details.get('percentofAfricanAmericanStudents')
                if percentage is not None:
                    african_american_percentages.append(percentage)

        if african_american_percentages:
            average_percentage = sum(african_american_percentages) / len(african_american_percentages)
        else:
            average_percentage = 0

        results.append({'state_code': state_code, 'average_percentage': average_percentage})

    top5 = sorted(results, key=lambda x: x['average_percentage'], reverse=True)[:5]

    return JsonResponse(top5, safe=False)

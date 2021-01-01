import requests

def create_query(languages, min_stars=50000):
    #example:  stars:>50000 language:python language:javascript
    query= f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "
    
    return query


def github_repo_search(languages, sort="stars", order="desc"):
    api_url = "https://api.github.com/search/repositories"

    query = create_query(languages)

    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(api_url, params=params)
    status_code = response.status_code

    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.") 
    else:   
        response_json = response.json()
        records = response_json["items"]
        return records


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = github_repo_search(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo that has {stars} stars. ")



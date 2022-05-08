enterprise_search_args = load_credentials("~/.twitter_keys.yaml",
                                          yaml_key="search_tweets_enterprise",
                                          env_overwrite=False)
#option one
from searchtweets import collect_results
weets = collect_results(rule,
                         max_results=100,
                         result_stream_args=enterprise_search_args)
[print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]];
# commented out, unless you want this data[print(tweet.created_at_datetime) for tweet in tweets[0:10]];
[print(tweet.generator.get("name")) for tweet in tweets[0:10]];

#option two
rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **premium_search_args)

print(rs)
tweets = list(rs.stream())
# using unidecode to prevent emoji/accents printing 
[print(tweet.all_text) for tweet in tweets[0:10]];
count_rule = gen_rule_payload("beyonce", count_bucket="day")

counts = collect_results(count_rule, result_stream_args=enterprise_search_args)
counts

#option three, shound like we should go this route due to the idea we will be able to do a full archive search
rule = gen_rule_payload("from:jack",
                        from_date="2017-09-01", #UTC 2017-09-01 00:00
                        to_date="2017-10-30",#UTC 2017-10-30 00:00
                        results_per_call=500)
print(rule)
tweets = collect_results(rule, max_results=500, result_stream_args=enterprise_search_args)
[print(tweet.all_text) for tweet in tweets[0:10]];
#modify below text for filters and ways to sort data
rule = gen_rule_payload("from:jack",
                        from_date="2017-09-20",
                        to_date="2017-10-30",
                        count_bucket="day",
                        results_per_call=500)
print(rule)
counts = collect_results(rule, max_results=500, result_stream_args=enterprise_search_args)
[print(c) for c in counts];

#make into a readme.sh
jupyter-nbconvert ./api_example.ipynb --to rst
#jupyter-nbconvert ./credential_handling.ipynb --to rst

sed 's/.*parsed-literal.*/::/' api_example.rst > _api_example.rst
#sed 's/.*parsed-literal.*/::/' credential_handling.rst > _credential_handling.rst

mv _api_example.rst api_example.rst
#mv _credential_handling.rst credential_handling.rst

$(brew --prefix)/bin/pandoc -i base_readme.rst --to rst | sed 's/ipython3/python/' > ../README.rst
#| sed 's/.*parsed-literal.*/::/' 















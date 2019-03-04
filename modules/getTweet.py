import tweepy
import time


if __name__ == "__main__":
    current_milli_time = lambda: int(round(time.time() * 1000))

    def authorize():
        keys = {}
        with open("res/tweet_auth.txt") as creds:
            for line in creds:
                line = line.strip()
                eq = line.find("=")
                keys[line[:eq]] = line[eq+1:]

        auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_key"], keys["access_secret"])

        return auth

    def queryTwitter(query, n):
        start = time.time()
        max_queries = 100
        api = tweepy.API(authorize(), wait_on_rate_limit=True)
        
        tweets = tweet_batch = api.search(query, count=n, lang="en")
        i = 1

        print("Getting tweets...")

        while len(tweets) < n and i < max_queries:
            pr = (len(tweets) * 100) / n
            print("{0:.1f}%".format(pr))
            tweet_batch = api.search(query, count = n - len(tweets), max_id = tweet_batch.max_id, lang="en")
            tweets.extend(tweet_batch)
            i += 1
        end = time.time()
        t = end - start

        print("Done! Got {0} tweets in {1:.2f} seconds!".format(n, t))

        return tweets

    query = input("Enter a search query: ")
    n = int(input("How many results do you want: "))

    results = queryTwitter(query, n)

    with open("res/tweets.txt", "w+",  encoding="utf-8") as resultFile:
        for result in results:
            resultFile.write(result.text + "\n")

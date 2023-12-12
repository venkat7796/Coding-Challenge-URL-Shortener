1. Convert Long Url to Short Url
Endpoint : http://localhost:5000/api/v1/converturl
Request Parameters : 
{
    "longUrl": "https://www.new.com"
}
Response Parameters :
{
    "longUrl": "https://www.new.com",
    "shortUrl": "http://localhost:5000/LaYngYt",
    "shortUrlId": "LaYngYt"
}
Algorithm Used:
In total there are 62 possibilities
numeric --> 0 - 9
lowercase --> a - z
uppercase --> A - Z
In total there will be 62 values.
Mapping each value to a numeric from 0 to 61. For instance {0: '0', 1:'1',...,10:'a'}

Algorithm:
When a post request is made to the above endpoint, capture the timestamp.

The timestamp is then subjected to a base 62 conversion with the timestamp value divided by 62 with the remainder is mapped against my mapping table and the quotient is subjected to base 62 conversion.

The remainder value is consolidated at each step and the resultant value is returned back as the short url with the domain being http://localhost:5000 since the code is executed locally.

This algorithm is the miniature version of the Twitter Snowflake approach which would have leveraged more terminologies such as data center id, machine id etc for large scale systems.

2. Redirect short Url requests to the appropriate long URL
Endpoint : http://localhost:5000/{shortUrlId}

Response : LongUrl
Message Code : 302

If shortURL does not exist then return error.


3. Delete the shortUrl
Endpoint : http://localhost:5000/{shortUrlId}

Response : Success Message
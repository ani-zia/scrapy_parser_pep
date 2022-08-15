# Python PEP Parsing Project

Quick and simple parser for you to catch up with PEP Documentation Statuses.

All technology magic based on Scrapy framework.

## Start & Usage

### Installing

```
git clone https://github.com/ani-zia/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

```
python3 -m venv venv && source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


### Introducing

Command to get all existing PEPs along with they actual statuses:

```
scrapy crawl pep
```

The results will be in a folder `results`:

* csv file with the table of all existing PEPs along with they numbers and actual statuses
* csv file with the table of availible PEP statuses and a number of them (and sum of them all!)


---

Author Anya Simanova
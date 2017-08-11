# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

#counties = ['adair','alfalfa','atoka','beaver','beckham','blaine','bryan','caddo','canadian','carter','cherokee','choctaw','cimarron','coal','comanche','cotton','craig','creek','bristow','drumright','custer','delaware','dewey','ellis','garfield','garvin','grady','grant','greer','harmon','harper','haskell','hughes','jackson','jefferson','johnston','kay','poncacity','kingfisher','kiowa','latimer','leflore','lincoln','logan','love','major','marshall','mayes','mcclain','mccurtain','mcintosh','murray','muskogee','noble','nowata','okfuskee','oklahoma','okmulgee','henryetta','osage','ottawa','payne','pawnee','pittsburg','pontotoc','pottawatomie','pushmataha','rogermills','rogers','seminole','sequoyah','stephens','texas','tillman','wagoner','washington','washita','woods','woodward']
counties = ['oklahoma','Tulsa','cleveland']
#next_link = 0
years = ['2011','2012','2013','2014','2015','2016','2017']
CrimeSeverity = ['CF','CM']

def CaseEndingNumbers():
    for x in range(1, 7500):
        yield '%d' % x




def GetOklahomaStateCases():
    for county in counties:
        for CaseEndingNumber in ListOfCaseEndingNumbers:
            for year in years:
                for severity in CrimeSeverity:
                  record = {}
                  #print 'http://www.oscn.net/dockets/GetCaseInformation.aspx?db=%s&number=%s-%s-%s' % (county, severity, year, CaseEndingNumber)
                  record['case'] ='http://www.oscn.net/dockets/GetCaseInformation.aspx?db=%s&number=%s-%s-%s' % (county, severity, year, CaseEndingNumber)
                  print 'Case URL:', record
                  scraperwiki.sqlite.save(unique_keys=['case'], data=record)
                
CaseEndingNumbers()
ListOfCaseEndingNumbers = list(CaseEndingNumbers())
GetOklahomaStateCases()
#scraperwiki.sqlite.save(['case'], record)

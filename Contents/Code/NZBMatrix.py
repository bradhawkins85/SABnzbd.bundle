#### Use this file as a template when adding support for a new NZB Provider ####
##### Save modified version with filename <provider>.py, eg. NZBMatrix.py ######

PROVIDER = 'NZBMatrix' 

# URL used for API-based search #
API_SEARCH_URL      =  'http://api.nzbmatrix.com/v1.1/search.php?search=%s&catid=%s&num=%s&username=%s&apikey=%s'
                        # (query, category='', max_results='', user, api_key)

# URL used for API-based NZB downloads #
API_DOWNLOAD_URL    =   'http://api.nzbmatrix.com/v1.1/download.php?id=%s&username=%s&apikey=%s'
                        # (nzb_id, user, api_key)

### DEFAULT SETTINGS ###
USE_HTTPS = False   # Takes a bool
MAX_RESULTS = ''    # Takes an integer (as a string) to a maximum of 50
MAX_AGE = ''        # Takes an integer (as a string)

# NZB Categories #
CATEGORIES = [] ### TODO:: figure out how to handle categories

def Search(sender, user='', api_key='', query='', category=''): ###TODO:: What other global-type parameters should be added? ###
    '''
        should return a list of JSON objects with the following fields:
        {
            "title"     :   "the title of the nzb",
            "nzb_id"    :   "the unqiue id of the nzb used by the provider",
            "provider"  :   "same as the filename (without '.py')",
            "summary"   :   "Build a summary string with as much detail as can
                                be gathered just from the search response.",
            "thumb:     :   "an image URL is available"
        }
    '''
    
    return

def Add(sender, nzb_id, user='', api_key=''):
    ''' should return a URL for the NZB to be added which can then be passed via
        the SABnzbd API function "addurl" '''
    return

def GetNZBDetails(sender, nzb_id, user='', api_key=''):
    ''' return a JSON object with as much detail about the NZB as possible '''
    return

def NZBMatrixURL(url):
    try:
        if Dict[PROVIDER]['use_https']:
            return url.replace('http://', 'https://')
        else:
            return url
    except:
        return url

################################################################################
######## Add methods for setting provider-specific defaults below here #########
################################################################################

def SetDefaults(sender):
    ''' return a MediaContainer with a list of DirectoryItem function callbacks
     for setting defaults specific to this NZB Provider '''
    
    if Dict.haskey(PROVIDER):
        ''' check to see if defaults already exist for this provider '''
        pass
    else:
        ''' otherwise create a set of defaults settings '''
        Dict[PROVIDER] = {}
        ''' Add basic default settings here '''
        Dict[PROVIDER]['use_https']     =   USE_HTTPS
        Dict[PROVIDER]['max_results']   =   MAX_RESULTS
        Dict[PROVIDER]['max_age']       =   MAX_AGE
    
    dir = MediaContainer(title1=PROVIDER, title2="Set Defaults")
    if Dict[PROVIDER]['use_https']:
        dir.Append(Function(DirectoryObject(UseHTTPS, title="Use SSL Encryption: TRUE"), https=False))
    else:
        dir.Append(Function(DirectoryObject(UseHTTPS, title="Use SSL Encryption: FALSE"), https=True))
    dir.Append(Function(InputDirectoryObject(MaxResults, title="Maximum # of results to return: %s" % Dict[PROVIDER]['max_results'])))
    dir.Append(Function(InputDirectoryObject(MaxAge, title="Maximum age of results to return: %s days" % Dict[PROVIDER]['max_age'])))
    
    return dir
    
def UseHTTPS(sender, https):
    Dict[PROVIDER]['use_https'] = https
    return MessageContainer(PROVIDER, "Use SSL Encryption set to %s" % Dict[PROVIDER]['use_https'])
    
def MaxResults(sender, max_results):
    Dict[PROVIDER]['max_results'] = max_results
    return MessageContainer(PROVIDER, "Max results set to %s" % Dict[PROVIDER]['max_results'])
    
def MaxAge(sender, max_age):
    Dict[PROVIDER]['max_age'] = max_age
    return MessageContainer(PROVIDER, "Max age set to %s" % Dict[PROVIDER]['max_age'])
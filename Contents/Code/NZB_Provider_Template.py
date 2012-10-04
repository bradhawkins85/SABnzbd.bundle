#### Use this file as a template when adding support for a new NZB Provider ####
##### Save modified version with filename <provider>.py, eg. NZBMatrix.py ######

PROVIDER = '' 

# URL used for API-based search #
API_SEARCH_URL      =   '' 

# URL used for API-based NZB downloads #
API_DOWNLOAD_URL    =   ''

def Search(sender, user='', api_key='', query=''): ###TODO:: What other global-type parameters should be added? ###
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
    return

def GetNZBDetails(sender, nzb_id, user='', api_key=''):
    return

################################################################################
######## Add methods for setting provider-specific defaults below here #########
################################################################################

def SetDefaults(sender):
    ''' return a MediaContainer with a list of DirectoryItem function callbacks
     for setting defaults specific to this NZB Provider '''
    dir = MediaContainer(title1=PROVIDER, title2="Set Defaults")
    
    return dir
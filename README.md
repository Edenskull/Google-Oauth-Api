# Google-Oauth-Api

Python Script file to connect with Google API.

## Getting Started

This file is a template file to add in a project that need to connect to Google API via Oauth Authentication and using a client_secret.json file.

### Prerequisites

You'll need to download google-api-python-client and oauth2client to use this file : 

```CMD
pip install --upgrade google-api-python-client oauth2client
```

### Installing

## Deployment and Modification

You can change the scope to what API you need to use [there](https://developers.google.com/identity/protocols/googlescopes) is the list of Scopes you can set.  
You also need to modify the build of the service : 

```PYTHON
return build('drive', 'v3', http=creds.authorize(Http())) # You can change drive by maps, gmail, etc.... Don't forget to change the version
```

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details

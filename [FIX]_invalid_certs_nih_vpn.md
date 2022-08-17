## Issue Description
Installing/updating conda or pypi packages via NIH VPN results in the `HTTP 000 CONNECTION FAILED` error. This is strange coz when I copy and paste the [conda URL](https://conda.anaconda.org/conda-forge/osx-64) and [pypi URL](https://pypi.org/simple/pip/)in my browser, I'm able to access it. 

**Conda Error**

```bash 
$ conda install -c conda-forge r-mumin
Collecting package metadata (current_repodata.json): failed

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://conda.anaconda.org/conda-forge/osx-64/current_repodata.json>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.
'https://conda.anaconda.org/conda-forge/osx-64'
```

**PyPI Error**

```bash
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```

## Working Solution

1. Open up pypi.org on firefox and found the NIH certificate that was being used for verification. 


![Screen Shot 2022-01-24 at 2 55 24 PM](https://user-images.githubusercontent.com/10297203/161587769-48a4129b-2050-4748-8e74-ab76624f0647.png)

2. Export the certificate to home directory, from KeyChain Access on Mac, in  `.pem` format. 


![Screen Shot 2022-01-24 at 3 03 21 PM](https://user-images.githubusercontent.com/10297203/161587873-8187d39e-a65e-4952-b571-0af93ab6d4d7.png)


![Screen Shot 2022-01-24 at 2 53 02 PM](https://user-images.githubusercontent.com/10297203/161588048-dd9abf13-f395-44f5-a0b9-bf78575b9fb9.png)
 

3. For any pip/conda install commands, I use the --cert flag. For example - `pip install --cert ~/NIH-DPKI-ROOT-1A.pem dcm2bids`

### "permanent"-ish fix

Adding the following line in my zshrc file saves me the trouble of specifying the `--cert` flag but that said I'm not sure what's causing the issue to begin with. 

```bash
export REQUESTS_CA_BUNDLE=/Users/arshithab/NIH-DPKI-ROOT-1A.pem
```


## References
* [pip install fails with "connection error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:598)"](https://stackoverflow.com/a/26062583/4393932)
* [Conda update fails with SSL error CERTIFICATE_VERIFY_FAILED](https://stackoverflow.com/a/35804869)
* [Conda User guide on Non-standard certificates](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/non-standard-certs.html)
* For DSST folks, here's our [slack discussion thread](https://nimh-dsst.slack.com/archives/CNH809210/p1649081358561459) on the issue

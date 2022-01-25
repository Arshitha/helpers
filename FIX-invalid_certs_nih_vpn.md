## Issue Description
Installing/updating conda or pypi packages via NIH VPN results in the `HTTP 000 CONNECTION FAILED` error. This is strange because when I copy and paste the [URL](https://conda.anaconda.org/conda-forge/osx-64) in my browser, I'm able to access it. 

```bash 
$ conda install -c conda-forge r-mumin
Collecting package metadata (current_repodata.json): failed

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://conda.anaconda.org/conda-forge/osx-64/current_repodata.json>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.
'https://conda.anaconda.org/conda-forge/osx-64'
```


## Working Solution

1. Open up pypi.org on firefox and found the NIH certificate that was being used for verification. 
2. Export the certificate to home directory, from KeyChain Access on Mac, in  `.pem` format. 
3. For any pip/conda install commands, I use the --cert flag. For example - pip install --cert ~/NIH-DPKI-ROOT-1A.pem dcm2bids


## References
* [Conda update fails with SSL error CERTIFICATE_VERIFY_FAILED](https://stackoverflow.com/a/35804869)
* [Conda User guide on Non-standard certificates](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/non-standard-certs.html)

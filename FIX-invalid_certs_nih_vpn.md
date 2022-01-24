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


## References

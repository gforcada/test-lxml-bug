## LXML bug test repo

This repository serves as a bug report to demonstrate the "eating text" bug found in lxml.

To test it:

```
git clone https://github.com/gforcada/test-lxml-bug.git
cd test-lxml-bug
python3 -m venv .
. bin/activate
pip install -r requirements.txt
pytest test.py
```

One test should pass, the other one fail.
The `diff` between the two XSLT transforms gives the culprit of the failure:

```
diff -u article-works.xsl article-fails.xsl
```

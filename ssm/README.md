# SSM Parameter Fetcher

To add a command line helper, add the following to relevant bash files:

```bash
ssm() {
    SSM_DIR=~/workspace/gists-personal/ssm/
    source $SSM_DIR/venv/bin/activate
    python $SSM_DIR/ssm.py "$@"
    deactivate
}
```

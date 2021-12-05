# delta_copy
delta copy for file backup

## Installation
```bash
git clone https://github.com/GouMinghao/delta_copy
cd delta_copy
python3 -m pip install .
```

## Example

### delta compare
Given source directory and destination directory, delta_compare can find those files or directories that exist in source directory but do not exist in destination directory. 
```bash
cd tests
python test_compare.py
```
The missing file `dir2` with regard to `dir1` will be saved in a txt file.

### delta copy
The delta compare program will generate a log file which points out the differences. You can modify the log file and then execute delta copy according to the file.
```bash
# modify line 2 in test_copy.py
# modify the delta compare log file
cd tests
python test_copy.py
```
You will see the missing files in `dir2` are copied from `dir1`.

## Usage
Two scripts file are provided in `scripts`.
You should run `run_compare.py` first and then modify the log file and finally run `run_copy.py`. The missing file from one directory will be copied to the other one.
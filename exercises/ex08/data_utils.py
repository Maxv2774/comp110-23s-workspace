"""Data Utils.py !"""
__author__ = "730605138"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """read a csv file and returns a list of dictionaries"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """returns values in a table column under a specfic header"""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """reformats data so that its a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    first_row: dict[str,str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result

def head(table: dict[str,list[str]], n: int) -> dict[str, list[str]]:
    """returns the first n values of the table"""
    out: dict[str, list[str]] = {}
    for i in table:
        out[i] = table[i][:n]
    return out

def select(table: dict[str, list[str]], col: list[str]) -> dict[str, list[str]]:
    """returns only the selected columns"""
    out: dict[str, list[str]] = {}
    for i in table:
        if i in col:
            out[i] = table[i]
    return out

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """concats 2 tables"""
    out: dict[str, list[str]] = {}
    for i in table1:
        out[i] = table1[i]
    for i in table2:
        if i in out:
            out[i] += table2[i]
        else:
            out[i] = table2[i]
    return out

def count(l1: list[str]) -> dict[str, int]:
    out = {}
    for i in set(l1):
        out[i] = l1.count(i) 
    return out
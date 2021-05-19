# LIML
List Markup Language

## Introduction
LIML is a lightweight markup language that systematically represents list of data. 
It is designed to systematically store lists of small data. This allows the establishment of a simple and structured list-type database.

## Example
```ini
; ftpinfo.liml 

[users]
danidoco
martin
liam
harry

[superusers]
danidoco

[files]
hello.txt
bye.txt
super.c
ftpinfo.liml
```

If you parse this as dictionary, you can get result like this:
```json
{
  "users": ["danidoco", "martin", "liam", "harry"],
  "superusers": ["danidoco"],
  "files": ["hello.txt", "bye.txt", "super.c", "ftpinfo.liml"]
}
```
## Usage
LIML have only three concepts
* section
* value
* comment

### Section
A section is a unit in which a value can be contained.
All values must be included in a section, and there cannot be a section within the section.


You can create a section with brackets.
```ini
[section1]
a
b
c
d

[section2]
e
f
g
```

Value list of section1: `[a, b, c, d]`

Value list of section2: `[e, f, g]`

You cannot contain sections in a section.
```ini
[section1]
[section2]
value
valval
luelue

; WRONG CODE
```



### Value
Value is element of section.

You can declare value like this.
```ini
[section]
value1
value2
value3
```

In the code above, `value1` `value2` `value3` is value.

### Comment
Comments do not wrok at all. It is just a memo for developer.
However, writing comments is not recommended, because it can cause some tiny problems when you use LIML parser.


You can write comment with semicolon
```ini
[section]
val1
val2
; comment comment comment!
val3
```

However, you cannot write comment with values in one line
```plain
[section]
some ;comment
```

If you write comment like this, parser cannot recognize that it is a comment.
Parser will think ```some ;comment``` as a value

## Using LIML Library
LIML Library basically includes parser and writer. With this, you can parse and modify LIML file smoothly.


Currently, LIML library supports the programming languages listed below.

* python

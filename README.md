# tf

CLI tool to extract and print formatted lines using regular expressions.

This is a very hacky and naive script, which allows extraction of textual data from line based input for printing as formatted text.
There are probably tons of errors and pitfalls in and thousands of ways to break it. But if applied properly, it does a great job.

It is written in python3 and uses only buitlin dependencies.

## Usage

The script takes two arguments. First arg is a regular expression (python syntax) with capture groups, and second one is a python format string with curly braces as placeholders. It reads line based input from stdin, and prints the format string for every line, where the regex found a match, replacing the placeholders with the corresponding capture group.

### Example

```sh
$ cat file.txt | tf.py '(.*)' 'line: {}'
line: always
line: be
line: yourself
```

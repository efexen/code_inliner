# Simple doc inliner

Small utility to enable inserting a text file inline to a master file. I wrote this to allow me to keep my code examples in separate files and reference them from my markdown files.

### Usage

Usage is simply:

```
$ python build.py <input_file> <output_file>
```

This will read the `input_file`, search for occurence of {{ and }} with some text in the middle that contains a `.`

If found it uses the found string as a file path and reads the file contents and replaces the occurence of the placeholder with the contents.

*Note* Currently the paths to the files need to be relative to the location the script is run from*

### Example

Given template:

````
# Wow

This is a test and should haves some Jabba code next

```JAVA
{{code/test.java}}
```

This should be after the code
````

and a file `test.java` in a folder `code` with content of:

```
class Tester {
  public Tester() {
    public static void main(string[] args) {
    }
  }
}
```

running the following command:

```
python build.py template.md output.md
```

Will result in the output md file that looks like this:

````
# Wow

This is a test and should haves some Jabba code next

```JAVA
class Tester {
  public Tester() {
    public static void main(string[] args) {
    }
  }
}

```

This should be after the code

````

# Hypertext Translator
Hypertext Translator (shortened as HT) is a programming language implemented in Python which gets compiled to Hypertext Markup Language (shortened as HTML). This programming language can be used for generating some simple HTML files but this programming language can't make dynamic websites. You have to edit the output file to make the website better and functionable. And like most of you I also thing that this programming language is kinda useless but anyways, it's a programming language.
## How to use
To use HT you can use the `ht.py` file like `ht.py input_file.ht output_file.html`.
## How to program in this language?
Every program in HT must start with a line without a tag for the title. After that line you can use tags like `big_header`, `small_header`, etc. The tags can have values like `big_header: Hello world!`. Every tag and value must be seperated with a `: `. Here's an example program you can maybe look at and change some piece to learn:
```Hypertext Translator
example_title
big_header: Welcome!
small_header: This is a website written using HT.
paragraph: Hypertext Translator is a programming language which gets translated into HTML.
openable: This is an openable!-!An openable is just the details tag in HTML.
form: username$Enter your username**password$Enter your password!-!Login
```
## How can I use a style?
The styles are new and because of this there's only a single style. You can use it by adding `--classic-dark` at the end of the compiling command. You can also specify that you don't want a style by adding `--none` at the end of your compiling command but it's useless. You can just not specify the style to get nothing as the style.
## Tags
|Tag|Explanation|Example usage|
|---|-----------|-------------|
|`big_header`|It's H1 in HTML.|`big_header: Hello world!`|
|`small_header`|It's H3 in HTML.|`small_header: This is a small header.`|
|`paragraph`|It's `<p>` in HTML.|`paragraph: This is a paragraph.`|
|`openable`|It's `<details>` and `<summary>` in HTML. The summary and the content is seperated with a `!-!` which is interesting.|`openable: example_summary!-!This is something.`|
|`form`|It's `<form>` in HTML. You can add inputs like `name$placeholder` and the inputs have to be seperated with a `**`. You must also add submit button like `!-!button_text` at the end.|`form: username$Enter your username**password$Enter your password!-!Login`|
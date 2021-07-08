import json
import os
import pathlib

from jinja2 import Environment, FileSystemLoader
from livereload import Server
from more_itertools import chunked


def get_book_json(json_path):
    json_path = pathlib.Path("library", "json", json_path)

    with open(json_path, 'r', encoding="utf-8") as book_json:
        book_json = json.load(book_json)

    img_path, book_title, book_path = book_json["img_path"],\
        book_json["title"], book_json['book_path']

    if img_path is not None:
        img_path = img_path.replace("\\", "/")
        img_path = f"../{img_path}"
    else:
        img_path = "../images/Noimg.gif"

    book_path = book_path.replace("\\", "/")
    book_path = f"../{book_path}"

    book_json["title"] = book_title
    book_json["img_path"] = img_path
    book_json["book_path"] = book_path

    return book_json


def split_into_columns(book_coulmn):
    num = len(book_coulmn) // 2
    first_book_column, second_book_coulmn = list(chunked(book_coulmn, num))

    return first_book_column, second_book_coulmn


def get_books():
    json_file_list = os.listdir("library/json")
    books_json = [get_book_json(json_path) for json_path in json_file_list]
    return books_json


def rebuild():
    os.makedirs("pages", exist_ok=True)

    books_number_per_page = 20
    environment = Environment(loader=FileSystemLoader("templates"))
    template = environment.get_template("template.html")
    books = get_books()
    chunked_books_per_page = list(chunked(books, books_number_per_page))
    path = pathlib.Path("pages", "index")

    for current_page, book_coulmn in enumerate(chunked_books_per_page, 1):
        file_name = f"{path}{current_page}.html"
        first_book_column, second_book_coulmn = split_into_columns(book_coulmn)

        pages_info = {
            "current_page": current_page,
            "all_pages_number": len(chunked_books_per_page)
        }

        rendered_page = template.render(
            first_book_column=first_book_column,
            second_book_coulmn=second_book_coulmn,
            current_page=pages_info["current_page"],
            all_pages_number=pages_info["all_pages_number"]
        )

        with open(file_name, "w", encoding="utf8") as file:
            file.write(rendered_page)
    print("Site rebuilt")


def main():
    server = Server()
    rebuild()
    server.watch("templates/*.html", rebuild)
    server.serve(root=".")


if __name__ == "__main__":
    main()

import json
import os
from collections.abc import Callable
from typing import Any

import click
from jinja2 import Environment, FileSystemLoader


def skill_icons_get_icons_strategy(skills: list[str]) -> str:
    return f"https://skillicons.dev/icons?i={','.join(skills)}"


TEMPLATE_PATH = "./templates"
DEFAULT_DEST_PATH = "./README.md"
DEV_DEST_PATH = "generated/README.md"
DEFAULT_SKILL_ICON_STRATEGY: Callable[[list[str]], str] = skill_icons_get_icons_strategy


def render_simple_template(env: Environment, data: dict[str, Any]) -> str:
    template = env.get_template("simple.md")

    description: str = data["description"]
    skills: list[str] = data["skills"]
    email = data["contact"]["email"]
    discord = data["contact"]["discord"]

    data = {
        "description": description,
        "skills_img_url": DEFAULT_SKILL_ICON_STRATEGY(skills),
        "contacts": [
            {
                "label": "Email",
                "link": f"mailto:{email}",
                "value": email,
                "type": "link",
            },
            {"label": "Discord", "value": discord, "type": "username"},
        ],
    }

    return template.render(data)


@click.command()
@click.option("--mode", default="default", type=str)
@click.argument("data_file", type=str)
def main(mode: str, data_file: str):
    dest_path = None
    if mode == "dev":
        dest_path = DEV_DEST_PATH
    else:
        dest_path = DEFAULT_DEST_PATH

    env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    print(f"Reading data file contents: {data_file}")
    with open(data_file) as f:
        data: dict[str, Any] = json.load(f)

    print("Rendering template...")
    result = None
    if data["template"] == "simple":
        result = render_simple_template(env, data["data"])
    else:
        raise ValueError("unsupported type")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    print("Writing result to DEST_PATH")
    with open(dest_path, "w") as f:
        f.write(result)
    print("Completed!")


if __name__ == "__main__":
    main()

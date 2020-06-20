# Traefic proof of concept

Goal: Test out the Traefic

See:

* [Basics](projectinfo-1.md)
* [Configuration](projectinfo-2.md)


## Building documentation - Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    src/          # source code

## Running it

```bash
docker run --rm -it -p 8000:8000 -v $(pwd):/docs miroadamy/mkdocs-material
```

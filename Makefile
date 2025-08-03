build:
	python scripts/generate_nav.py
	cat mkdocs.base.yml > mkdocs.yml
	echo "" >> mkdocs.yml
	cat nav.yml >> mkdocs.yml
	mkdocs build

serve:
	mkdocs serve

clean:
	rm -rf site
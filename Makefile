CATALOG_URL = http://catalog.tamu.edu/undergraduate
DATA_DIR = data
PROCESSORS = processors

.PHONY: all



school_links.csv: catalog_page.html
	cat $(DATA_DIR)/$< | python $(PROCESSORS)/extract_links.py $(CATALOG_URL) > $(DATA_DIR)/$@

catalog_page.html: all
	wget $(CATALOG_URL) -O $(DATA_DIR)/$@

clean:
	rm -Rf data/*
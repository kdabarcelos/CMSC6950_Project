default: report.pdf

report.pdf: report.tex CO_CH_length_acf_plot.png msd_plot.png keywords_acf.png lags_acf.png references.bib
	latexmk -pdf

CO_CH_length_acf_plot.png: make_plot_acf_bond_length.py CH_acf.txt CO_acf.txt
	python3 make_plot_acf_bond_length.py CH_acf.txt CO_acf.txt CO_CH_length_acf_plot.png

msd_plot.png: make_plot_msd_random_walk.py msd_random_walk.txt
	python3 make_plot_msd_random_walk.py msd_random_walk.txt msd_plot.png

keywords_acf.png: make_plot_keywords_acf.py kw_acf.txt
	python3 make_plot_keywords_acf.py kw_acf.txt kw_acf.png

lags_acf.png: make_plot_kw_lags_acf.py kw_acf.txt
	python3 make_plot_kw_lags_acf.py kw_acf.txt lags_acf.png

CO_acf.txt: create_acf_bond_length.py CO_length_MD.txt
	python3 create_acf_bond_length.py CO_length_MD.txt CO_acf.txt

CH_acf.txt: create_acf_bond_length.py CH_length_MD.txt
	python3 create_acf_bond_length.py CH_length_MD.txt CH_acf.txt

msd_random_walk.txt: create_msd_random_walk.py
	python3 create_msd_random_walk.py msd_random_walk.txt

kw_acf.txt: download_keywords_acf.py
	python3 download_keywords_acf.py kw_acf.txt

clean:
	#not clean the input file for task 1 test800-1500ns-CO.txt and test800-1500ns-CH.txt
	find ./ -name "*.txt" -not -name "*_length_MD*" -exec rm {} \;
	rm *.png
	latexmk -c
	rm *.bbl

deepclean:
	rm *.pdf

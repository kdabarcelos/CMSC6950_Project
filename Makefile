default: report.pdf

report.pdf: report.tex CO_CH_length_acf_plot.png msd_plot.png
	pdflatex report.tex
	
CO_CH_length_acf_plot.png: make_plot_acf_bond_length.py CO_acf.txt CH_acf.txt
	python3 make_plot_acf.py CO_acf.txt CH_acf.txt CO_CH_length_acf_plot.png

msd_plot.png: make_plot_msd_random_walk.py msd.txt
	python3 make_plot_msd_random_walk.py msd.txt msd_plot.png

CO_acf.txt: create_acf_bond_length.py test800-1500ns-CO.txt
	python3 create_acf_bond_length.py test800-1500ns-CO.txt CO_acf.txt

CH_acf.txt: create_acf_bond_length.py test800-1500ns-CH.txt
	python3 create_acf_bond_length.py test800-1500ns-CH.txt CH_acf.txt

msd.txt: create_msd_random_walk.py
	python3 create_msd_random_walk.py msd_random_walk.txt

clean:
	rm *.txt
	rm *.png

# SARS-CoV-2-genome-diagram-using-Biopython
> Using Biopython to study computational molecular biology to build a Covid-19 genome diagram

The only purpose of this project is to learn more about computational molecular biology and the Biopython library.

For trustworthy information about SARS-CoV-2 (Covid-19) please look for reliable articles.

## Usage example

You can get the complete Covid-19 genome researched in Brazil and China and the MERS-CoV in the respective links:

[SARS-CoV-2/human/BRA/SP02cc/2020](https://www.ncbi.nlm.nih.gov/nuccore/MT350282)

[coronavirus 2 isolate 2019-nCoV WHU01](https://www.ncbi.nlm.nih.gov/nuccore/MN988668)

[Middle East respiratory syndrome coronavirus](https://www.ncbi.nlm.nih.gov/nuccore/KJ477102)

The diagrams elaborated with the Reportlab library in this project produced the following schematics:

A comparison between Covid-19 in Brazil, China and MERS-CoV, respectively
![](CDS%20Covid-19%20(BR)%20x%20Covid-19%20(WU)%20x%20MERS-CoV.jpg)

Covid-19's genome
![](Covid-19%20-%20Genome%20Diagram%20(circular).jpg)
![](Covid-19%20-%20Genome%20Diagram%20(linear).jpg)

Although the diagrams do not represent 100% of the reality, it was possible to have a great similarity with the tests obtained by professionals in the field, such as this research:

[SARS-CoV-2 (COVID-19) Genome](https://www.snapgene.com/resources/coronavirus-resources/?resource=SARS-CoV-2_(COVID-19)_Genome)


## Development setup

Install the Biopython library an the reportlab library via pip using
```sh
pip install biopython
pip install reportlab
```

## Contributing

1. Fork it (<https://github.com/aljawetz/SARS-CoV-2-genome-diagram-using-Biopython/fork>)
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

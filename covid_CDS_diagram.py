from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors

covid_br = SeqIO.read("MT_350282.gbk", "gb")
covid_wu = SeqIO.read('MN_988668.gbk', "gb")
mers = SeqIO.read("KJ_477102.gbk", "gb")

name = "CDS Covid-19 (BR) x Covid-19 (WU) x MERS-CoV"
gd_diagram = GenomeDiagram.Diagram(name)

index = 1
for record in [covid_br, covid_wu, mers]:

    gd_track_for_features = gd_diagram.new_track(
        index, name=record.id, greytrack=True, start=0, end=len(record)
    )
    index += 1
    gd_feature_set = gd_track_for_features.new_set()

    for feature in record.features:
        if feature.type != "CDS":
            # Exclude this feature
            continue
        if len(gd_feature_set) % 2 == 0:
            color = colors.grey
        else:
            color = colors.red

        gd_feature_set.add_feature(
            feature,
            sigil="ARROW",
            color=color,
            label=True,
            label_position="middle",
            label_size=6,
            label_angle=60,
        )

gd_diagram.draw(format="linear", pagesize="A4",
                fragments=1, start=0, end=len(record))
gd_diagram.write(name + ".pdf", "PDF")

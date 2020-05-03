from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

# Get the Covid-19 record
record = SeqIO.read("MT_350282.gbk", "genbank")

# Create the diagram
gd_diagram = GenomeDiagram.Diagram(record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features:
    if feature.type != "gene":
        # Exclude non genes
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue

    # Draws each of the genes
    gd_feature_set.add_feature(
        feature,
        sigil="ARROW",
        color=color,
        label=True,
        label_size=12,
        label_angle=60,
        label_position="middle",
        arrowshaft_height=0.2
    )

# Draw the linear diagram
gd_diagram.draw(format="linear", pagesize="A4",
                fragments=2, start=0, end=len(record))

gd_diagram.write("Covid-19 - Genome Diagram (linear).pdf", "PDF")

# Draw the circular diagram
gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(20 * cm, 20 * cm),
    start=0,
    end=len(record),
    circle_core=0.3,
)
gd_diagram.write("Covid-19 - Genome Diagram (circular).pdf", "PDF")

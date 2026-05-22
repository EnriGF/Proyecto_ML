library(chorddiag)
library(htmlwidgets)
matriz <- as.matrix(read.csv(file.choose(), row.names=1))
p <- chorddiag(matriz,
                 margin=250,
                 width=1000,
                 height=1000,
                 palette="Spectral",
                 groupnamePadding = 20,
                 groupnameFontsize = 10,
                 showTicks=FALSE)
saveWidget(p,  file="chordDiagram_porgrupos.html")

---
title: Lavorare con lo sfondo nei file ODS
type: docs
weight: 150
url: /it/python-net/working-with-background-in-ods-files/
description: Come lavorare con lo sfondo nei file ODS con Aspose.Cells for Python via .NET API.
keywords: Python work with Background in ODS Files, Read Background Information from ODS file Pyton via NET, Add Colored Background to ODS file using Python via NET, Python via NET Add Graphic Background to ODS file.
---
##  **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli nei file ODS. Lo sfondo può essere uno sfondo colorato o uno sfondo grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel file PDF generato. Lo sfondo è visibile anche nella finestra di dialogo dell'anteprima di stampa.

Aspose.Cells for Python via .NET offre la possibilità di leggere le informazioni di sfondo e aggiungere lo sfondo nei file ODS.

##  **Leggi le informazioni di base dal file ODS**

Aspose.Cells for Python via .NET fornisce il[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) classe per gestire lo sfondo nei file ODS. Nell'esempio di codice seguente viene illustrato l'utilizzo di[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) classe caricando il file[fonte ODS](90112030.ods) file e leggere le informazioni di base. Si prega di consultare l'output della console generato dal codice come riferimento.

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

###  **Uscita della console**

Tipo di sfondo: grafico

Posizione di sfondo: CenterCenter

##  **Aggiungi sfondo colorato al file ODS**

Aspose.Cells for Python via .NET fornisce il[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)classe per gestire lo sfondo nei file ODS. Nell'esempio di codice seguente viene illustrato l'utilizzo di[**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) proprietà per aggiungere uno sfondo colorato al file ODS. Si prega di consultare il[uscita ODS](90112031.ods) file generato dal codice come riferimento.

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

##  **Aggiungi sfondo grafico al file ODS**

Aspose.Cells for Python via .NET fornisce il[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)classe per gestire lo sfondo nei file ODS. Nell'esempio di codice seguente viene illustrato l'utilizzo di[**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/)proprietà per aggiungere uno sfondo grafico al file ODS. Si prega di consultare il[uscita ODS](90112030.ods)file generato dal codice come riferimento.

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}

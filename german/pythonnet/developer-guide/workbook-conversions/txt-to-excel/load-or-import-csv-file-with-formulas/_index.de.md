---
title: Laden oder importieren Sie die Datei CSV mit Formeln
type: docs
weight: 350
url: /de/python-net/load-or-import-csv-file-with-formulas/
description: Laden oder importieren Sie die Datei CSV mit Formeln mithilfe von Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 Die Datei CSV enthält hauptsächlich Textdaten und keine Formeln. Allerdings kommt es manchmal vor, dass CSV-Dateien auch Formeln enthalten. Solche CSV-Dateien sollten durch Festlegen von geladen werden[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) als *wahr**. Sobald diese Eigenschaft auf *true** gesetzt ist, behandelt Aspose.Cells Formeln nicht mehr als einfachen Text. Sie werden als Formel behandelt und von der Formelberechnungsmaschine Aspose.Cells wie gewohnt verarbeitet.

{{% /alert %}} 

 Der folgende Code veranschaulicht, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die[einfache CSV-Datei](5115034.csv)welches diese Daten enthält. Wie Sie sehen, enthält es eine Formel.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Der Code lädt zunächst die Datei CSV und importiert sie dann erneut in Zelle D4. Schließlich wird das Arbeitsmappenobjekt im XSLX-Format gespeichert. Der[Ausgabedatei XLSX](5115052.xlsx) sieht aus wie das. Wie Sie sehen, enthalten die Zellen C3 und F4 die Formel und das Ergebnis 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |


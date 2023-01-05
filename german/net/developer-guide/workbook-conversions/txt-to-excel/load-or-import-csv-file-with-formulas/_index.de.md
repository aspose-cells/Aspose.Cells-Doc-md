---
title: Laden oder importieren Sie die Datei CSV mit Formeln
type: docs
weight: 350
url: /de/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV-Datei enthält hauptsächlich Textdaten und keine Formeln. Manchmal kommt es jedoch vor, dass CSV-Dateien auch Formeln enthalten. Solche CSV-Dateien sollten geladen werden, indem Sie die[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) als**wahr** . Sobald diese Eigenschaft festgelegt wird**wahr**, Aspose.Cells behandelt die Formel nicht als einfachen Text. Sie werden als Formel behandelt und von der Formelberechnungs-Engine Aspose.Cells wie gewohnt verarbeitet.

{{% /alert %}} 

 Der folgende Code veranschaulicht, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die[einfache csv-Datei](5115034.csv) die diese Daten enthält. Wie Sie sehen, enthält es eine Formel.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Der Code lädt zuerst die Datei CSV und importiert sie dann erneut in Zelle D4. Schließlich wird das Arbeitsmappenobjekt im XSLX-Format gespeichert. Das[Ausgabedatei XLSX](5115052.xlsx) sieht aus wie das. Wie Sie sehen, enthalten die Zellen C3 und F4 die Formel und ihr Ergebnis 800.

|![todo: Bild_alt_Text](load-or-import-csv-file-with-formulas_1.png)|
|:- |


---
title: Laden oder importieren Sie die Datei CSV mit Formeln
type: docs
weight: 500
url: /de/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV-Datei enthält hauptsächlich Textdaten und keine Formeln. Manchmal kommt es jedoch vor, dass CSV-Dateien auch Formeln enthalten. Solche CSV-Dateien sollten geladen werden, indem Sie die[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) zu**wahr** . Sobald diese Eigenschaft festgelegt wird**wahr**, Aspose.Cells behandelt die Formel nicht als einfachen Text. Sie werden als Formel behandelt und von der Formelberechnungs-Engine Aspose.Cells wie gewohnt verarbeitet.

{{% /alert %}} 
## **Laden oder importieren Sie die Datei CSV mit Formeln**
 Der folgende Code veranschaulicht, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die[einfache csv-Datei](5472505.csv) die diese Daten enthält. Wie Sie sehen, enthält es eine Formel.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Der Code lädt zuerst die Datei CSV und importiert sie dann erneut in Zelle D4. Schließlich wird das Arbeitsmappenobjekt im XSLX-Format gespeichert. Das[Ausgabedatei XLSX](5472503.xlsx) sieht aus wie das. Wie Sie sehen, enthalten die Zellen C3 und F4 die Formel und ihr Ergebnis 800.

![todo: Bild_alt_Text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}

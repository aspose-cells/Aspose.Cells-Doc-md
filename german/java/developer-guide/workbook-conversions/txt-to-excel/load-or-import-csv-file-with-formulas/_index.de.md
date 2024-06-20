---
title: Laden oder Importieren von CSV Dateien mit Formeln
type: docs
weight: 500
url: /de/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Eine CSV-Datei enthält meistens textuelle Daten und keine Formeln. Manchmal enthalten CSV-Dateien jedoch auch Formeln. Solche CSV-Dateien sollten durch Festlegen von [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) auf **true** geladen werden. Sobald diese Eigenschaft auf **true** gesetzt ist, behandelt Aspose.Cells die Formel nicht als einfachen Text. Sie werden als Formel behandelt und von Aspose.Cells-Formelberechnungsmaschine wie gewohnt verarbeitet.

{{% /alert %}} 
## **CSV-Datei mit Formeln laden oder importieren**
Der folgende Code veranschaulicht, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zum Veranschaulichen verwenden wir die [einfache CSV-Datei](5472505.csv), die diese Daten enthält. Wie Sie sehen können, enthält sie eine Formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Der Code lädt zunächst die CSV-Datei und importiert sie erneut in die Zelle D4. Schließlich speichert er das Arbeitsmappenobjekt im XSLX-Format. Die [Ausgabe-XLSX-Datei](5472503.xlsx) sieht so aus. Wie Sie sehen können, enthält die Zelle C3 und F4 eine Formel und deren Ergebnis 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}

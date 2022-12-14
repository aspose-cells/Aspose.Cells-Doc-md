---
title: Laden Sie die Arbeitsmappe mit dem angegebenen Druckerpapierformat
type: docs
weight: 430
url: /de/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 Sie können das Druckerpapierformat Ihrer Wahl angeben, während Sie Ihre Arbeitsmappe mit verwenden[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) Methode. Bitte beachten Sie, dass beim Erstellen einer neuen Datei in MS Excel das Papierformat mit der Einstellung des Standarddruckers in Ihrem Gerät übereinstimmt.

{{% /alert %}}

 Der folgende Beispielcode veranschaulicht die Verwendung von[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) Methode. Es erstellt zuerst eine Arbeitsmappe und speichert sie dann im Speicherstrom im XLSX-Format. Dann lädt es es mit A5-Papiergröße und speichert es im PDF-Format. Dann lädt es es wieder mit A3-Papiergröße und speichert es wieder im PDF-Format. Wenn Sie die Ausgabe-PDFs öffnen und ihre Papiergröße überprüfen, werden Sie feststellen, dass sie unterschiedlich sind. Einer ist A5 und der andere ist A3. Bitte laden Sie die herunter[A5-Ausgabe-PDF](5115234.pdf) und[A3-Ausgabe-PDF](5115233.pdf) generiert durch den Code für Ihre Referenz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}

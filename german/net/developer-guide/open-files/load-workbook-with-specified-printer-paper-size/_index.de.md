---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 430
url: /de/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Sie können die Druckerpapiergröße Ihrer Wahl beim Laden Ihres Arbeitsbuches mit der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)-Methode angeben. Bitte beachten Sie, wenn Sie eine neue Datei in MS Excel erstellen, finden Sie die Papiergröße ist dieselbe wie die Einstellung des Standarddruckers in Ihrem Gerät.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht die Verwendung der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) Methode. Zuerst wird eine Arbeitsmappe erstellt, dann wird sie im XLSX-Format in einem MemoryStream gespeichert. Anschließend wird sie mit der Papiergröße A5 geladen und im PDF-Format gespeichert. Dann wird sie erneut mit der Papiergröße A3 geladen und erneut im PDF-Format gespeichert. Wenn Sie die Ausgabe-PDFs öffnen und ihre Papiergröße überprüfen, werden Sie feststellen, dass sie unterschiedlich sind. Eines ist A5 und das andere ist A3. Laden Sie zur Verfügung, bitte das [A5-Ausgabe-PDF](5115234.pdf) und das [A3-Ausgabe-PDF](5115233.pdf) herunter, die vom Code generiert wurden, um sie zu überprüfen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

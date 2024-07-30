---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 430
url: /de/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Sie können die Druckerpapiergröße Ihrer Wahl beim Laden Ihres Arbeitsbuches mit der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)-Methode angeben. Bitte beachten Sie, wenn Sie eine neue Datei in MS Excel erstellen, finden Sie die Papiergröße ist dieselbe wie die Einstellung des Standarddruckers in Ihrem Gerät.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht die Verwendung der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)-Methode. Zuerst wird eine Arbeitsmappe erstellt, dann wird sie im Speicher als XLSX-Datei gespeichert. Anschließend wird sie mit dem Papierformat A5 geladen und als PDF-Datei gespeichert. Dann wird sie erneut mit dem Papierformat A3 geladen und wieder als PDF-Datei gespeichert. Wenn Sie die Ausgabe-PDFs öffnen und deren Papierformat überprüfen, werden Sie feststellen, dass sie unterschiedlich sind. Eines ist A5 und das andere ist A3. Laden Sie bitte die [A5 Ausgabe-PDF-Datei](PrinterSize-a5_out.pdf) und die [A3 Ausgabe-PDF-Datei](PrinterSize-a3_out.pdf) herunter, die vom Code für Ihre Referenz generiert wurden.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}

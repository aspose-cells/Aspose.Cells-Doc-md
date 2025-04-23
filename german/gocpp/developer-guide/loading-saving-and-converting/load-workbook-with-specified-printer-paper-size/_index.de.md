---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 430
url: /de/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Sie können die Papiergröße Ihres Druckers beim Laden Ihrer Arbeitsmappe mit der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/)-Methode festlegen. Bitte beachten Sie, dass bei einer neuen Datei in MS Excel die Papiergröße auf die Standardeinstellung Ihres Druckers eingestellt ist.

{{% /alert %}}

Das folgende Beispiel zeigt die Verwendung der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/)-Methode. Es erstellt zuerst eine Arbeitsmappe und speichert sie in einem Speicher-Stream im XLSX-Format. Dann lädt es diese mit A5-Papierformat und speichert sie erneut als PDF. Anschließend lädt es sie mit A3-Papiergröße und speichert wieder im PDF-Format. Wenn Sie die Ausgabepdfs öffnen und deren Papiergröße überprüfen, sehen Sie die Unterschiede. Ein PDF ist A5, das andere A3. Laden Sie die [A5-Ausgabepdf](PrinterSize-a5_out.pdf) und [A3-Ausgabepdf](PrinterSize-a3_out.pdf) herunter, die vom Code erzeugt wurden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}

---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 430
url: /de/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Sie können die Druckerpapiergröße Ihrer Wahl beim Laden Ihres Arbeitsbuches mit der [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)-Methode angeben. Bitte beachten Sie, wenn Sie eine neue Datei in MS Excel erstellen, finden Sie die Papiergröße ist dieselbe wie die Einstellung des Standarddruckers in Ihrem Gerät.

{{% /alert %}}

Der folgende Beispielcode zeigt die Verwendung der Methode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Er erstellt zuerst ein Workbook, speichert es dann im Arbeitsspeicher im XLSX-Format, lädt es mit A5-Papierformat und speichert es im PDF-Format. Anschließend lädt es erneut mit A3-Papierformat und speichert es wieder im PDF-Format. Wenn Sie die Ausgabedateien öffnen und ihre Papiergröße prüfen, sehen Sie, dass sie unterschiedlich sind. Eine ist A5 und die andere A3. Laden Sie die [A5-Ausgabepdf](PrinterSize-a5_out.pdf) und die [A3-Ausgabepdf](PrinterSize-a3_out.pdf) herunter, die vom Code generiert wurden.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

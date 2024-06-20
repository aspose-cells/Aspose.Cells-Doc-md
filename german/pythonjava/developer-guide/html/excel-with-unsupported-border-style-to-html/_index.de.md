---
title: Excel mit nicht unterstütztem Rahmenstil zu HTML
type: docs
weight: 80
url: /de/python-java/excel-with-unsupported-border-style-to/
---

## **Excel mit nicht unterstütztem Rahmenstil zu HTML**
Microsoft Excel unterstützt bestimmte gestrichelte Rahmenarten, die von Webbrowsern nicht unterstützt werden. Wenn solche Dateien mit Aspose.Cells in HTML konvertiert werden, werden diese Rahmen entfernt. Aspose.Cells für Python via Java unterstützt das Anzeigen ähnlicher Rahmen mit der Eigenschaft [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). Sie können den Wert der Eigenschaft [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) auf **True** setzen, um nicht unterstützte Rahmen zu exportieren.

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](sampleExportSimilarBorderStyle.xlsx), die einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Auswirkung der Eigenschaft [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) in der [Ausgabedatei HTML](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}

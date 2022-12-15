---
title: Excel mit nicht unterstütztem Rahmenstil zu HTML
type: docs
weight: 80
url: /de/python-java/excel-with-unsupported-border-style-to/
---
## **Excel mit nicht unterstütztem Rahmenstil zu HTML**
Microsoft Excel unterstützt einige Arten von gestrichelten Rahmen, die von Webbrowsern nicht unterstützt werden. Wenn solche Dateien mit Aspose.Cells in HTML konvertiert werden, werden diese Ränder entfernt. Aspose.Cells for Python via Java unterstützt jedoch die Anzeige ähnlicher Rahmen mit[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)Eigentum. Sie können den Wert von festlegen[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) Eigentum zu**WAHR** nicht unterstützte Grenzen zu exportieren.

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](sampleExportSimilarBorderStyle.xlsx)das einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Wirkung von[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)Eigentum innerhalb der[HTML ausgeben](outputExportSimilarBorderStyle.zip).

![todo: Bild_alt_Text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}

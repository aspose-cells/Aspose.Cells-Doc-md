---
title: Verhindern Sie den Export von versteckten Arbeitsblattinhalten beim Speichern unter HTML
type: docs
weight: 90
url: /de/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen unter HTML speichern. Wenn die Arbeitsmappe jedoch ausgeblendete Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig den Inhalt der ausgeblendeten Arbeitsblätter in die Ausgabe HTML (_ files)-Verzeichnis, das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angebracht, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Wenn beispielsweise das ausgeblendete Arbeitsblatt Bilder enthält, die nicht in die exportiert werden sollen_Dateien Verzeichnis.

{{% /alert %}}

Aspose.Cells bietet die[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) Eigentum. Standardmäßig ist die[**Verstecktes Arbeitsblatt exportieren**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) Eigenschaft eingestellt ist**wahr**. Wenn du es einstellst**FALSCH**, dann exportiert Aspose.Cells keine versteckten Arbeitsblattinhalte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Neben der Steuerung, ob ausgeblendete Arbeitsblätter exportiert werden sollen oder nicht, können Sie auch zusätzliche Einstellungen für den Export von Arbeitsmappen nach HTML konfigurieren. Die folgenden Artikel zeigen andere Funktionen, die von Aspose.Cells zum Exportieren von Arbeitsmappen nach HTML unterstützt werden.

- [Konvertieren Sie Excel in HTML mit Überschriften](/cells/de/java/convert-excel-to-html-with-headings/)
- [Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus](/cells/de/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exportieren Sie Kommentare beim Speichern einer Excel-Datei unter HTML](/cells/de/java/export-comments-while-saving-excel-file-to-html/)
- [Ausblenden von überlagerten Inhalten mit CrossHideRight beim Speichern unter HTML](/cells/de/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exportieren Sie einen ähnlichen Rahmenstil, wenn der Rahmenstil nicht von Webbrowsern unterstützt wird](/cells/de/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)

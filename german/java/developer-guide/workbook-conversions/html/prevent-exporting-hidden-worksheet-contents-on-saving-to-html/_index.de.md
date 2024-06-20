---
title: Verhindern des Exports versteckter Arbeitsblattinhalte beim Speichern als HTML
type: docs
weight: 90
url: /de/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen in HTML speichern. Wenn die Arbeitsmappe jedoch versteckte Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig die versteckten Inhalte des Arbeitsblatts in das HTML-Ausgabeverzeichnis (_files), das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angemessen, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Zum Beispiel, wenn das versteckte Arbeitsblatt Bilder enthält, die nicht in das Verzeichnis _files exportiert werden sollen.

{{% /alert %}}

Aspose.Cells bietet die [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)-Eigenschaft. Standardmäßig ist die [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)-Eigenschaft auf **true** gesetzt. Wenn Sie sie auf **false** setzen, exportiert Aspose.Cells die versteckten Arbeitsblattinhalte nicht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Neben der Kontrolle, ob versteckte Arbeitsblätter exportiert werden sollen oder nicht, können Sie auch zusätzliche Einstellungen für den Export von Arbeitsmappen in HTML konfigurieren. Die folgenden Artikel zeigen weitere Funktionen, die von Aspose.Cells für den Export von Arbeitsmappen in HTML unterstützt werden.

- [Excel in HTML mit Überschriften konvertieren](/cells/de/java/convert-excel-to-html-with-headings/)
- [Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen](/cells/de/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Kommentare beim Speichern einer Excel-Datei in HTML exportieren](/cells/de/java/export-comments-while-saving-excel-file-to-html/)
- [Überlagerter Inhalt mit CrossHideRight beim Speichern in HTML ausblenden](/cells/de/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird](/cells/de/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)

---
title: Förhindra export av dolt kalkylbladsinnehåll vid sparande till HTML
type: docs
weight: 90
url: /sv/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells tillhandahåller [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)egenskapen. Som standard är [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)egenskapen inställd på **true**. Om du ställer in den till **false**, kommer inte Aspose.Cells att exportera innehållet på de dolda kalkylbladen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Förutom att kontrollera om dolda kalkylblad ska exporteras eller inte kan du också konfigurera ytterligare inställningar för att exportera arbetsboken till HTML. Följande artiklar visar andra funktioner som stöds av Aspose.Cells för att exportera arbetsböcker till HTML.

- [Konvertera Excel till HTML med rubriker](/cells/sv/java/convert-excel-to-html-with-headings/)
- [Uteslut oanvända stilar under Excel till HTML-konvertering](/cells/sv/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exportera kommentarer vid sparande av Excel-fil till HTML](/cells/sv/java/export-comments-while-saving-excel-file-to-html/)
- [Dölja överlagt innehåll med CrossHideRight vid sparande till HTML](/cells/sv/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exportera liknande kantstilmall när kantstil inte stöds av webbläsare](/cells/sv/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)

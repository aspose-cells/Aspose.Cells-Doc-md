---
title: Förhindra export av dolt kalkylbladsinnehåll när du sparar till HTML
type: docs
weight: 90
url: /sv/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Men om arbetsboken innehåller dolda kalkylblad, exporterar Aspose.Cells som standard det dolda kalkylbladets innehåll till HTML-utdata (_ files) katalog som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, etc. Ibland är det inte lämpligt att exportera innehållet i de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte bör exporteras till_filer katalog.

{{% /alert %}}

Aspose.Cells tillhandahåller[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) fast egendom. Som standard är[**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) egenskapen är inställd på**Sann**. Om du ställer in den på**falsk**, då kommer Aspose.Cells inte att exportera dolt kalkylbladsinnehåll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Förutom att kontrollera om du vill exportera dolda kalkylblad eller inte, kan du också konfigurera ytterligare inställningar för att exportera arbetsbok till HTML. Följande artiklar visar andra funktioner som stöds av Aspose.Cells för export av arbetsböcker till HTML.

- [Konvertera Excel till HTML med rubriker](/cells/sv/java/convert-excel-to-html-with-headings/)
- [Uteslut oanvända stilar under konvertering av Excel till HTML](/cells/sv/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exportera kommentarer medan du sparar Excel-fil till HTML](/cells/sv/java/export-comments-while-saving-excel-file-to-html/)
- [Döljer överlagrat innehåll med CrossHideRight medan du sparar till HTML](/cells/sv/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exportera liknande kantstil när kantstil inte stöds av webbläsare](/cells/sv/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)

---
title: Förhindra export av dolt kalkylbladsinnehåll när du sparar till HTML
type: docs
weight: 210
url: /sv/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Men om arbetsboken innehåller dolda kalkylblad, exporterar Aspose.Cells som standard det dolda kalkylbladets innehåll till HTML-utgången (_ files) katalog som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, etc. Ibland är det inte lämpligt att exportera innehållet i de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte bör exporteras till_filer katalog.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) fast egendom. Som standard är den inställd på**Sann** och dolda kalkylblad exporteras till HTML. Om du ställer in det**falsk**, Aspose.Cells kommer inte att exportera dolt kalkylbladsinnehåll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}


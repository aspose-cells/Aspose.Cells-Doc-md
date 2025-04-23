---
title: Förhindra export av dolt kalkylbladsinnehåll vid sparande till HTML
type: docs
weight: 210
url: /sv/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells tillhandahåller [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet)-egenskapen. Som standard är den inställd på **true** och dolda arbetsblad exporteras till HTML. Om du anger den till **false**, kommer inte Aspose.Cells att exportera innehållet på dolda arbetsblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}


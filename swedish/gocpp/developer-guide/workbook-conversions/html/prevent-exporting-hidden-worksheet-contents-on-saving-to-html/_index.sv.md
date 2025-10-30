---
title: Förhindra att dölja kalkylbladets innehåll vid sparning till HTML med Golang via C++
linktitle: Förhindra export av dolt arbetsbladinnehåll
type: docs
weight: 210
url: /sv/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Lär dig hur du förhindrar export av dolt arbetsbladinnehåll när du sparar Excel arbetsböcker till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells tillhandahåller [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/)-egenskapen. Som standard är den inställd på **true** och dolda arbetsblad exporteras till HTML. Om du anger den till **false**, kommer inte Aspose.Cells att exportera innehållet på dolda arbetsblad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}

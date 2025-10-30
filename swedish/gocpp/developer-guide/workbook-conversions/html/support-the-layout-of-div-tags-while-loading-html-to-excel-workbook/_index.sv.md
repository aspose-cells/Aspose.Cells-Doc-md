---
title: Stöd layouten för DIV taggar vid inläsning av HTML till Excel arbetsbok med Golang via C++
linktitle: Stöd för DIV Taggars layout
type: docs
weight: 50
url: /sv/go-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: Lär dig hur man stödjer layouten av DIV taggar när du laddar HTML till en Excel arbetsbok med hjälp av Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

 Vanligtvis ignoreras layouten för DIV-taggar vid inläsning av HTML till ett Excel arbetsboksobjekt. Men om du vill att layouten för DIV-taggar ska bevaras, ställ in egenskapen [GetSupportDivTag()](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getsupportdivtag/) till **true**. Standardvärdet för denna egenskap är **false**.

{{% /alert %}} 

Följande exempelillustrerar användningen av egenskapen [GetSupportDivTag()](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getsupportdivtag/). Vänligen ladda ner [Aspose-logotypen](5115218.png) som används i inmatnings HTML och [utdata Excel-filen](5115220.xlsx) genererad av koden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SupportTheLayoutOfDivTagsWhileLoadingHtmlToExcelWorkbook.go" >}}

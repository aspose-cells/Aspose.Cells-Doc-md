---  
title: Ta bort oanvända stilar i arbetsboken med Golang via C++  
linktitle: Ta bort oanvända stilar inne i arbetsboken  
type: docs  
weight: 340  
url: /sv/go-cpp/remove-unused-styles-inside-the-workbook/  
description: Ta bort oanvända stilar i Excel arbetsboken med Aspose.Cells med Golang via C++.  
---  

{{% alert color="primary" %}}  

Oanvända stilar i Excel-filer tar inte bara upp utrymme utan kan också orsaka prestandaproblem vid konvertering till olika format som PDF, HTML etc. Aspose.Cells tillhandahåller [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) för att ta bort alla oanvända stilar i arbetsboken.  

{{% /alert %}}  

Följande kod förklarar användningen av [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/). Koden laddar [mallexcelfilen](5115520.xlsx) som du kan ladda ner från länken. Den innehåller en oanvänd stil som heter **AsposeStyle**; denna stil och alla andra oanvända stilar tas bort efter körning.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}

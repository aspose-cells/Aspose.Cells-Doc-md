---
title: Ta bort oanvända stilar i arbetsboken
type: docs
weight: 340
url: /sv/net/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}}

Oanvända stilar i excel-filer tar inte bara plats utan orsakar även prestandaproblem vid konvertering till olika format som PDF, HTML, etc. Aspose.Cells tillhandahåller[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) för att ta bort alla oanvända stilar i arbetsboken.

{{% /alert %}}

 Följande kod förklarar användningen av[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) . Koden laddar[mall excel-fil](5115520.xlsx) som du kan ladda ner från den medföljande länken. Den innehåller en oanvänd stil som heter**AsposeStil**, kommer denna stil och alla andra oanvända stilar att tas bort efter exekvering av koden.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}

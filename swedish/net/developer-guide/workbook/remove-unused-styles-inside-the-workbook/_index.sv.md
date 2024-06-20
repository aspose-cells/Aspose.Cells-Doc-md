---
title: Ta bort oanvända stilar inne i arbetsboken
type: docs
weight: 340
url: /sv/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Oanvända stilar i excelfilen tar inte bara plats utan orsakar också prestandaproblem vid konvertering till olika format som PDF, HTML, etc. Aspose.Cells tillhandahåller [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) för att ta bort alla oanvända stilar inne i arbetsboken.

{{% /alert %}}

Följande kod förklarar användningen av [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles). Koden laddar den [mall excelfil](5115520.xlsx) som du kan ladda ner från den medföljande länken. Den innehåller en oanvänd stil med namnet **AsposeStyle**, den här stilen och alla andra oanvända stilar kommer att tas bort efter att koden har körts.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}

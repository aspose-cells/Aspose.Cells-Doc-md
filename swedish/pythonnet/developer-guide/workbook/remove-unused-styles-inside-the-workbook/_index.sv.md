---
title: Ta bort oanvända stilar inne i arbetsboken
type: docs
weight: 340
url: /sv/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Onödiga stilar i Excel-fil tar inte bara plats utan orsakar också prestandaproblem vid konvertering till olika format som PDF, HTML, etc. Aspose.Cells för Python via .NET tillhandahåller [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) för att ta bort alla oanvända stilar i arbetsboken.

{{% /alert %}}

Följande kod förklarar användningen av [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). Koden laddar den [mall excelfil](5115520.xlsx) som du kan ladda ner från den medföljande länken. Den innehåller en oanvänd stil med namnet **AsposeStyle**, den här stilen och alla andra oanvända stilar kommer att tas bort efter att koden har körts.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

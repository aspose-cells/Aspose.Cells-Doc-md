---
title: Släpp okontrollerade resurser för arbetsboken i Python via .NET
linktitle: Släpp okontrollerade resurser
type: docs
weight: 310
url: /sv/python-net/release-unmanaged-resources-of-the-workbook/
description: Lär dig hur du ordentligt släpper okontrollerade resurser när du arbetar med Excel arbetsböcker med Aspose.Cells för Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)-metoden för att släppa okontrollerade resurser för [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-objektet. Denna mönster är avgörande för hantering av okontrollerade resurser som filhandtag, strömmar eller minnesallokeringar som inte hanteras automatiskt av Pythons garbage collector.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen implementerar Pythons kontexthanteringsprotokoll för resursförvaltning. Du kan antingen explicit anropa [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)-metoden eller använda Pythons `with`-sats för att säkerställa korrekt städning.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
{{< app/cells/assistant language="python-net" >}}

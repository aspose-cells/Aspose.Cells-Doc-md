---
title: Unmanaged Ressourcen der Arbeitsmappe mit Python via .NET freigeben
linktitle: Unmanaged Ressourcen freigeben
type: docs
weight: 310
url: /de/python-net/release-unmanaged-resources-of-the-workbook/
description: Erfahren Sie, wie Sie Ressourcen richtig freigeben, wenn Sie mit Arbeitsmappen in Excel mittels Aspose.Cells for Python via .NET arbeiten.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)-Methode, um unmanaged Ressourcen des [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Objekts freizugeben. Dieses Muster ist essenziell für die Handhabung unmanaged Ressourcen wie Dateihandles, Streams oder Speicherzuweisungen, die nicht automatisch vom Python-Garbage-Collector verwaltet werden.

{{% /alert %}}

Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse implementiert das Kontext-Manager-Protokoll von Python für das Ressourcenmanagement. Sie können entweder explizit die [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)-Methode aufrufen oder die `with`-Anweisung von Python verwenden, um eine ordnungsgemäße Bereinigung sicherzustellen.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
{{< app/cells/assistant language="python-net" >}}

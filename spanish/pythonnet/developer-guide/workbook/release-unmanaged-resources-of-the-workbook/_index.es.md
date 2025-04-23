---
title: Liberar recursos no gestionados del libro de trabajo con Python via .NET
linktitle: Liberar recursos no gestionados
type: docs
weight: 310
url: /es/python-net/release-unmanaged-resources-of-the-workbook/
description: Aprende cómo liberar correctamente los recursos no gestionados al trabajar con libros de Excel usando Aspose.Cells para Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) para liberar recursos no gestionados del objeto [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Este patrón es crucial para manejar recursos no gestionados como manejadores de archivos, flujos o asignaciones de memoria que no son gestionadas automáticamente por el recolector de basura de Python.

{{% /alert %}}

La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) implementa el protocolo del gestor de contexto de Python para la gestión de recursos. Puedes llamar explícitamente al método [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) o usar la declaración `with` de Python para garantizar una limpieza adecuada.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```

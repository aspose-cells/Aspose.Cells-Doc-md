---
title: Configurar el modo de cálculo de fórmulas del libro de trabajo con Python.NET
linktitle: Configuración del modo de cálculo de fórmulas del libro de trabajo
type: docs
weight: 110
url: /es/python-net/setting-formula-calculation-mode-of-workbook/
description: Aprenda cómo establecer el modo de cálculo de fórmulas (automático, manual) en libros de trabajo de Excel usando Aspose.Cells para la API de Python via .NET. Guía paso a paso con ejemplos de código.
keywords: Python, Aspose.Cells, Excel, libro de trabajo, modo de cálculo de fórmulas, automático, manual, configuraciones
---

## ** Configuración del modo de cálculo de fórmulas en el libro de trabajo**

{{% alert color="primary" %}}

Microsoft Excel ofrece tres modos de cálculo de fórmulas:
- **Automático**: Recalcula las fórmulas en cada cambio y al abrir el libro de trabajo
- **Automático excepto para tablas de datos**: Recalcula las fórmulas excepto las tablas de datos en cambios
- **Manual**: Solo recalcule cuando el usuario lo solicite (F9/CTRL+ALT+F9) o durante el guardado

{{% /alert %}}

### ** Configuración del modo de cálculo con Aspose.Cells**

Aspose.Cells para Python via .NET proporciona la configuración [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) a través de la propiedad [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Use el atributo [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) para controlar el comportamiento del cálculo.

 Modos disponibles a través del enum [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/):
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Pasos de implementación:**
1. Cargar el libro de trabajo existente o crear una nueva instancia
2. Acceder a la configuración del libro de trabajo
3. Establecer el modo de cálculo usando `formula_settings.calculation_mode`
4. Guardar el libro de trabajo modificado

```python
from aspose.cells import Workbook, CalcModeType

# Load source workbook
workbook = Workbook("source.xlsx")

# Configure manual calculation mode
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CalcModeType, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create a workbook
workbook = Workbook()

# Set the Formula Calculation Mode to Manual
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save the workbook
output_path = os.path.join(data_dir, "output_out.xlsx")
workbook.save(output_path, SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}

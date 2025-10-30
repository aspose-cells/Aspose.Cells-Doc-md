---
title: Inställning av formelberäkningsläge för arbetsbok med Python.NET
linktitle: Ställa in formelberäkningsläget för arbetsboken
type: docs
weight: 110
url: /sv/python-net/setting-formula-calculation-mode-of-workbook/
description: Lär dig hur man ställer in formelberäkningsläge (automatiskt, manuellt) i Excel arbetsböcker med Aspose.Cells för Python via .NET API. Steg för steg guide med kodexempel.
keywords: Python, Aspose.Cells, Excel, arbetsbok, formelberäkningsläge, automatiskt, manuellt, inställningar
---

## **Ställa in formelberäkningsläge i arbetsbok**

{{% alert color="primary" %}}

Microsoft Excel erbjuder tre formelberäkningslägen:
- **Automatiskt**: Omberäknar formler vid varje ändring och vid öppning av arbetsboken
- **Automatiskt förutom datatabeller**: Omberäknar formler förutom datatabeller vid ändringar
- **Manuellt**: Omberäknar endast när användaren begär (F9/CTRL+ALT+F9) eller vid sparning

{{% /alert %}}

### **Ställa in beräkningsläge med Aspose.Cells**

Aspose.Cells för Python via .NET tillhandahåller konfigurationen [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) via egenskapen [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Använd attributet [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) för att styra beräkningsbeteendet.

Tillgängliga lägen via [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/) enum:
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Implementeringssteg:**
1. Ladda befintlig arbetsbok eller skapa en ny instans
2. Åtkomst till arbetsbokens inställningar
3. Ställ in beräkningsläge med `formula_settings.calculation_mode`
4. Spara den ändrade arbetsboken

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

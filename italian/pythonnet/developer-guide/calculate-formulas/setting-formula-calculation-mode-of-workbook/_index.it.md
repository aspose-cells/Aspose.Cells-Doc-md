---
title: Impostare la modalità di calcolo delle formule del Workbook con Python.NET
linktitle: Impostazione della modalità di calcolo delle formule di Workbook
type: docs
weight: 110
url: /it/python-net/setting-formula-calculation-mode-of-workbook/
description: Impara come impostare la modalità di calcolo delle formule (automatico, manuale) nei workbook Excel usando Aspose.Cells per Python via .NET API. Guida passo passo con esempi di codice.
keywords: Python, Aspose.Cells, Excel, workbook, modalità di calcolo delle formule, automatica, manuale, impostazioni
---

## **Impostare la modalità di calcolo delle formule nel Workbook**

{{% alert color="primary" %}}

Microsoft Excel fornisce tre modalità di calcolo delle formule:
- **Automatico**: Ricalcola le formule ad ogni modifica e all'apertura del workbook
- **Automatico tranne che per le tabelle di dati**: Ricalcola le formule tranne le tabelle di dati durante le modifiche
- **Manuale**: Ricalcola solo quando l'utente lo richiede (F9/CTRL+ALT+F9) o durante il salvataggio

{{% /alert %}}

### **Impostare la modalità di calcolo con Aspose.Cells**

Aspose.Cells per Python via .NET fornisce la configurazione [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) tramite la proprietà [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Usa l'attributo [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) per controllare il comportamento del calcolo.

Modalità disponibili tramite enum [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/):
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Passaggi di implementazione:**
1. Caricare il workbook esistente o crearne uno nuovo
2. Accedere alle impostazioni del workbook
3. Impostare la modalità di calcolo usando `formula_settings.calculation_mode`
4. Salvare il workbook modificato

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

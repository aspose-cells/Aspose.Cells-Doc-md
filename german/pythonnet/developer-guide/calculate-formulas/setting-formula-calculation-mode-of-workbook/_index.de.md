---
title: Einstellung des Formelfeldberechnungsmodus des Arbeitsbuchs mit Python.NET
linktitle: Einstellen des Formelberechnungsmodus der Arbeitsmappe
type: docs
weight: 110
url: /de/python-net/setting-formula-calculation-mode-of-workbook/
description: Erfahren Sie, wie Sie den Berechnungsmodus (automatisch, manuell) in Excel Arbeitsmappen mit Aspose.Cells für Python via .NET API einstellen. Schritt für Schritt Anleitung mit Codebeispielen.
keywords: Python, Aspose.Cells, Excel, Arbeitsmappe, Formelfeldberechnungsmodus, automatisch, manuell, Einstellungen
---

## **Einstellung des Formelfeldberechnungsmodus in der Arbeitsmappe**

{{% alert color="primary" %}}

Microsoft Excel bietet drei Modi für die Formelfeldberechnung:
- **Automatisch**: Formeln werden bei jeder Änderung und beim Öffnen der Arbeitsmappe neu berechnet
- **Automatisch außer für Datentabellen**: Formeln werden bei Änderungen neu berechnet, außer für Datentabellen
- **Manuell**: Nur bei Benutzeranforderung (F9/CTRL+ALT+F9) oder beim Speichern neu berechnet

{{% /alert %}}

### **Einstellung des Berechnungsmodus mit Aspose.Cells**

Aspose.Cells für Python via .NET bietet die Konfiguration [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) über die Eigenschaft [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Verwenden Sie das Attribut [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/), um das Berechnungsverhalten zu steuern.

Verfügbare Modi über das [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/)-Enum:
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Implementierungsschritte:**
1. Laden Sie das vorhandene Arbeitsbuch oder erstellen Sie eine neue Instanz
2. Zugriff auf die Arbeitseinstellungen
3. Stellen Sie den Berechnungsmodus ein mit `formula_settings.calculation_mode`
4. Speichern Sie das geänderte Arbeitsbuch

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

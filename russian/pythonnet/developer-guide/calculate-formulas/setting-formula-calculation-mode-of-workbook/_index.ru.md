---
title: Установка режима расчетов формул книги с помощью Python.NET
linktitle: Установка режима расчета формул в книге Excel
type: docs
weight: 110
url: /ru/python-net/setting-formula-calculation-mode-of-workbook/
description: Узнайте, как установить режим расчетов формул (автоматический, ручной) в рабочих книгах Excel с помощью Aspose.Cells для Python via .NET. Пошаговое руководство с примерами кода.
keywords: Python, Aspose.Cells, Excel, рабочая книга, режим расчетов формул, автоматический, ручной, настройки
---

## **Установка режима расчетов формул в рабочей книге**

{{% alert color="primary" %}}

Microsoft Excel предлагает три режима вычисления формул:
- **Автоматический**: пересчет формул при каждом изменении и при открытии книги
- **Автоматический, кроме таблиц данных**: пересчет формул за исключением таблиц данных при изменениях
- **Ручной**: пересчет только по запросу пользователя (F9/CTRL+ALT+F9) или при сохранении

{{% /alert %}}

### **Настройка режима вычислений с помощью Aspose.Cells**

Aspose.Cells для Python via .NET предоставляет конфигурацию [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) через свойство [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). Используйте атрибут [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) для управления поведением расчетов.

Доступные режимы через перечисление [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/):
- `АВТОМАТИЧЕСКИЙ`
- `ИСКЛЮЧЕНИЕ_ИЗ_АВТОМАТИЧЕСКОГО`
- `РУЧНОЙ`

**Этапы реализации:**
1. Загрузите существующую рабочую книгу или создайте новый экземпляр
2. Получите доступ к настройкам книги
3. Установите режим вычислений с помощью `formula_settings.calculation_mode`
4. Сохраните измененную рабочую книгу

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

---
title: Python.NET ile Çalışmaya Kitaplıkta Formül Hesaplama Modunu Ayarlama
linktitle: Çalışbook un Formül Hesaplama Modunu Ayarlama
type: docs
weight: 110
url: /tr/python-net/setting-formula-calculation-mode-of-workbook/
description: Aspose.Cells for Python via .NET API kullanarak Excel çalışma kitaplarında formül hesaplama modunu (otomatik, manuel) nasıl ayarlayacağınızı öğrenin. Adım adım kod örnekleriyle rehber.
keywords: Python, Aspose.Cells, Excel, çalışma kitabı, formül hesaplama modu, otomatik, manuel, ayarlar
---

## **Çalışma Kitabında Formül Hesaplama Modunu Ayarlama**

{{% alert color="primary" %}}

Microsoft Excel üç farklı formül hesaplama modu sağlar:
- **Otomatik**: Formülleri her değişiklikte ve çalışma kitabı açıldığında yeniden hesaplar
- **Veri tabloları hariç otomatik**: Yalnızca veri tabloları dışındaki formülleri değişikliklerde yeniden hesaplar
- **Manuel**: Sadece kullanıcı isteğiyle (F9/CTRL+ALT+F9) veya kaydedilirken yeniden hesaplar

{{% /alert %}}

### **Aspose.Cells ile Hesaplama Modu Ayarlama**

Aspose.Cells for Python via .NET, `[**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/)` yapılandırmasını `[**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/)` özelliği aracılığıyla sunar. Hesaplama davranışını kontrol etmek için `[**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/)` özniteliğini kullanın.

Mevcut modlar `[**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/)` enum ile erişilebilir:
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**Uygulama Adımları:**
1. Mevcut çalışma kitabını yükleyin veya yeni örnek oluşturun
2. Çalışma kitabı ayarlarına erişin
3. `formula_settings.calculation_mode` kullanarak hesaplama modunu ayarlayın
4. Değiştirilmiş çalışma kitabını kaydedin

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

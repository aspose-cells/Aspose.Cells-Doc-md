---
title: Отключить CSS при сохранении в HTML с помощью Python.NET
linktitle: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/python-net/disable-css-while-saving-to-html/
description: Узнайте, как отключить стили CSS при сохранении файлов Excel в формат HTML с помощью API Aspose.Cells for Python via .NET.
---

## **Возможные сценарии использования**

При сохранении файла Excel в одностраничный HTML, элементы CSS обычно встроены внутри файла HTML и располагаются в разделе HEAD. Если прикрепить этот файл в качестве содержимого/тела электронной почты, большинство почтовых клиентов удалят CSS-элементы, что приведет к неправильному отображению. API Aspose.Cells for Python via .NET добавляет опцию, которая позволяет по желанию отключить CSS, чтобы стили применялись непосредственно внутри элементов HTML. Если вы хотите установить HTML как содержимое тела письма, используйте свойство [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) и установите его значение в **True**.

## **Отключить CSS при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **Образец кода**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}

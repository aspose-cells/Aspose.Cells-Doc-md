---
title: Включить пользовательские свойства CSS при сохранении в HTML с помощью Python.NET
linktitle: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/python-net/enable-css-custom-properties-while-saving-to-html/
description: Узнайте, как включить пользовательские свойства CSS при сохранении файлов Excel в HTML с помощью API Aspose.Cells for Python via .NET.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, если в нем встречается несколько одинаковых изображений base64, использование пользовательских свойств CSS позволяет сохранять данные изображения только один раз. Это повышает производительность итогового HTML. Используйте атрибут [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) и установите его в **True** при сохранении в HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример демонстрирует использование атрибута [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/). Скриншот показывает эффект, когда этот параметр не установлен в True. Скачайте [пример файла Excel](50528260.xlsx), использованный в этом коде, и [сгенерированный HTML](50528261.zip) для ознакомления.

## **Образец кода**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}

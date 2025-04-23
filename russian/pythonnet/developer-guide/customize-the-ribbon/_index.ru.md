---
title: Настройка XML ленты с помощью Python via .NET
linktitle: Настроить меню Excel
type: docs
weight: 1500
url: /ru/python-net/customizing-the-ribbon-xml/
description: Чтение, запись и управление настройками Ribbon XML с использованием Aspose.Cells для Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office заменил меню и панели инструментов на ленту в верхней части окна приложения с Office 2007. Лента настраиваема. 
Aspose.Cells позволяет вам:

- Оставляйте Ribbon XML без разбора
- Чтение и запись Ribbon XML без разбора
- Получение и установка данных Ribbon XML

Если вы хотите изменить XML-ленту, вам нужно его проанализировать с помощью парсера XML или другого инструмента для работы с XML-лентой.

{{% /alert %}}

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

wb = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
xml_path = os.path.join(data_dir, "CustomUI.xml")

with open(xml_path, 'r') as sr:
    wb.ribbon_xml = sr.read()
```

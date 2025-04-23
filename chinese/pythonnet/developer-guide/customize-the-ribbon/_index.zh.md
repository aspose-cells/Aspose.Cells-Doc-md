---
title: 使用 Python via .NET 自定义 Ribbon XML
linktitle: 自定义Excel菜单
type: docs
weight: 1500
url: /zh/python-net/customizing-the-ribbon-xml/
description: 使用 Aspose.Cells for Python via .NET API 读写和管理 Excel Ribbon XML 自定义。
---

{{% alert color="primary" %}} 

自2007 年版起，Microsoft Office 用 Ribbon 替代菜单栏和工具栏，并且 Ribbon 可以自定义。 
Aspose.Cells 允许你：

- 保持 Ribbon XML 而不解析
- 读写 Ribbon XML 而不解析
- 获取和设置 Ribbon XML 数据

如果要更改Ribbon XML，则必须使用XML解析器或其他Ribbon XML工具解析它。

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

---
title: カスタマイズされたリボンXMLをPythonで作成 via .NET
linktitle: Excelメニューのカスタマイズ
type: docs
weight: 1500
url: /ja/python-net/customizing-the-ribbon-xml/
description: Aspose.Cells for Python via .NET APIを使用したExcelリボンXMLの読み取り、書き込み、管理方法。
---

{{% alert color="primary" %}} 

Microsoft Officeは2007以降、メニューやツールバーを廃止し、アプリケーションウィンドウの上部にリボンを配置しています。リボンはカスタマイズ可能です。 
Aspose.Cellsは次のことを可能にします：

- リボンXMLをパースせずに保持する
- リボンXMLをパースせずに読み取りと書き込みを行う
- リボンXMLデータの取得と設定

リボンXMLを変更する場合は、XMLパーサーまたは他のリボンXMLツールで解析する必要があります。

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

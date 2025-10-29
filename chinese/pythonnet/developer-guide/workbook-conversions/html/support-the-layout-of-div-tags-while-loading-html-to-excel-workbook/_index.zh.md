---
title: 支持在用Python加载HTML到Excel工作簿时布局DIV标签 via .NET
linktitle: 支持HTML导入中的DIV标签布局
type: docs
weight: 50
url: /zh/python-net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: 学习如何在使用Aspose.Cells for Python via .NET导入HTML到Excel工作簿时，保持DIV标签的布局。实现HTML结构转换的精确控制。
---

{{% alert color="primary" %}} 

 通常，在将HTML加载到Excel工作簿对象时，会忽略div标签的布局。然而，如果你希望保留div标签的布局，可以将[HtmlLoadOptions.support_div_tag](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/#support_div_tag)属性设置为**True**。此属性的默认值为**False**。

{{% /alert %}} 

 以下示例代码演示了如何使用[HtmlLoadOptions.support_div_tag](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/#support_div_tag)属性。请下载示例中使用的输入HTML的Aspose Logo(5115218.png) 和生成的输出Excel文件(5115220.xlsx)。

```python
import os
import io
from aspose.cells import Workbook, HtmlLoadOptions, LoadFormat, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

export_html = f"""
<html>
<body>
    <table>
        <tr>
            <td>
                <div>This is some Text.</div>
                <div>
                    <div>
                        <span>This is some more Text</span>
                    </div>
                    <div>
                        <span>abc@abc.com</span>
                    </div>
                    <div>
                        <span>1234567890</span>
                    </div>
                    <div>
                        <span>ABC DEF</span>
                    </div>
                </div>
                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
            </td>
            <td>
                <img src="{os.path.join(data_dir, 'ASpose_logo_100x100.png')}" />
            </td>
        </tr>
    </table>
</body>
</html>"""

with io.BytesIO(export_html.encode('utf-8')) as ms:
    # Specify HTML load options, support div tag layouts
    load_options = HtmlLoadOptions(LoadFormat.HTML)
    load_options.support_div_tag = True

    # Create workbook object from the html using load options
    wb = Workbook(ms, load_options)

    # Auto fit rows and columns of first worksheet
    ws = wb.worksheets[0]
    ws.auto_fit_rows()
    ws.auto_fit_columns()

    # Save the workbook in xlsx format
    output_path = os.path.join(data_dir, "DivTagsLayout_out.xlsx")
    wb.save(output_path, SaveFormat.XLSX)
```

```python
from aspose.cells import HtmlLoadOptions, Workbook, SaveFormat

# Create HTML load options and enable DIV tag support
load_options = HtmlLoadOptions()
load_options.support_div_tag = True

# Load HTML file with DIV tag layout preservation
workbook = Workbook("input.html", load_options)

# Save the workbook with preserved layout
workbook.save("output.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}

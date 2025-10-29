---
title: 使用Python.NET应用高级条件格式
linktitle: 应用高级条件格式
type: docs
weight: 70
url: /zh/python-net/apply-advanced-conditional-formatting/
description: 学习如何用Aspose.Cells for Python via .NET实现Excel的高级条件格式功能，如数据条、颜色比例和图标集。
keywords: Python Excel格式，条件格式Python，数据条Python，颜色比例Python，图标集Python，Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007及以后的版本（2010/2013/2016）提供了高级的条件格式功能，包括单元格填充、边框、彩色图标、箭头、旗帜和字体格式。

{{% /alert %}} 

## **在Excel文件中实现高级条件格式**
Aspose.Cells for Python via .NET支持所有高级条件格式功能，包括：

- 使用数据条以图形化方式增强单元格中的基础数字，通过在单元格中嵌入简单的条形图。
- 根据它们与范围内其他单元格中的值的关系自动通过颜色比例给单元格着色。默认设置将最低值以红色着色，向上转为最高值以绿色着色。
- 以与颜色比例类似的方式使用图标集，但与给单元格着色不同，它向单元格中添加小图标，如箭头和交通灯。

Aspose.Cells 在运行时完全支持 Microsoft Excel 2007 年及以后版本在 XLSX 格式中提供的条件格式。此示例演示了包括图标集、数据条、颜色比例、时间周期、前/后和其他规则在内的高级条件格式类型的实参练习。

- [**Adding Color Scale Conditional Formattings**](/cells/zh/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/zh/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/zh/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/zh/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/zh/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/zh/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/zh/python-net/how-to-add-top10-conditional-formatting/)



### **计算Excel的颜色选择以进行颜色刻度格式化**
本代码显示了如何确定Excel为ColorScale条件格式规则选择的颜色：

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}

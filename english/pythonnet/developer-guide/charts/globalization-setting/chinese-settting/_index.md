---
title: Convert Chart to Image for Chinese Region with Python.NET
linktitle: Set Chinese Region
type: docs
weight: 9
url: /python-net/convert-chart-to-image-for-chinese-region/
description: Learn how to configure charts for Chinese regional settings using Aspose.Cells for Python.NET. Configure charts to support Chinese characters, fonts, text directions, and formatting.
keywords: Python Excel charts, Chinese chart configuration, Python chart localization, Aspose.Cells Python chart settings
aliases: [/python-net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

This guide demonstrates how to configure Chinese regional settings for charts using Aspose.Cells for Python.NET.

{{% /alert %}}

## **Define an Inherited Class**

First, create a class **ChartChineseSettings** that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartglobalizationsettings/). Override relevant methods to customize chart element text in Chinese:

```python
from aspose.cells.charts import ChartGlobalizationSettings, DisplayUnitType

class ChartChineseSetttings(ChartGlobalizationSettings):
    def get_axis_title_name(self) -> str:
        return "坐标轴标题"
    
    def get_axis_unit_name(self, type: DisplayUnitType) -> str:
        match type:
            case DisplayUnitType.NONE:
                return ""
            case DisplayUnitType.HUNDREDS:
                return "百"
            case DisplayUnitType.THOUSANDS:
                return "千"
            case DisplayUnitType.TEN_THOUSANDS:
                return "万"
            case DisplayUnitType.HUNDRED_THOUSANDS:
                return "十万"
            case DisplayUnitType.MILLIONS:
                return "百万"
            case DisplayUnitType.TEN_MILLIONS:
                return "千万"
            case DisplayUnitType.HUNDRED_MILLIONS:
                return "亿"
            case DisplayUnitType.BILLIONS:
                return "十亿"
            case DisplayUnitType.TRILLIONS:
                return "兆"
            case _:
                return ""
    
    def get_chart_title_name(self) -> str:
        return "图表标题"
    
    def get_legend_decrease_name(self) -> str:
        return "减少"
    
    def get_legend_increase_name(self) -> str:
        return "增加"
    
    def get_legend_total_name(self) -> str:
        return "汇总"
    
    def get_other_name(self) -> str:
        return "其他"
    
    def get_series_name(self) -> str:
        return "系列"
```

## **Configure Chinese Settings for Charts**

Use the custom **ChartChineseSettings** class to apply Chinese localization:

```python
from aspose.cells import Workbook
from aspose.cells.charts import Chart
import clr

# Load workbook and apply Chinese settings
wb = Workbook("Chinese.xls")
wb.settings.globalization_settings.chart_settings = ChartChineseSettings()

# Process chart and export
chart0 = wb.worksheets[0].charts[0]
chart0.to_image("Output.png")
```

This configuration ensures chart elements render with Chinese localization in the output image.

## **Implementation Notes**

Without proper Chinese configuration, chart elements may display in default English. After applying these settings:

|**Supported Element**|**Chinese Value**|**English Default**|
| :- | :- | :- |
|Axis Title Name|坐标轴标题|Axis Title|
|Axis Unit Name|百,千...|Hundreds, Thousands...|
|Chart Title Name|图表标题|Chart Title|
|Legend Increase Name|增加|Increase|
|Legend Decrease Name|减少|Decrease|
|Legend Total Name|汇总|Total|
|Other Name|其他|Other|
|Series Name|系列|Series|
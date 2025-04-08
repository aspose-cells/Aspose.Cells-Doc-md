---
title: Convert Chart to Image for Japanese Region with Python.NET
linktitle: Set Japanese Region
type: docs
weight: 10
url: /python-net/convert-chart-to-image-for-japanese-region/
alias: [/python-net/set-japanese-configuration-for-chart/]
description: Learn how to configure charts with Japanese regional settings using Aspose.Cells for Python.NET. Set Japanese characters, fonts, text direction and formatting for chart elements.
keywords: Python.NET Excel charts, Japanese chart configuration, Aspose.Cells globalization, chart localization settings, Japanese fonts in charts
---

{{% alert color="primary" %}}

This guide shows how to configure Japanese regional settings for chart elements using Aspose.Cells for Python.NET.

{{% /alert %}}

## **Implementing Custom Globalization Settings**

First, create a class `ChartJapaneseSettings` that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartglobalizationsettings/). Override methods to provide Japanese translations for chart elements:

```python
from aspose.cells.charts import ChartGlobalizationSettings, DisplayUnitType

class ChartJapaneseSetttings(ChartGlobalizationSettings):
    def get_axis_title_name(self) -> str:
        return "軸タイトル"
    
    def get_axis_unit_name(self, type: DisplayUnitType) -> str:
        unit_map = {
            DisplayUnitType.NONE: "",
            DisplayUnitType.HUNDREDS: "百",
            DisplayUnitType.THOUSANDS: "千",
            DisplayUnitType.TEN_THOUSANDS: "万",
            DisplayUnitType.HUNDRED_THOUSANDS: "10万",
            DisplayUnitType.MILLIONS: "百万",
            DisplayUnitType.TEN_MILLIONS: "千万",
            DisplayUnitType.HUNDRED_MILLIONS: "億",
            DisplayUnitType.BILLIONS: "10億",
            DisplayUnitType.TRILLIONS: "兆",
        }
        return unit_map.get(type, "")
    
    def get_chart_title_name(self) -> str:
        return "グラフ タイトル"
    
    def get_legend_decrease_name(self) -> str:
        return "削減"
    
    def get_legend_increase_name(self) -> str:
        return "ぞうか"
    
    def get_legend_total_name(self) -> str:
        return "すべての"
    
    def get_other_name(self) -> str:
        return "その他"
    
    def get_series_name(self) -> str:
        return "シリーズ"
```

## **Applying Japanese Configuration to Charts**

Use the custom settings class when rendering charts to images:

```python
from aspose.cells import Workbook
from aspose.cells.charts import Chart
import clr

clr.AddReference("Aspose.Cells")

# Load workbook and apply Japanese settings
wb = Workbook("Japanese.xls")
wb.settings.globalization_settings.chart_settings = ChartJapaneseSettings()

# Convert chart to image
chart0 = wb.worksheets[0].charts[0]
chart0.to_image("Output.png")
```

This configuration ensures chart elements render with Japanese localization in the output image.

## **Localization Effects**

Without Japanese configuration, chart elements would display in default English. The table below shows localization differences:

| **Chart Element**       | **Japanese Value** | **Default English Value** |
|-------------------------|---------------------|---------------------------|
| Axis Title              | 軸タイトル          | Axis Title                |
| Axis Unit               | 百,千               | Hundreds, Thousands       |
| Chart Title             | グラフ タイトル     | Chart Title               |
| Legend Increase         | ぞうか              | Increase                  |
| Legend Decrease         | 削減                | Decrease                  |
| Legend Total            | すべての            | Total                     |
| Other Category          | その他              | Other                     |
| Series Name             | シリーズ            | Series                    |

{{% alert color="warning" %}} 
Ensure Japanese fonts are installed and properly configured in your environment for accurate rendering.
{{% /alert %}}
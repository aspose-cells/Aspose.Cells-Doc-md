---
title: Customize Globalization Settings for Pivot Table with Python.NET
linktitle: Customize Globalization Settings for Pivot Table
type: docs
weight: 50
url: /python-net/customize-globalization-settings-for-pivot-table/
description: Learn how to customize pivot table labels and totals in multiple languages using Aspose.Cells for Python via .NET API.
---

## **Possible Usage Scenarios**

Sometimes you want to customize the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* text as per your requirements. Aspose.Cells allows you to customize the globalization settings of the pivot table to deal with such scenarios. You can also use this feature to change the labels to other languages like Arabic, Hindi, Polish, etc.

## **Customize Globalization Settings for Pivot Table**

The following sample code explains how to customize globalization settings for the pivot table. It creates a class *CustomPivotTableGlobalizationSettings* derived from a base class [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells.settings/pivotglobalizationsettings/) and overrides all of its necessary methods. These methods return the customized text for the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Then it assigns the object of this class to [**WorkbookSettings.globalization_settings.pivot_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/#pivot_settings) property. The code loads the [source excel file](40468488.xlsx) that contains the pivot table, refreshes and calculate its data and saves it as [output PDF](40468487.pdf) file. The following screenshot shows the effect of the sample code on the output PDF. As you can see in the screenshot, different parts of the pivot table have now a customized text returned by the overridden methods of [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells.settings/pivotglobalizationsettings/) class.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Sample Code**

```python
import os
from aspose.cells import Workbook, PdfSaveOptions
from aspose.cells.settings import PivotGlobalizationSettings
from aspose.cells.pivot import PivotFieldSubtotalType

class CustomPivotTableGlobalizationSettings(PivotGlobalizationSettings):
    def get_text_of_total(self):
        print("---------GetPivotTotalName-------------")
        return "AsposeGetPivotTotalName"

    def get_text_of_grand_total(self):
        print("---------GetPivotGrandTotalName-------------")
        return "AsposeGetPivotGrandTotalName"

    def get_text_of_multiple_items(self):
        print("---------GetMultipleItemsName-------------")
        return "AsposeGetMultipleItemsName"

    def get_text_of_all(self):
        print("---------GetAllName-------------")
        return "AsposeGetAllName"

    def get_text_of_column_labels(self):
        print("---------GetColumnLabelsOfPivotTable-------------")
        return "AsposeGetColumnLabelsOfPivotTable"

    def get_text_of_row_labels(self):
        print("---------GetRowLabelsNameOfPivotTable-------------")
        return "AsposeGetRowLabelsNameOfPivotTable"

    def get_text_of_empty_data(self):
        print("---------GetEmptyDataName-------------")
        return "(blank)AsposeGetEmptyDataName"

    def get_text_of_sub_total(self, sub_total_type):
        print("---------GetSubTotalName-------------")
        if sub_total_type == PivotFieldSubtotalType.SUM:
            return "AsposeSum"
        elif sub_total_type == PivotFieldSubtotalType.COUNT:
            return "AsposeCount"
        elif sub_total_type == PivotFieldSubtotalType.AVERAGE:
            return "AsposeAverage"
        elif sub_total_type == PivotFieldSubtotalType.MAX:
            return "AsposeMax"
        elif sub_total_type == PivotFieldSubtotalType.MIN:
            return "AsposeMin"
        elif sub_total_type == PivotFieldSubtotalType.PRODUCT:
            return "AsposeProduct"
        elif sub_total_type == PivotFieldSubtotalType.COUNT_NUMS:
            return "AsposeCount"
        elif sub_total_type == PivotFieldSubtotalType.STDEV:
            return "AsposeStdDev"
        elif sub_total_type == PivotFieldSubtotalType.STDEVP:
            return "AsposeStdDevp"
        elif sub_total_type == PivotFieldSubtotalType.VAR:
            return "AsposeVar"
        elif sub_total_type == PivotFieldSubtotalType.VARP:
            return "AsposeVarp"
        return "AsposeSubTotalName"

def run():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    
    wb = Workbook(os.path.join(data_dir, "samplePivotTableGlobalizationSettings.xlsx"))
    wb.settings.globalization_settings.pivot_settings = CustomPivotTableGlobalizationSettings()
    
    wb.worksheets[0].is_visible = False
    ws = wb.worksheets[1]
    
    pt = ws.pivot_tables[0]
    pt.refresh_data_flag = True
    pt.refresh_data()
    pt.calculate_data()
    pt.refresh_data_flag = False
    
    options = PdfSaveOptions()
    options.one_page_per_sheet = True
    
    output_path = os.path.join(data_dir, "outputPivotTableGlobalizationSettings.pdf")
    wb.save(output_path, options)
```
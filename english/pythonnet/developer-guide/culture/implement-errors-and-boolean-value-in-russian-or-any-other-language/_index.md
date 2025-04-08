---
title: Implement Errors and Boolean Value in Russian or Any Other Language with Python.NET
linktitle: Implement Errors and Boolean Value
type: docs
weight: 40
url: /python-net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Learn how to display localized error messages and boolean values in Excel files using Aspose.Cells for Python via .NET API.
---

## **Possible Usage Scenarios**

If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve similar behavior using Aspose.Cells by using the [**workbook.settings.globalization_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/#globalization_settings) property. You will need to override the following methods of [**GlobalizationSettings**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/) class:

- [**get_error_value_string()**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/#get_error_value_str)
- [**get_boolean_value_string()**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/#get_boolean_value_str)

## **Implement Errors and Boolean Value in Russian or Any Other Language**

The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the [Sample Excel File](73990159.xlsx) used in this code and its [Output PDF](73990160.pdf). The screenshot shows the difference between Sample Excel File and the Output PDF for reference.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Sample Code**

```python
from aspose.cells import Workbook, GlobalizationSettings

class RussianGlobalization(GlobalizationSettings):
    def get_error_value_string(self, err: str) -> str:
        if err.upper() == "#NAME?":
            return "#RussianName-имя?"
        return "RussianError-ошибка"
    
    def get_boolean_value_string(self, bv: bool) -> str:
        return "RussianTrue-правда" if bv else "RussianFalse-ложный"

def run():
    # Load the source workbook
    wb = Workbook("sampleRussianGlobalization.xlsx")
    
    # Set GlobalizationSettings in Russian Language
    wb.settings.globalization_settings = RussianGlobalization()
    
    # Calculate the formula
    wb.calculate_formula()
    
    # Save the workbook in pdf format
    wb.save("outputRussianGlobalization.pdf")
```
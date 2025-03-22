---
title: Manage settings of Excel spreadsheet files with C++
linktitle: Workbook Settings
type: docs
weight: 185
url: /cpp/workbook-settings/
description: Manage settings of Microsoft Excel files using Aspose.Cells with C++.
---

## **Workbook Settings Overview**

Aspose.Cells provides a comprehensive set of properties and methods to manage the settings of Excel files programmatically. These settings include calculation options, display settings, and other workbook-level configurations.

The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class in Aspose.Cells represents an Excel file and provides access to its settings through the [Settings](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/) property. The [WorkbookSettings](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/) class contains various properties and methods to configure the workbook settings.

## **Managing Calculation Options**

You can control how formulas are calculated in the workbook using the [FormulaSettings](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/) property of the [WorkbookSettings](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/) class. For example, you can enable or disable automatic calculation of formulas.

### **Example: Disabling Automatic Calculation**

The following example demonstrates how to disable automatic calculation in a workbook:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void DisableAutomaticCalculation() {
    // Create a new workbook
    Workbook workbook;

    // Disable automatic calculation
    workbook.GetSettings()->SetFormulaSettings(FormulaSettings::Manual);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **Configuring Display Settings**

You can also configure various display settings for the workbook, such as hiding gridlines, row and column headers, and more.

### **Example: Hiding Gridlines**

The following example demonstrates how to hide gridlines in a workbook:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void HideGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Hide gridlines
    workbook.GetSettings()->SetShowGridlines(false);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **Setting Workbook Properties**

You can set various workbook properties such as the author, title, and subject using the [BuiltInDocumentProperties](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/builtindocumentproperties/) property of the [WorkbookSettings](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/) class.

### **Example: Setting Workbook Properties**

The following example demonstrates how to set the author and title of a workbook:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetWorkbookProperties() {
    // Create a new workbook
    Workbook workbook;

    // Set the author and title
    workbook.GetSettings()->GetBuiltInDocumentProperties()->SetAuthor("John Doe");
    workbook.GetSettings()->GetBuiltInDocumentProperties()->SetTitle("Sample Workbook");

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **Conclusion**

Aspose.Cells for C++ provides a powerful and flexible API to manage the settings of Excel files programmatically. By using the [WorkbookSettings](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/) class, you can configure calculation options, display settings, and other workbook properties to meet your specific requirements.
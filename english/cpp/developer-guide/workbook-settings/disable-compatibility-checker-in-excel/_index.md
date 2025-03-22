---
title: Disable Compatibility Checker in Excel with C++
linktitle: Disable Compatibility Checker
type: docs
weight: 170
url: /cpp/disable-compatibility-checker-in-excel/
description: This article shows how to disable compatibility checker through the Aspose.Cells for C++ API.
keywords: C++ Disable Compatibility Checker, Excel Disable Compatibility Checker in C++, Disable Compatibility Checker in Workbook. 
---

## Disable Compatibility Checker in Excel Worksheets in C++

{{% alert color="primary" %}}

Microsoft Excel's Compatibility Checker flags when saving a file in an earlier file format might cause functionality issues or loss of fidelity. The Compatibility Checker is a feature of Microsoft Office Excel 2007 and Microsoft Excel 2010.

When you save a workbook in a previous version, Excel 97 through Excel 2003, from Excel 2007 or Excel 2010, the Compatibility Checker scans the workbook to see if it contains features that are not supported by the earlier version. To help you make decisions about how to handle compatibility issues, the Compatibility Checker displays dialog boxes with options. It can also be used to create a report on any issues in the workbook, or disable the feature.

Sometimes, you need to disable the Compatibility Checker for a particular spreadsheet. With Aspose.Cells' APIs you can do this programmatically so that users don't get frustrated or confused by the Compatibility Checker dialog box popping up when they re-save the file in Microsoft Excel manually.

{{% /alert %}}

## **How to Disable Compatibility Checker using Microsoft Excel**

To disable the Compatibility Checker in Microsoft Excel (for example Microsoft Excel 2007/2010):

- (Excel 2007) On the Office button, click **Prepare**, then **Run Compatibility Checker**, and then clear the **Check compatibility when you save this workbook** option.
- (Excel 2010) On the File tab, click **Info**, then **Check for issues**, click **Check Compatibility**, and, finally, clear the **Check compatibility when you save this workbook** option.

## **How to Disable Compatibility Checker using Aspose.Cells APIs**

Set the [**Workbook.Settings.CheckCompatibility**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/checkcompatibility/) property to **False** to disable Microsoft Excel's Compatibility Checker.

### **Code Examples**

The code examples that follow show how to disable the Compatibility Checker with Aspose.Cells for C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    
    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
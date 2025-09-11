---
title: Specify Custom Number Decimal and Group Separators for Workbook
linktitle: Specify Custom Number Decimal and Group Separators for Workbook
type: docs
weight: 110
url: /nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Change Number decimal and group separators in Excel using Aspose.Cells for Node.js via C++. 
keywords: specify custom decimal separator excel node.js via C++, specify custom group separator excel node.js via C++, change decimal and group separator excel node.js via C++
---

{{% alert color="primary" %}}

In Microsoft Excel, you can specify the Custom Decimal and Thousands Separators instead of using System Separators from the **Advanced Excel Options** as shown in the screenshot below.

Aspose.Cells provides the [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) and [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) methods to set the custom separators for formatting/parsing numbers.

{{% /alert %}}

## **Specifying Custom Separators using Microsoft Excel**

The following screenshot shows the **Advanced Excel Options** and highlights the section to specify the **Custom Separators**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specifying Custom Separators using Aspose.Cells for Node.js via C++**

The following sample code illustrates how to specify the Custom Separators using Aspose.Cells API. It specifies the Custom Number Decimal and Group Separators as dot and space respectively.

### Node.js code to specify custom Number Decimal and Group Separators

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
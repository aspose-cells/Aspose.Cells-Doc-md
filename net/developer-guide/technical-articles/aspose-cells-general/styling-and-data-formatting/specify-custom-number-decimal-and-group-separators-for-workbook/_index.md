---
title: Specify Custom Number Decimal and Group Separators for Workbook
type: docs
weight: 110
url: /net/specify-custom-number-decimal-and-group-separators-for-workbook/
---

{{% alert color="primary" %}} 

In Microsoft Excel, you can specify the Custom Decimal and Thousands Separators instead of using System Separators from the **Advanced Excel Options** as shown in the screenshot below.

Aspose.Cells provides the [WorkbookSettings.NumberDecimalSeparator](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/numberdecimalseparator) and [WorkbookSettings.NumberGroupSeparator](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/numbergroupseparator) properties to set the custom separators for formatting/parsing numbers.

{{% /alert %}} 
## **Specifying Custom Separators using Microsoft Excel**
The following screenshot shows the **Advanced Excel Options** and highlights the section to specify the **Custom Separators**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)
## **Specifying Custom Separators using Aspose.Cells**
The following sample code illustrates how to specify the Custom Separators using Aspose.Cells API. It specifies the Custom Number Decimal and Group Separators as dot and space respectively.
### **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-StylingAndDataFormatting-CustomDecimalAndGroupSeparator-CustomDecimalAndGroupSeparator.cs" >}}

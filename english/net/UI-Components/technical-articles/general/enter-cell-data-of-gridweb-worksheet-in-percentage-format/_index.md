---
title: Enter Cell Data of GridWeb Worksheet in Percentage Format
type: docs
weight: 80
url: /net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: This article introduce enter cell data with percentage format in GridWeb .
---


## **Possible Usage Scenarios**
GridWeb now supports users to enter cell data in percentage format like 3% and the data in the cell will automatically be formatted as 3.00%. However, you will have to set the cell style to Percentage Format which is either GridTableItemStyle.NumberType a 9 or 10. The number 9 will format 3% as 3% but the number 10 will format 3% as 3.00%.

{{% alert color="primary" %}} 

If you have not set the cell style to Percentage Format, then input data 3% will display as 0.03.

{{% /alert %}} 
## **Enter Cell Data of GridWeb Worksheet in Percentage Format**
The following sample code sets the cell A1 GridTableItemStyle.NumberType as 10, therefore the input data 3% automatically be formatted as 3.00% as shown in the screenshot.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Sample Code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}

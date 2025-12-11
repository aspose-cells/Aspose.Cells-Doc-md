---
title: Enter Cell Data of GridWeb Worksheet in Percentage Format
type: docs
weight: 80
url: /net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: This article introduces how to enter cell data with percentage format in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
GridWeb now supports users in entering cell data in percentage format, such as 3%, and the data in the cell will automatically be formatted as 3.00%. However, you must set the cell style to Percentage Format, which is either GridTableItemStyle.NumberType 9 or 10. Number 9 will format 3% as 3%, while number 10 will format 3% as 3.00%.

{{% alert color="primary" %}} 

If you have not set the cell style to Percentage Format, then the input data 3% will display as 0.03.

{{% /alert %}} 

## **Enter Cell Data of GridWeb Worksheet in Percentage Format**
The following sample code sets the GridTableItemStyle.NumberType of cell A1 to 10; therefore, the input data 3% is automatically formatted as 3.00% as shown in the screenshot.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}

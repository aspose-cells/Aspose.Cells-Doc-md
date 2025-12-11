---
title: Enter Cell Data of GridWeb Worksheet in Percentage Format
type: docs
weight: 1010
url: /java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
GridWeb now supports users in entering cell data in percentage format, such as 3%, and the data in the cell will automatically be formatted as 3.00%. However, you must set the cell style to Percentage Format, which is either `GridTableItemStyle.NumberType` set to 9 or 10. The value 9 will format 3% as 3%, while the value 10 will format 3% as 3.00%.

{{% alert color="primary" %}} 

If you have not set the cell style to Percentage Format, then input data 3% will display as 0.03.

{{% /alert %}} 

## **Enter Cell Data of GridWeb Worksheet in Percentage Format**
The following sample code sets the `GridTableItemStyle.NumberType` of cell A1 to 10; therefore, the input data 3% is automatically formatted as 3.00% as shown in the screenshot.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}

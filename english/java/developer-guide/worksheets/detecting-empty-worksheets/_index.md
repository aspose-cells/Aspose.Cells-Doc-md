---
title: Detecting Empty Worksheets
type: docs
weight: 710
url: /java/detecting-empty-worksheets/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Check for Populated Cells**
Worksheets can have one or more cells populated with values where a value can be simple (text, numeric, date/time) or a formula or a formula based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) or [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) properties. If the aforementioned properties return zero or positive values then that means, one or more cells have been populated, however, if any of these properties return -1, that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}} 

The rows & columns collections have a zero-based index, therefore, a cell at row 0 & column 0 means the first cell in the worksheet, which is A1.

{{% /alert %}} 
## **Check for Empty Initialized Cells**
All cells which have values are automatically initialized, however, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) or [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) properties will return -1 indicating the absence of any populated values but initialized cells due to the cell formatting cannot be detected using this approach. In order to check if a worksheet has empty initialized cells, it is advised to use the *Iterator.hasNext* method on iterator acquired from Cells collection. If the *iterator.hasNext* method returns true then that means there are one or more initialized cells in the given worksheet.

{{% alert color="primary" %}} 

There are a number of ways to acquire the cells enumerator as detailed in [How & Where to use Iterators](/cells/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Check for Shapes**
It is possible that a given worksheet does not have any populated cells, however, it could contain shapes & objects such as controls, charts, images and so on. If we need to check if a worksheet contains any shape, we can do it by inspecting the [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count) property. Any positive value indicates the presence of shape(s) in the worksheet.
## **Programming Sample**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}

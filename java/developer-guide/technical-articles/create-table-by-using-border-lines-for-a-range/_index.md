---
title: Create Table by Using Border Lines for a Range
type: docs
weight: 50
url: /java/create-table-by-using-border-lines-for-a-range/
---

{{% alert color="primary" %}} 

Sometimes, you want to create a table by adding border lines for a **Range**/**CellArea** based on the address of the cells you have. You can use [Cells.createRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) method to create a range of cells. The [Cells.createRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) method returns a [Range](https://apireference.aspose.com/java/cells/com.aspose.cells/Range) object. You can create a [Style](https://apireference.aspose.com/java/cells/com.aspose.cells/Style) object and specify the borders (top, left, bottom, right) options accordingly. Later, you may get the cells of the [Range](https://apireference.aspose.com/java/cells/com.aspose.cells/Range) and apply your desired formatting to the cells. 

{{% /alert %}} 
##### **Example:**
The following example shows how to create a [Range](https://apireference.aspose.com/java/cells/com.aspose.cells/Range) and specify the borderlines for the range cells. 

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}



After running the above code, we can have the generated excel file containing the formatted table; here is the screenshot of the file. 

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
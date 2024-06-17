---
title: 在xlsx4j中检测合并单元格
type: docs
weight: 20
url: /zh/java/detect-merged-cells-in-xlsx4j/
---

## **Aspose.Cells - 检测合并单元格**
在Microsoft Excel中，几个单元格可以合并为一个。这通常用于创建复杂的表格，或者创建一个跨越多个列的标题单元格。
Aspose.Cells允许您识别工作表中的合并单元格区域。您也可以取消合并它们。

**Java**

{{< highlight java >}}

 //Get the merged cells list to put it into the arraylist object

ArrayList<CellArea> al = worksheet.getCells().getMergedCells();

//Define cellarea

CellArea ca;

//Define some variables

int frow, fcol, erow, ecol;

// Print Message

System.out.println("Merged Areas: \n"+ al.toString());

//Loop through the arraylist and get each cellarea to unmerge it

for(int i = al.size()-1 ; i > -1; i--)

{

	ca = new CellArea();

	ca = (CellArea)al.get(i);

	frow = ca.StartRow;

	fcol = ca.StartColumn;

	erow = ca.EndRow;

	ecol = ca.EndColumn;

	System.out.println((i+1) + ". [" + fcol +"," + frow +"] " + "[" + ecol +"," + erow +"]");

	worksheet.getCells().unMerge(frow, fcol, erow, ecol);

}

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

更多详情，请访问[检测工作表中的合并单元格](/cells/zh/java/detect-merged-cells-in-a-worksheet)。

{{% /alert %}}

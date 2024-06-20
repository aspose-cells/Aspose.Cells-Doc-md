---
title: xlsx4jでマージされたセルを検出
type: docs
weight: 20
url: /ja/java/detect-merged-cells-in-xlsx4j/
---

## **Aspose.Cells - マージされたセルを検出**
Microsoft Excelでは、複数のセルを1つにマージすることができます。これは、複雑なテーブルを作成したり、複数の列にまたがる見出しを作成するためによく使用されます。
Aspose.Cellsを使用すると、ワークシート内のマージされたセル領域を識別できます。また、それらをアンマージすることもできます。

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

ワークシートでのマージされたセルの検出についての詳細は、[マージされたセルの検出](/cells/ja/java/detect-merged-cells-in-a-worksheet)をご覧ください。

{{% /alert %}}

---
title: xlsx4jでマージされたCellsを検出
type: docs
weight: 20
url: /ja/java/detect-merged-cells-in-xlsx4j/
---
## **Aspose.Cells - マージされた検出 Cells**
Microsoft Excel では、複数のセルを 1 つに結合できます。これは、複雑なテーブルを作成したり、複数の列にまたがる見出しを保持するセルを作成したりするためによく使用されます。
Aspose.Cells を使用すると、ワークシート内の結合されたセル領域を識別できます。それらをマージ解除することもできます。

**Java**

{{< highlight "java" >}}

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
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークシートでマージされた Cells を検出する](/cells/ja/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}

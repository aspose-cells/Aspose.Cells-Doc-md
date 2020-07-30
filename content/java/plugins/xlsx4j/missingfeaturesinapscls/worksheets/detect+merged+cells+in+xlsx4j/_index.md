---
title : "Detect Merged Cells in xlsx4j" 
description : "" 
weight : 20682 
toc : false
type: docs
url: /java/plugins/xlsx4j/missingfeaturesinapscls/worksheets/detect+merged+cells+in+xlsx4j/
---

# Aspose.Cells for Java : Detect Merged Cells in xlsx4j


## Aspose.Cells - Detect Merged Cells

In Microsoft Excel, several cells can be merged into one. This is often used to create complex tables, or to create a cell that holds a heading that spans several colums.  
Aspose.Cells allows you to identify merged cell areas in a worksheet. You can unmerge them too.

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

For more details, visit [Detect Merged Cells in a Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Detect+Merged+Cells+in+a+Worksheet).


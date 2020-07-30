---
title : "Detect Merged Cells using Aspose.Cells" 
description : "" 
weight : 20638 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/worksheets/detect+merged+cells+using+aspose.cells/
---

# Aspose.Cells for Java : Detect Merged Cells using Aspose.Cells


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

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

For more details, visit [Detect Merged Cells in a Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Detect+Merged+Cells+in+a+Worksheet).


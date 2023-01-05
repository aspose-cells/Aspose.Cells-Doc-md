---
title: Zusammengeführte Cells in xlsx4j erkennen
type: docs
weight: 20
url: /de/java/detect-merged-cells-in-xlsx4j/
---
## **Aspose.Cells - Zusammengeführte Cells erkennen**
In Microsoft Excel können mehrere Zellen zu einer zusammengeführt werden. Dies wird häufig verwendet, um komplexe Tabellen zu erstellen oder um eine Zelle zu erstellen, die eine Überschrift enthält, die sich über mehrere Spalten erstreckt.
Aspose.Cells ermöglicht es Ihnen, verbundene Zellbereiche in einem Arbeitsblatt zu identifizieren. Sie können die Zusammenführung auch aufheben.

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Zusammengeführte Cells in einem Arbeitsblatt erkennen](/cells/de/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}

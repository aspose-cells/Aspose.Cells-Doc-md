---
title: Zusammengeführte Zellen mit Aspose.Cells erkennen
type: docs
weight: 30
url: /de/java/detect-merged-cells-using-aspose-cells/
---

## **Aspose.Cells - Erkennen von zusammengeführten Zellen**
In Microsoft Excel können mehrere Zellen zu einer zusammengeführt werden. Dies wird oft verwendet, um komplexe Tabellen zu erstellen oder um eine Zelle zu erstellen, die über mehrere Spalten hinweg einen Kopf enthält.
Aspose.Cells ermöglicht es Ihnen, zusammengeführte Zellbereiche in einem Arbeitsblatt zu identifizieren. Sie können sie auch wieder aufteilen.

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
## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Zusammengeführte Zellen in einem Arbeitsblatt erkennen](/cells/de/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}

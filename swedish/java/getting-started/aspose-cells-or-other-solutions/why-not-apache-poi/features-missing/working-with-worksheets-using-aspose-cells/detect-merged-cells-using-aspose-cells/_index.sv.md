---
title: Identifiera sammanslagna Cells med Aspose.Cells
type: docs
weight: 30
url: /sv/java/detect-merged-cells-using-aspose-cells/
---
## **Aspose.Cells - Detect Merged Cells**
Microsoft Excel kan flera celler slås samman till en. Detta används ofta för att skapa komplexa tabeller eller för att skapa en cell som innehåller en rubrik som sträcker sig över flera kolumner.
Aspose.Cells låter dig identifiera sammanslagna cellområden i ett kalkylblad. Du kan också ta bort dem.

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
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 För mer information, besök[Identifiera sammanslagna Cells i ett kalkylblad](/cells/sv/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}

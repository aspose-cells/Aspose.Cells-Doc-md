---
title: Identifiera sammanslagna celler i xlsx4j
type: docs
weight: 20
url: /sv/java/detect-merged-cells-in-xlsx4j/
---

## **Aspose.Cells - Identifiera sammanslagna celler**
I Microsoft Excel kan flera celler slås samman till en. Detta används ofta för att skapa komplexa tabeller eller för att skapa en cell som innehåller en rubrik som omfattar flera kolumner.
Aspose.Cells låter dig identifiera områden med sammanslagna celler i ett kalkylblad. Du kan också avslå dem.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

För mer information, besök [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/java/identifiera-sammanslagna-celler-i-ett-kalkylblad).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

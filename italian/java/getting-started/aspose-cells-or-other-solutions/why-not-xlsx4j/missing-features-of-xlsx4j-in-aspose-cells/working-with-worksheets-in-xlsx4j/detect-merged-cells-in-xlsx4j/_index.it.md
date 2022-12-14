---
title: Rileva Cells unito in xlsx4j
type: docs
weight: 20
url: /it/java/detect-merged-cells-in-xlsx4j/
---
## **Aspose.Cells - Rileva unione Cells**
In Microsoft Excel, più celle possono essere unite in una sola. Viene spesso utilizzato per creare tabelle complesse o per creare una cella che contenga un'intestazione che si estende su più colonne.
Aspose.Cells consente di identificare le aree di celle unite in un foglio di lavoro. Puoi separarli anche tu.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Rileva Cells unito in un foglio di lavoro](/cells/it/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}

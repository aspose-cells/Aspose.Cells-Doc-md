---
title: Detectar celdas fusionadas en xlsx4j
type: docs
weight: 20
url: /es/java/detect-merged-cells-in-xlsx4j/
---

## **Aspose.Cells - Detectar celdas fusionadas**
En Microsoft Excel, varias celdas pueden fusionarse en una sola. Esto se usa a menudo para crear tablas complejas, o para crear una celda que contiene un encabezado que abarca varias columnas.
Aspose.Cells te permite identificar áreas de celdas fusionadas en una hoja de cálculo. También puedes deshacer la fusión.

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

Para obtener más detalles, visite [Detectar celdas fusionadas en una hoja de cálculo](/cells/es/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

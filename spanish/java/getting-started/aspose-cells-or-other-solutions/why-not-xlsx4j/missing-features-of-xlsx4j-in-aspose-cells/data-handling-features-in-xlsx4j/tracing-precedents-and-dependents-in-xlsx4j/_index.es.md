---
title: Seguimiento de precedentes y dependientes en xlsx4j
type: docs
weight: 70
url: /es/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Rastreo de precedentes y dependientes**
Las hojas de cálculo financieras complejas, especialmente las desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula usa celdas precedentes y celdas dependientes.

- **Células precedentes**son celdas a las que se hace referencia mediante una fórmula en otro Cell. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es un precedente de la celda D10.
- **células dependientes**contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desee mostrar claramente qué celdas de una hoja de cálculo se utilizan en una fórmula. De manera similar, es posible que desee extraer las celdas dependientes de otras celdas.

Aspose.Cells le permite rastrear celdas y averiguar cuáles están vinculadas.

Rastreando precedentes

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

Seguimiento de dependientes

**Java**

{{< highlight "java" >}}

 //Obtener la celda A1

Cell c = celdas.get("A5");

// Obtenga todos los dependientes de la celda A5

Cell[]dependientes = c.getDependents(true);

para (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Seguimiento de precedentes y dependientes](/java/tracing-precedents-and-dependents).

{{% /alert %}}

---
title: Rastreo de Precedentes y Dependientes en Aspose.Cells
type: docs
weight: 130
url: /es/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente las desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula usa celdas precedentes y celdas dependientes.

- **Células precedentes** son celdas a las que se hace referencia mediante una fórmula en otro Cell. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es un precedente de la celda D10.
- **células dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desee mostrar claramente qué celdas de una hoja de cálculo se utilizan en una fórmula. De manera similar, es posible que desee extraer las celdas dependientes de otras celdas.

Aspose.Cells le permite rastrear celdas y averiguar cuáles están vinculadas.

{{% /alert %}} 
## **Seguimiento de precedentes y dependientes Cells: Microsoft Excel**
Las fórmulas pueden cambiar según las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de que C3 y C4 contengan una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4, u otras celdas, deben cambiar para equilibrar la hoja de cálculo según las reglas comerciales.

De manera similar, suponga que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que deba rastrear la dependencia de una celda en particular con otras celdas. Si las reglas comerciales están incrustadas en fórmulas, nos gustaría averiguar la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas de la hoja de trabajo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear precedentes y dependientes.

1.  Sobre el**Ver barra de herramientas** , Seleccione**Auditoría de fórmulas**.
 Se muestra el cuadro de diálogo Auditoría de fórmulas.
   **El cuadro de diálogo Auditoría de fórmulas** 

![todo:imagen_alternativa_texto](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Rastrear precedentes:
 1. Seleccione la celda que contiene la fórmula para la que desea buscar celdas precedentes.
 1. Para mostrar una flecha de seguimiento a cada celda que proporciona datos directamente a la celda activa, haga clic en**Rastrear precedentes** sobre el**Auditoría de fórmulas** barra de herramientas.
1. Seguimiento de fórmulas que hacen referencia a una celda en particular (dependientes)
 1. Seleccione la celda para la que desea identificar las celdas dependientes.
1. Para mostrar una flecha de rastreo para cada celda que depende de la celda activa, haga clic en Rastrear dependientes en la barra de herramientas Auditoría de fórmulas.
## **Seguimiento de precedentes y dependientes Cells: Aspose.Cells**
### **Rastreando precedentes**
Aspose.Cells facilita la obtención de celdas precedentes. No solo puede recuperar celdas que proporcionan datos a los precedentes de una fórmula simple, sino que también puede encontrar celdas que proporcionan datos a los precedentes de una fórmula compleja con rangos con nombre.

En el siguiente ejemplo, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de cálculo.

**La hoja de cálculo de entrada** 

![todo:imagen_alternativa_texto](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells proporciona el método GetPrecedents de la clase Cell que se usa para rastrear los precedentes de una celda. Devuelve una ReferredAreaCollection. Como puede ver arriba, en Book1.xls, la celda B7 contiene una fórmula "=SUM(A1:A3)". Entonces, las celdas A1:A3 son las celdas precedentes a la celda B7. El siguiente ejemplo demuestra la función de rastreo de precedentes utilizando el archivo de plantilla Book1.xls.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Seguimiento de dependientes**
Aspose.Cells le permite obtener celdas dependientes en hojas de cálculo. Aspose.Cells no solo puede recuperar celdas que brindan datos con respecto a una fórmula simple, sino también encontrar celdas que brindan datos a una fórmula compleja dependiente con rangos con nombre.

Aspose.Cells proporciona el método GetDependents de la clase Cell que se usa para rastrear los dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo muestra cómo realizar un seguimiento de los dependientes de la celda A1 mediante el archivo de plantilla Book1.xlsx.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)


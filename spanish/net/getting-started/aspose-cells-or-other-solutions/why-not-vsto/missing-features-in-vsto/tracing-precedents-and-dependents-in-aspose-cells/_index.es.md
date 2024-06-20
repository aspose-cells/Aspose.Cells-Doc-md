---
title: Trazar precedentes y dependientes en Aspose.Cells
type: docs
weight: 130
url: /es/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente aquellas desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula utiliza celdas precedentes y celdas dependientes.

- **Celdas precedentes** son celdas a las que hace referencia una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es precedente a la celda D10.
- **Las celdas dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 es dependiente de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desees mostrar claramente qué celdas en una hoja de cálculo se utilizan en una fórmula. Del mismo modo, es posible que desees extraer las celdas dependientes de otras celdas.

Aspose.Cells te permite rastrear celdas y averiguar cuáles están vinculadas.

{{% /alert %}} 
## **Rastreo de celdas precedentes y dependientes: Microsoft Excel**
Las fórmulas pueden cambiar según las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de que las celdas C3 y C4 contengan una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4 o otras celdas, deben cambiar para equilibrar la hoja de cálculo según las reglas comerciales.

Del mismo modo, supongamos que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que necesites rastrear la dependencia de una celda en particular hacia otras celdas. Si las reglas comerciales están integradas en las fórmulas, nos gustaría descubrir la dependencia y ejecutar algunas reglas basadas en ella. Del mismo modo, si se modifica el valor de una celda en particular, ¿qué celdas en la hoja de cálculo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear las celdas precedentes y dependientes.

1. En la **Barra de herramientas Ver**, selecciona **Auditoría de fórmulas**.
   Se muestra el cuadro de diálogo de Auditoría de fórmulas. 
   **El cuadro de diálogo de Auditoría de fórmulas** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Rastrear precedentes:
   1. Selecciona la celda que contiene la fórmula de la cual deseas encontrar las celdas precedentes.
   1. Para mostrar una flecha rastreadora a cada celda que proporciona datos directamente a la celda activa, haz clic en **Rastrear precedentes** en la barra de herramientas **Auditoría de fórmulas**.
1. Rastrear fórmulas que hacen referencia a una celda en particular (dependientes)
   1. Selecciona la celda de la que deseas identificar las celdas dependientes.
   1. Para mostrar una flecha rastreadora a cada celda que depende de la celda activa, haz clic en Rastrear dependientes en la barra de herramientas Auditoría de fórmulas.
## **Rastreo de celdas precedentes y dependientes: Aspose.Cells**
### **Rastreo de Precedentes**
Aspose.Cells facilita obtener celdas precedentes. No solo puede recuperar celdas que proporcionan datos a precedentes de fórmulas simples, sino también encontrar celdas que proporcionan datos a precedentes de fórmulas complejas con rangos nombrados.

En el ejemplo a continuación, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de trabajo.

**La hoja de cálculo de entrada** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells proporciona el método GetPrecedents de la clase Cell utilizado para rastrear los precedentes de una celda. Devuelve una ReferredAreaCollection. Como se puede ver arriba, en Book1.xls, la celda B7 contiene la fórmula "=SUM(A1:A3)". Por lo tanto, las celdas A1:A3 son las celdas precedentes de la celda B7. El siguiente ejemplo demuestra la función de rastreo de precedentes utilizando el archivo de plantilla Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **Rastreo de Dependientes**
Aspose.Cells le permite obtener celdas dependientes en las hojas de cálculo. Aspose.Cells no solo puede recuperar celdas que proporcionan datos con respecto a una fórmula simple, sino que también puede encontrar celdas que proporcionan datos a dependientes de fórmulas complejas con rangos nombrados.

Aspose.Cells proporciona el método GetDependents de la clase Cell utilizado para rastrear los dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo demuestra cómo rastrear los dependientes de la celda A1 utilizando el archivo de plantilla Book1.xlsx.

**C#**

{{< highlight csharp >}}

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)


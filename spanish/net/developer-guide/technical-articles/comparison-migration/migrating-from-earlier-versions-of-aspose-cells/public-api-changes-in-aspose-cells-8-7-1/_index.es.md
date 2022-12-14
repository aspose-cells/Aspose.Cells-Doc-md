---
title: Público API Cambios en Aspose.Cells 8.7.1
type: docs
weight: 240
url: /es/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.0 a la 8.7.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Se agregó la propiedad LookInType.OriginalValues**
 Aspose.Cells Las API ya son compatibles con[Buscar o buscar datos](/cells/es/net/find-or-search-data/)función para hojas de cálculo con el fin de encontrar algún contenido particular en el valor de la celda y la fórmula. Sin embargo, a esta función le faltaba el aspecto del formato aplicado a la celda que puede cambiar la apariencia y el valor de los contenidos y, en consecuencia, hacer que el texto no se pueda buscar con el valor original. Con este lanzamiento de las API Aspose.Cells, otra constante con el nombre LookInType.OriginalValues se ha expuesto al público API, lo que permite superar la situación que se mencionó anteriormente.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Buscar datos utilizando valores originales](/cells/es/net/search-data-using-original-values/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Se agregó el evento OnBeforeColumnFilter para GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.1 ha expuesto el evento OnBeforeColumnFilter que sirve como devolución de llamada al mecanismo de filtrado realizado a través de la interfaz de usuario de GridWeb. Como sugiere el nombre, el evento se activa antes de que se aplique el filtrado de columnas y se puede usar para obtener la información de filtrado, como el índice de columna y el valor en el que se debe aplicar el filtro.

El escenario de uso simple se ve de la siguiente manera.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

No olvide registrar el evento en el control GridWeb<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}

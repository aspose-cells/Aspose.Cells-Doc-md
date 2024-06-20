---
title: Cambios en la API pública en Aspose.Cells 8.7.1
type: docs
weight: 240
url: /es/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.7.0 a 8.7.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento en segundo plano en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Propiedad LookInType.OriginalValues agregada**
Las APIs de Aspose.Cells ya admiten la función [Buscar o Buscar Datos](/cells/es/net/find-or-search-data/) para hojas de cálculo con el fin de encontrar un contenido específico en el valor y la fórmula de una celda. Sin embargo, esta función carecía de la capacidad para buscar el formato aplicado a la celda, lo que puede cambiar la apariencia y el valor del contenido, haciendo que el texto original sea no buscable. Con esta versión de las APIs de Aspose.Cells, se ha expuesto otra constante con el nombre LookInType.OriginalValues a la API pública, lo que permite superar la situación mencionada anteriormente.

{{% alert color="primary" %}} 

Para más detalles sobre esta función, consulte el artículo detallado sobre [Buscar Datos Usando Valores Originales](/cells/es/net/search-data-using-original-values/)

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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


### **Agregado evento OnBeforeColumnFilter para GridWeb**
Aspose.Cells.GridWeb para .NET 8.7.1 ha expuesto el evento OnBeforeColumnFilter que sirve como una devolución de llamada para el mecanismo de filtrado realizado a través de la interfaz de usuario de GridWeb. Como su nombre indica, el evento se activa antes de que se aplique el filtrado de columnas y se puede utilizar para obtener información de filtrado como el índice de la columna y el valor en el que se aplicará el filtro.

Un escenario de uso simple se ve como sigue.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}

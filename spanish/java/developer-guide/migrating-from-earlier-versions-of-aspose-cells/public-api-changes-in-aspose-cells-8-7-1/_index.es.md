---
title: Público API Cambios en Aspose.Cells 8.7.1
type: docs
weight: 250
url: /es/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.0 a la 8.7.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Se agregó la propiedad LookInType.ORIGINAL_VALUES**
 Aspose.Cells Las API ya son compatibles con[Buscar o buscar datos](/cells/es/java/find-or-search-data/)función para hojas de cálculo con el fin de encontrar algún contenido particular en el valor de la celda y la fórmula. Sin embargo, a esta función le faltaba el aspecto del formato aplicado a la celda que puede cambiar la apariencia y el valor de los contenidos y, en consecuencia, hacer que el texto no se pueda buscar con el valor original. Con este lanzamiento de las API Aspose.Cells, otra constante con el nombre LookInType.ORIGINAL_VALUES se ha expuesto al público API, lo que permite superar la situación que se mencionó anteriormente.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Buscar datos utilizando valores originales](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}

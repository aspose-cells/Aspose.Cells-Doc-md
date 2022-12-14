---
title: Fusión y desfusión Cells
type: docs
weight: 140
url: /es/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

No siempre desea la misma cantidad de celdas en cada fila o columna. Por ejemplo, es posible que desee colocar un título en una celda que abarque varias columnas. O, si crea una factura, es posible que desee menos columnas para el total. Para crear una celda a partir de dos o más celdas, combínelas. Microsoft Excel permite a los usuarios seleccionar celdas y combinarlas para estructurar la hoja de cálculo de la forma que deseen.

**El resultado de fusionar y luego dividir un rango de celdas formateadas como las celdas a la izquierda en Microsoft Excel** 

![todo:imagen_alternativa_texto](merging-and-unmerging-cells_1.png)

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puede separar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango seleccionado originalmente.

Tenga en cuenta que cuando se combinan celdas, solo se conservan los datos de la celda superior izquierda. Si hay datos en las otras celdas del rango, esos datos se eliminan.

El formato, del mismo modo, se basa en la celda de referencia, de modo que cuando combina celdas, la configuración de formato de la celda superior izquierda en el rango se aplica en la celda combinada. Cuando la celda se divide, las nuevas celdas mantienen su configuración de formato original.

{{% /alert %}}

## **Fusionando Cells en una hoja de trabajo.**

### **Usando Microsoft Excel**

Los siguientes pasos describen cómo combinar celdas en la hoja de trabajo usando Microsoft Excel.

1. Copie los datos que desee en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea fusionar.
1.  Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en**Fusionar y centro** icono en el**Formateo** barra de herramientas.

### **Usando Aspose.Cells**

 los[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) class tiene algunos métodos útiles para la tarea. Por ejemplo, el método[**unir()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) combina las celdas en una sola celda dentro de un rango específico de celdas.

El siguiente resultado se genera después de ejecutar el siguiente código.

**Las celdas (C6:E7) se han fusionado** 

![todo:imagen_alternativa_texto](merging-and-unmerging-cells_2.png)

#### **Ejemplo de código**

El siguiente ejemplo muestra cómo fusionar celdas (C6:E7) en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Dejar de fusionar (Dividir) Fusionado Cells**

### **Usando Microsoft Excel**

Los siguientes pasos describen cómo dividir celdas combinadas usando Microsoft Excel.

1.  Seleccione la celda combinada.
 Cuando las células se han combinado,**Fusionar y centro** se selecciona en el**Formateo** barra de herramientas.
1.  Hacer clic**Fusionar y centro** sobre el**Formateo** barra de herramientas.

#### **Usando Aspose.Cells**

 los[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) la clase tiene un método llamado[**desfusionar()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) que divide las células en su estado original. El método separa las celdas usando la referencia de la celda en el rango de celdas combinadas.

#### **Ejemplo de código**

El siguiente ejemplo muestra cómo dividir las celdas combinadas (C6). El ejemplo usa el archivo creado en el ejemplo anterior y divide las celdas combinadas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Artículos relacionados**

- [Encontrar y dividir celdas combinadas](/cells/es/java/detect-merged-cells-in-a-worksheet/).
- [Combinar y dividir un rango de celdas usando los métodos Range.merge() y Range.unMerge()](/cells/es/java/merge-or-unmerge-range-of-cells/).


---
title: Fusionar y Desfusionar Celdas
type: docs
weight: 140
url: /es/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

No siempre quieres el mismo número de celdas en cada fila o columna. Por ejemplo, es posible que desees poner un título en una celda que abarca varias columnas. O, al crear una factura, es posible que desees menos columnas para el total. Para convertir dos o más celdas en una sola celda, combínelas. Microsoft Excel permite a los usuarios seleccionar celdas y combinarlas para estructurar la hoja de cálculo como deseen.

**El resultado de combinar y luego dividir un rango de celdas formateadas como las celdas a la izquierda en Microsoft Excel** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells es compatible con esta función y también puede combinar celdas en una hoja de cálculo. También puedes descombinar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango originalmente seleccionado.

Ten en cuenta que cuando se combinan celdas, solo se conservan los datos en la celda superior izquierda. Si hay datos en las otras celdas del rango, esos datos se eliminan.

El formato, asimismo, se basa en la celda de referencia para que cuando combines celdas, se apliquen las configuraciones de formato de la celda superior izquierda en el rango. Cuando la celda se divide, las nuevas celdas conservan sus configuraciones de formato originales.

{{% /alert %}}

## **Combinar celdas en una hoja de cálculo.**

### **Usar Microsoft Excel**

Los siguientes pasos describen cómo combinar celdas en la hoja de cálculo usando Microsoft Excel.

1. Copie los datos que desea en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea combinar.
1. Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en el icono **Combinar y centrar** en la barra de herramientas **Formato**.

### **Usar Aspose.Cells**

La clase [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) tiene algunos métodos útiles para la tarea. Por ejemplo, el método [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) combina las celdas en una sola celda dentro de un rango especificado de las celdas.

La siguiente salida se genera después de ejecutar el código a continuación.

**Las celdas (C6:E7) se han combinado** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Ejemplo de Código**

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Descombinar (Separar) celdas combinadas**

### **Usar Microsoft Excel**

Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Seleccione la celda combinada. 
   Cuando las celdas se han combinado, **Combinar y centrar** se selecciona en la barra de herramientas **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.

#### **Usar Aspose.Cells**

La clase [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) tiene un método llamado [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) que divide las celdas en su estado original. El método descombina las celdas utilizando la referencia de la celda en el rango de celdas combinadas.

#### **Ejemplo de Código**

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Artículos relacionados**

- [Encontrar y dividir celdas fusionadas](/cells/es/java/detectar-celdas-fusionadas-en-una-hoja-de-cálculo/).
- [Fusionar y dividir un rango de celdas utilizando los métodos Range.merge() y Range.unMerge()](/cells/es/java/fusionar-o-desagrupar-rango-de-celdas/).


---
title: Fusionar y Desfusionar Celdas
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo, que admite combinar y descombinar celdas. Este artículo presentará cómo combinar y descombinar celdas usando la biblioteca Aspose.Cells, y cómo personalizar el estilo de las celdas combinadas.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, combinar celdas, descombinar celdas, configuración de estilos, estilos personalizados
type: docs
weight: 190
url: /es/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puedes descombinar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango original seleccionado.

{{% /alert %}} 
## **Introducción**
No siempre quieres el mismo número de celdas en cada fila o columna. Por ejemplo, es posible que desees colocar un título en una celda que abarque varias columnas. O, si estás creando una factura, es posible que desees menos columnas para el total. Para hacer una celda a partir de dos o más celdas, combínalas. Microsoft Excel permite a los usuarios seleccionar archivos y combinarlos para estructurar la hoja de cálculo según sus necesidades.

{{% alert color="primary" %}} 

Ten en cuenta que cuando las celdas se combinan, solo se conservan los datos de las celdas superiores izquierdas. Si hay datos en las otras celdas del rango, estos datos se eliminan.
Asimismo, el formato se basa en la celda de referencia, por lo que al combinar celdas, se aplican las configuraciones de formato de la celda superior izquierda en el rango a la celda combinada. Cuando la celda se divide, las nuevas celdas mantienen sus ajustes de formato originales.

{{% /alert %}} 
## **Combina celdas en una hoja de cálculo**
### **Combinar celdas en Microsoft Excel**
Los siguientes pasos describen cómo combinar celdas en la hoja de cálculo utilizando MS Excel.

1. Copie los datos que desea en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea combinar.
1. Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en el icono **Combinar y centrar** en la barra de herramientas **Formato**.
### **Combinar celdas con Aspose.Cells**
La clase Aspose.Cells.Cells tiene algunos métodos útiles para la tarea. Por ejemplo, el método Merge() combina las celdas en una sola celda dentro de un rango especificado.

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Descombinar (Separar) celdas combinadas**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Seleccione la celda combinada.
   Cuando las celdas se han combinado, **Combinar y centrar** se selecciona en la barra de herramientas **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.
### **Usar Aspose.Cells**
La clase Aspose.Cells.Cells tiene un método llamado UnMerge() que separa las celdas a su estado original. El método descombina las celdas utilizando la referencia de la celda en el rango de celdas combinadas.

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Temas avanzados**
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/net/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}

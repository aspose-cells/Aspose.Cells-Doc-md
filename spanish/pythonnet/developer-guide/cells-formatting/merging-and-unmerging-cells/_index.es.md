---
title: Fusionar y Desfusionar Celdas
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo, que soporta fusionar y desfusionar celdas. Este artículo presentará cómo fusionar y desfusionar celdas usando Aspose.Cells para Python via .NET, y cómo personalizar el estilo de la celda fusionada.
keywords: Aspose.Cells para Python via .NET, biblioteca .NET, hoja de cálculo, fusionar celdas, desfusionar celdas, configuración de estilos, estilos personalizados
type: docs
weight: 190
url: /es/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells para Python via .NET soporta esta funcionalidad y también puede fusionar celdas en una hoja. También puedes deshacer la fusión, o dividir, las celdas fusionadas. La referencia de celda de una celda fusionada es la referencia para la celda superior izquierda del rango original.

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

### **Fusión de celdas con Aspose.Cells para Python via .NET**
La clase Aspose.Cells.Cells tiene algunos métodos útiles para la tarea. Por ejemplo, el método Merge() combina las celdas en una sola celda dentro de un rango especificado.

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **Descombinar (Separar) celdas combinadas**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Selecciona la celda fusionada. Cuando las celdas se han combinado, **Fusionar y Centrar** está seleccionado en la barra de herramientas de **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.

### **Usando Aspose.Cells para Python via .NET**
La clase Aspose.Cells.Cells tiene un método llamado UnMerge() que separa las celdas a su estado original. El método descombina las celdas utilizando la referencia de la celda en el rango de celdas combinadas.

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **Temas avanzados**
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/python-net/detect-merged-cells-in-a-worksheet/)


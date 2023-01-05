---
title: Fusión y desfusión Cells
type: docs
weight: 190
url: /es/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puede separar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango seleccionado original.

{{% /alert %}} 
## **Introducción**
No siempre desea la misma cantidad de celdas en cada fila o columna. Por ejemplo, es posible que desee colocar un título en una celda que abarque varias columnas. O, si crea una factura, es posible que desee menos columnas para el total. Para crear una celda a partir de dos o más celdas, combínelas. Microsoft Excel permite a los usuarios seleccionar archivos y fusionarlos para estructurar la hoja de cálculo de la forma que deseen.

{{% alert color="primary" %}} 

Tenga en cuenta que cuando se combinan celdas, solo se conservan los datos de las celdas superiores izquierdas. Si hay datos en las otras celdas del rango, estos datos se eliminan.
Del mismo modo, el formato se basa en la celda de referencia, de modo que cuando combina celdas, la configuración de formato de la celda superior izquierda del rango se aplica a la celda combinada. Cuando la celda se divide, las nuevas celdas mantienen su configuración de formato original.

{{% /alert %}} 
## **Combinar Cells en una hoja de trabajo**
### **Fusionando Cells en Microsoft Excel**
Los siguientes pasos describen cómo combinar celdas en la hoja de trabajo usando MS Excel.

1. Copie los datos que desee en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea fusionar.
1.  Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en**Fusionar y centro** icono en el**Formateo** barra de herramientas.
### **Fusionando Cells con Aspose.Cells**
La clase Aspose.Cells.Cells tiene algunos métodos útiles para la tarea. Por ejemplo, el método Merge() fusiona las celdas en una sola celda dentro de un rango específico.

El siguiente ejemplo muestra cómo fusionar celdas (C6:E7) en una hoja de trabajo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Dejar de fusionar (Dividir) Fusionado Cells**
### **Usando Microsoft Excel**
Los siguientes pasos describen cómo dividir celdas combinadas usando Microsoft Excel.

1. Seleccione la celda combinada.
 Cuando las células se han combinado,**Fusionar y centro** se selecciona en el**Formateo** barra de herramientas.
1.  Hacer clic**Fusionar y centro** sobre el**Formateo** barra de herramientas.
### **Usando Aspose.Cells**
La clase Aspose.Cells.Cells tiene un método llamado UnMerge() que divide las celdas en su estado original. El método separa las celdas usando la referencia de la celda en el rango de celdas combinadas.

El siguiente ejemplo muestra cómo dividir las celdas combinadas (C6). El ejemplo usa el archivo creado en el ejemplo anterior y divide las celdas combinadas.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Temas avanzados**
- [Detectar fusionado Cells en una hoja de trabajo](/cells/es/net/detect-merged-cells-in-a-worksheet/)

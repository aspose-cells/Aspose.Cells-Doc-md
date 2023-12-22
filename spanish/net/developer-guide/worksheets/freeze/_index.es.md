---
title: Congelar paneles de la hoja de cálculo de Excel
linktitle: Congelar paneles
type: docs
weight: 190
url: /es/net/how-to-freeze-panes-of-excel-worksheet
description: En este artículo, aprenderá cómo congelar paneles de hojas de cálculo de Excel mediante programación utilizando la biblioteca C# con .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo congelar paneles.
Cuando tiene una gran cantidad de datos bajo un encabezado común, no puede ver el encabezado cuando se desplaza hacia abajo en la hoja de trabajo. Y cada registro contiene muchos datos. Puede congelar paneles para poder ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puede ver fácilmente los encabezados en las filas superiores o en las primeras columnas. Congelar y descongelar paneles solo cambia la vista de los datos sin cambiar los datos en sí.

{{% /alert %}}

##  **en excel**

**![Congelar paneles en Excel](Freeze-panes.png)**


1. Si desea congelar paneles, congelar filas y columnas, primero seleccione una celda (como B2)
2. Haga clic en Ver > Congelar paneles.
3. En el menú desplegable, haga clic en Congelar paneles.
4. Si se desplaza hacia abajo o hacia la derecha, la primera fila y columna se congelan.

**![Paneles Fonzen](Frozen-Panes.png)**

 Como puede ver, la primera fila y la columna A están congeladas, la segunda fila es 32 y la segunda columna visible es D.

Los paneles congelados le permiten ver datos de gran tamaño sin realizar un seguimiento de la etiqueta de fila o columna.




##  **Congelar paneles con Aspose.Cells para .Net**
 Es sencillo congelar paneles con Aspose.Cells para .Net. Por favor use el[**Hoja de trabajo.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)método para fijar paneles en el Cell seleccionado.
1. Construya un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congele los paneles con el método Worksheet.FreezePanes().
3. Guarde el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Adjunto[archivo Excel fuente de muestra](Freeze.xlsx).

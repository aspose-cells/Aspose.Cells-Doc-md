---
title: Congelar las filas superiores de la hoja de cálculo de Excel
linktitle: Congelar filas
type: docs
weight: 190
url: /es/net/how-to-freeze-rows-of-excel-worksheet
description: En este artículo, aprenderá cómo congelar las filas superiores de hojas de cálculo de Excel mediante programación utilizando la biblioteca C# con .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo congelar las filas superiores.
Cuando tiene una gran cantidad de datos bajo un encabezado común, no puede ver el encabezado cuando se desplaza hacia abajo en la hoja de trabajo. Puede congelar las filas superiores para poder ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puede ver fácilmente los encabezados en las filas superiores.

{{% /alert %}}

##  **Congelar filas en Excel**

**![Congelar fila(s) superior(es) en Excel](Freeze-Rows.png)**


1. Si desea congelar las filas superiores, primero seleccione la fila debajo de la fila que necesita congelarse.
2. Haga clic en Ver > Congelar paneles.
3. En el menú desplegable, haga clic en Congelar fila superior.
4. Si se desplaza hacia abajo, la primera fila siempre está en la vista superior.

**![Fila Fonzen](Frozen-Row.png)**

Como puede ver, la primera fila está congelada, la primera fila siempre permanece en la parte superior de la vista cuando se desplaza hacia abajo.

Freeze Rows le permite ver su gran cantidad de datos sin realizar un seguimiento de la etiqueta de la fila.




##  **Congelar filas con Aspose.Cells para .Net**
 Es sencillo congelar filas con Aspose.Cells para .Net.
 Por favor use el[**Hoja de trabajo.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Método para dividir las filas en la fila seleccionada.
1. Construya un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congele la primera fila con el método Worksheet.FreezePanes().
3. Guarde el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Adjunto[archivo Excel fuente de muestra](../Freeze.xlsx).

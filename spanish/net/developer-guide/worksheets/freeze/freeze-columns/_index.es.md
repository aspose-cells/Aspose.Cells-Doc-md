---
title: Congelar las primeras columnas de la hoja de cálculo de Excel
linktitle: Congelar columnas
type: docs
weight: 190
url: /es/net/how-to-freeze-columns-of-excel-worksheet
description: En este artículo, aprenderá cómo congelar las columnas izquierdas de las hojas de cálculo de Excel mediante programación utilizando la biblioteca C# con .NET API.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo congelar las columnas de la izquierda.
Cuando tiene una gran cantidad de datos en una fila, no puede ver las columnas de la izquierda cuando se desplaza horizontalmente hacia abajo en la hoja de trabajo. Puede congelar y bloquear las primeras columnas para poder ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puede ver fácilmente los encabezados en las columnas de la izquierda.

{{% /alert %}}

##  **Congelar columnas en Excel**

**![Congelar columna(s) izquierda(s) en Excel](freeze-columns.png)**


1. Si desea congelar las columnas de la izquierda, primero seleccione la columna debajo de la columna que necesita congelarse
2. Haga clic en Ver > Congelar paneles.
3. En el menú desplegable, haga clic en Congelar primera columna.
4. Si se desplaza hacia abajo, la primera columna siempre está en la vista izquierda.

**![Columna Fonzen](columnas-congeladas.png)**

Como puede ver, la primera columna está congelada, la primera columna siempre está bloqueada en la parte superior de la vista cuando se desplaza horizontalmente.

Congelar columnas le permite ver sus datos extensos sin realizar un seguimiento de la primera columna.




##  **Congelar columnas con Aspose.Cells para .Net**
Es sencillo congelar las primeras columnas con Aspose.Cells para .Net.
 Por favor use el[**Hoja de trabajo.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)método para dividir la(s) columna(s) en la columna seleccionada.
1. Construya un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congele la primera columna con el método Worksheet.FreezePanes().
3. Guarde el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Adjunto[archivo Excel fuente de muestra](Freeze.xlsx).

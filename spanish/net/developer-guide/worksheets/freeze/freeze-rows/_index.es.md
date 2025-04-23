---
title: Congelar la(s) fila(s) superior(es) de la hoja de cálculo de Excel
linktitle: Congelar Filas
type: docs
weight: 190
url: /es/net/how-to-freeze-rows-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar las filas superiores de las hojas de cálculo de Excel programáticamente utilizando la Biblioteca C# con API .NET.
keywords: Congelar filas superiores, congelar fila superior.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar la(s) fila(s) superior(es). Cuando tienes una gran cantidad de datos bajo un encabezado común, es imposible ver el encabezado al desplazarte hacia abajo en la hoja de cálculo. Puedes congelar la(s) fila(s) superior(es) para poder ver esa porción congelada incluso al desplazarte por el resto de los datos. Podrás ver fácilmente los encabezados en las filas superiores.

## **Congelar Filas en Excel**

**![Congelar fila(s) superior(es) en Excel](Freeze-Rows.png)**


1. Si deseas congelar la(s) fila(s) superior(es), primero selecciona la fila debajo de la fila que necesita ser congelada.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar fila superior.
4. Si te desplazas hacia abajo, la primera fila siempre estará en la vista superior.

**![Fila congelada](Frozen-Row.png)**

Como puedes ver, la 1ra fila está congelada, la primera fila siempre permanece en la parte superior de la vista al desplazarte hacia abajo.

Congelar filas te permite ver tus datos grandes sin necesidad de hacer un seguimiento de las etiquetas de fila.




## **Congelar filas con Aspose.Cells para .Net**
Es fácil congelar fila(s) con Aspose.Cells para .Net. 
Por favor, use el método [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) para congelar fila(s) en la fila seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera fila con el método Worksheet.FreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

Adjunto [archivo de Excel de muestra](../Freeze.xlsx).
{{< app/cells/assistant language="csharp" >}}

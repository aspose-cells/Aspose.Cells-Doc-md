---
title: Congelar la Primera(s) Columna(s) de una Hoja de Cálculo de Excel
linktitle: Congelar Columnas
type: docs
weight: 190
url: /es/net/how-to-freeze-columns-of-excel-worksheet
description: En este artículo, aprenderás a congelar las columnas izquierdas de las Hojas de Cálculo de Excel de forma programática utilizando la Biblioteca C# con API .NET.
keywords: Congelar columnas izquierdas, Congelar primeras columnas, Bloquear la(s) columna(s)
---

## **Introducción**

En este artículo, aprenderemos cómo congelar la(s) columna(s) izquierda(s). Cuando tienes una gran cantidad de datos en una fila, es imposible ver las columnas izquierdas al desplazar horizontalmente la hoja de cálculo. Puedes congelar y bloquear la(s) primera(s) columna(s) para poder ver esa porción congelada incluso al desplazarte por el resto de los datos. Podrás ver fácilmente los encabezados en las columnas izquierdas.


## **Congelar Columnas en Excel**

**![Congelar columnas izquierdas en Excel](freeze-columns.png)**


1. Si deseas congelar la(s) columna(s) izquierda(s), primero selecciona la columna debajo de la que se debe congelar.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar Primera columna.
4. Si te desplazas hacia abajo, la primera columna siempre estará en la vista izquierda.

**![Columna congelada](frozen-columns.png)**

Como se puede ver, la primera columna está congelada, así estará siempre bloqueada en la parte superior de la vista al desplazarte horizontalmente.

Congelar Columnas te permite ver tus datos largos sin necesidad de hacer un seguimiento de la primera columna.




## **Congelar Columnas con Aspose.Cells para .Net**
Es sencillo congelar la(s) primera(s) columna(s) con Aspose.Cells para .Net. 
Por favor, utiliza el método [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) para congelar la(s) columna(s) en la columna seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera columna con el método Worksheet.FreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
{{< app/cells/assistant language="csharp" >}}

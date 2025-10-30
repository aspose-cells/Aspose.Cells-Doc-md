---
title: Congelar la Primera(s) Columna(s) de una Hoja de Cálculo de Excel
linktitle: Congelar Columnas
type: docs
weight: 190
url: /es/python-net/how-to-freeze-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar programáticamente las columnas de la izquierda de las hojas de cálculo de Excel usando las API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Congelar columnas a la izquierda en Python, Congelar primeras columnas en Python, Bloquear columnas en Python.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar la(s) columna(s) izquierda(s). Cuando tienes una gran cantidad de datos en una fila, es imposible ver las columnas izquierdas al desplazar horizontalmente la hoja de cálculo. Puedes congelar y bloquear la(s) primera(s) columna(s) para poder ver esa porción congelada incluso al desplazarte por el resto de los datos. Podrás ver fácilmente los encabezados en las columnas izquierdas.


## **Cómo congelar columnas en Excel**

**![Congelar columnas izquierdas en Excel](freeze-columns.png)**


1. Si deseas congelar la(s) columna(s) izquierda(s), primero selecciona la columna debajo de la que se debe congelar.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar Primera columna.
4. Si te desplazas hacia abajo, la primera columna siempre estará en la vista izquierda.

**![Columna congelada](frozen-columns.png)**

Como se puede ver, la primera columna está congelada, así estará siempre bloqueada en la parte superior de la vista al desplazarte horizontalmente.

Congelar Columnas te permite ver tus datos largos sin necesidad de hacer un seguimiento de la primera columna.




## **Cómo congelar columnas con Aspose.Cells para Python Biblioteca de Excel**
Es fácil congelar la(s) primera(s) columna(s) con Aspose.Cells para Python via .NET. Usa el método [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) para congelar columna(s) en la columna seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera columna con el método Worksheet.FreezePanes().
3. Guarda el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
{{< app/cells/assistant language="python-net" >}}

---
title: Cambiar la ruta absoluta del archivo de datos de origen de enlace externo con Node.js via C++
linktitle: Cambiar la ruta absoluta del archivo de origen de datos de enlace externo
type: docs
weight: 290
url: /es/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Aprende cómo cambiar la ruta absoluta del archivo de origen de datos de enlace externo usando Aspose.Cells for Node.js via C++. 
---

## Posibles Escenarios de Uso

Si deseas cambiar la ruta absoluta del archivo de origen de datos de enlace externo, usa la propiedad [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Inicialmente, esta propiedad estará configurada en la ruta desde donde se cargó el archivo Excel. Pero puedes configurarla como una cadena vacía, o establecerla en alguna carpeta local o ruta de red remota. Cada vez que cambies esta propiedad, también se cambiará la ruta del archivo de fuente del enlace externo.

## Cambiar la Ruta Absoluta del Archivo de Origen de Enlace Externo

El siguiente código de ejemplo carga el [archivo Excel de muestra](5115146.xlsx) que contiene un enlace externo. Primero imprime la fuente de datos del enlace externo, que muestra la ruta remota. Luego elimina la ruta remota y vuelve a imprimir; esta vez, imprime la fuente de datos del enlace externo con la ruta local. Luego cambia la propiedad [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) a una ruta local y remota y vuelve a imprimir la fuente del enlace externo, y los cambios se reflejan en la salida de la consola.

Este es la salida en consola o depuración después de la ejecución del código de ejemplo anterior con el [archivo Excel de muestra](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

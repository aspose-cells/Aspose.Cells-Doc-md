---
title: Cambiar la ruta absoluta de la fuente de datos del enlace externo con C++
linktitle: Cambiar la ruta absoluta del archivo de origen de datos de enlace externo
type: docs
weight: 290
url: /es/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Cambiar la ruta absoluta del archivo fuente del enlace externo en Aspose.Cells con C++.
---

## Posibles Escenarios de Uso

Si deseas cambiar la ruta absoluta del archivo fuente del enlace externo, usa el método [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/). Inicialmente, esta propiedad estará configurada a la ruta desde donde se cargó el archivo de Excel. Pero puedes establecerla a una cadena vacía o a una ruta de carpeta local o a una ruta remota de red. Cada vez que cambies esta propiedad, la ruta del archivo fuente del enlace externo también cambiará.

## Cambiar la Ruta Absoluta del Archivo de Origen de Enlace Externo

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](5115146.xlsx) que contiene un enlace externo. Primero imprime la fuente de datos del enlace externo, mostrando la ruta remota. Luego elimina la ruta remota e imprime nuevamente, esta vez la fuente de datos del enlace externo con la ruta local. Después cambia el método [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) a una ruta local y remota e imprime nuevamente la fuente de datos del enlace externo, reflejando los cambios en la consola.

Aquí está la salida de la consola o depuración después de la ejecución del código de muestra anterior con el [archivo de Excel de muestra](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

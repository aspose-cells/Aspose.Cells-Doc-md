---
title: Cambiar la ruta absoluta del archivo de origen de datos de enlace externo
type: docs
weight: 290
url: /es/net/change-the-absolute-path-of-external-link-data-source-file/
---

## Posibles Escenarios de Uso

Si desea cambiar la ruta absoluta del archivo de origen de enlace externo, utilice la propiedad [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath). Inicialmente, esta propiedad estará configurada con la ruta desde donde se cargó el archivo de Excel. Pero puede configurarla como una cadena vacía o como una ruta de carpeta local o una ruta de red remota. Cada vez que cambie esta propiedad, también se cambiará la ruta del archivo de origen de enlace externo.

## Cambiar la Ruta Absoluta del Archivo de Origen de Enlace Externo

El siguiente código de muestra carga el [archivo de Excel de muestra](5115146.xlsx) que contiene un enlace externo. Primero imprime el origen de datos del enlace externo que imprime la ruta remota. Luego elimina la ruta remota e imprime nuevamente, esta vez, imprime el origen de datos del enlace externo con la ruta local. Luego cambia la propiedad [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) a una ruta local y remota e imprime de nuevo el origen de datos del enlace externo y los cambios se reflejan en la salida de la consola.

Aquí está la salida de la consola o depuración después de la ejecución del código de muestra anterior con el [archivo de Excel de muestra](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

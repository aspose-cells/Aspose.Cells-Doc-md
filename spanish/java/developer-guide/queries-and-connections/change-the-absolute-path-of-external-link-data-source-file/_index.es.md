---
title: Cambiar la ruta absoluta del archivo de origen de datos de enlace externo
type: docs
weight: 1020
url: /es/java/change-the-absolute-path-of-external-link-data-source-file/
---
## **Posibles escenarios de uso**
 Si desea cambiar la ruta absoluta del archivo de fuente de datos del enlace externo, utilice el[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)propiedad. Inicialmente, esta propiedad se establecerá en la ruta desde donde se cargó el archivo de Excel. Pero puede configurarlo en una cadena vacía o puede configurarlo en alguna ruta de carpeta local o ruta de red remota. Cada vez que cambie esta propiedad, también se cambiará la ruta del archivo de origen de datos de enlace externo.
## **Cambiar la ruta absoluta del archivo de origen de datos de enlace externo**
 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](5472589.xlsx) que contiene un enlace externo. Primero imprime la fuente de datos del enlace externo que imprime la ruta remota. Luego elimina la ruta remota e imprime nuevamente, esta vez, imprime la fuente de datos del enlace externo con la ruta local. Luego cambia el[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)property a una ruta local y remota e imprime la fuente de datos del enlace externo nuevamente y los cambios se reflejan en la salida de la consola.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Salida de consola**
Aquí está la consola o la salida de depuración después de la ejecución del código de muestra anterior con el[ejemplo de archivo de Excel](5472589.xlsx).

{{< highlight "java" >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

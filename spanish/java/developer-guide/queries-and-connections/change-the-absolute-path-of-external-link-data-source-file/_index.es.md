---
title: Cambiar la ruta absoluta del archivo de origen de datos de enlace externo
type: docs
weight: 1020
url: /es/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Escenarios de uso posibles**
Si desea cambiar la ruta absoluta del archivo de origen de datos de enlace externo, utilice la propiedad [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath). Inicialmente, esta propiedad se establecerá en la ruta desde la cual se cargó el archivo de Excel. Pero puede establecerla en una cadena vacía o en alguna ruta de carpeta local o remota. Cada vez que cambie esta propiedad, también se cambiará la ruta del archivo de origen de datos de enlace externo.
## **Cambiar la ruta absoluta del archivo de origen de datos de enlace externo**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](5472589.xlsx) que contiene un enlace externo. Primero imprime el origen de datos de enlace externo que imprime la ruta remota. Luego elimina la ruta remota e imprime nuevamente, esta vez imprime el origen de datos de enlace externo con la ruta local. Luego cambia la propiedad [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) a una ruta local y remota e imprime nuevamente el origen de datos de enlace externo y los cambios se reflejan en la salida de la consola.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Salida de la consola**
Aquí está la salida de la consola o depuración después de la ejecución del código de ejemplo anterior con el [archivo de Excel de ejemplo](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

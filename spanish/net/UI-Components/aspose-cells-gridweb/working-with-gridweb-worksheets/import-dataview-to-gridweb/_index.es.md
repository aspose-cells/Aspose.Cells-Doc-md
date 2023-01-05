---
title: Importar DataView a GridWeb
type: docs
weight: 60
url: /es/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Con el lanzamiento del marco Microsoft .NET, se introdujo una nueva forma de almacenar datos. Ahora objetos DataSet, DataTable y DataView que almacenan datos en modo fuera de línea. Estos objetos son muy útiles como repositorios de datos. Usando Aspose.Cells.GridWeb, es posible importar datos desde objetos DataTable o DataView a hojas de trabajo. Aspose.Cells. GridWeb solo admite la importación de datos desde un DataView. pero un objeto DataTable también se puede usar indirectamente. Vamos a discutir esta característica en detalle.

{{% /alert %}} 
## **Importación de datos desde DataView**
Importe datos de un objeto DataView mediante el método ImportDataView de GridWorsheetCollection en el control GridWeb. Pase el objeto DataView del que desea importar datos al método ImportDataView. Es posible especificar encabezados de columna y estilos de datos durante la importación.

{{% alert color="primary" %}} 

Cuando se importan datos de un objeto DataView, se crea una nueva hoja de trabajo para contener los datos importados. La hoja de cálculo tiene el mismo nombre que DataTable.

{{% /alert %}} 

**Salida: datos importados de un DataView a una nueva hoja de cálculo** 

![todo:imagen_alternativa_texto](import-dataview-to-gridweb_1.png)

 Los anchos de las columnas se ajustan para mostrar todos los datos que contienen. Cuando los datos se importan desde DataView, los anchos de columna no se ajustan automáticamente. Los usuarios deben ajustarlos por sí mismos. Para ajustar el ancho de las columnas mediante programación, consulte[Cambiar el tamaño de filas y columnas](/cells/es/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Una versión sobrecargada del método ImportDataView permite a los desarrolladores especificar el nombre de la hoja que contiene los datos importados y un número específico de filas y columnas para importar desde el objeto DataView.

{{% /alert %}}

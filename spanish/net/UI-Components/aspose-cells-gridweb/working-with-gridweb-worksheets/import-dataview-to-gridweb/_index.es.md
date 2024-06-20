---
title: Importar DataView a GridWeb
type: docs
weight: 60
url: /es/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, importar
description: Este artículo introduce cómo importar datos en GridWeb.
---

{{% alert color="primary" %}} 

Con el lanzamiento del Microsoft .NET Framework, se introdujo una nueva forma de almacenar datos. Ahora, los objetos DataSet, DataTable y DataView almacenan datos en modo sin conexión. Estos objetos son muy útiles como repositorios de datos. Usando Aspose.Cells.GridWeb, es posible importar datos desde los objetos DataTable o DataView en hojas de cálculo. Aspose.Cells.GridWeb solo admite la importación de datos desde un objeto DataView, pero un objeto DataTable también se puede utilizar indirectamente. Discutamos esta función en detalle.

{{% /alert %}} 
## **Importar datos desde DataView**
Importar datos desde un objeto DataView usando el método ImportDataView de la colección GridWorsheetCollection en el control GridWeb. Pasa el objeto DataView del cual deseas importar datos al método ImportDataView. Es posible especificar el encabezado de columna y los estilos de datos durante la importación.

{{% alert color="primary" %}} 

Cuando los datos se importan desde un objeto DataView, se crea una nueva hoja de cálculo para contener los datos importados. La hoja de cálculo se nombra igual que el DataTable.

{{% /alert %}} 

**Salida: Datos importados desde un DataView a una nueva hoja de cálculo** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Los anchos de las columnas se ajustan para mostrar todos los datos que contienen. Cuando se importan los datos de un DataView, los anchos de columna no se ajustan automáticamente. Los usuarios necesitan ajustarlos por ellos mismos. Para ajustar los anchos de columna programáticamente, consulta [Redimensionar Filas y Columnas](/cells/es/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Una versión sobrecargada del método ImportDataView permite a los desarrolladores especificar el nombre de la hoja que contiene los datos importados y un número específico de filas y columnas para importar desde el objeto DataView.

{{% /alert %}}

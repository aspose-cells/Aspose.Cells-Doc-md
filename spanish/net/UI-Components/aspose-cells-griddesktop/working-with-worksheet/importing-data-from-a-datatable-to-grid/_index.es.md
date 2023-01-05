---
title: Importación de datos de un DataTable a Grid
type: docs
weight: 50
url: /es/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

Desde el lanzamiento del Framework .NET, Microsoft ha proporcionado una excelente manera de almacenar datos en modo fuera de línea en forma de un objeto DataTable. Comprender las necesidades de los desarrolladores, Aspose.Cells. GridDesktop también admite la importación de datos desde una tabla de datos. En este tema se explica cómo hacerlo.

{{% /alert %}} 
## **Ejemplo**
Para importar el contenido de una tabla de datos usando el control Aspose.Cells.GridDesktop:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Cree un objeto DataTable que contenga los datos que se van a importar.
1. Obtenga la referencia de una hoja de trabajo deseada.
1. Importe el contenido de la tabla de datos a la hoja de trabajo.
1. Establezca los encabezados de columna de la hoja de trabajo de acuerdo con los nombres de columna de la tabla de datos.
1. Establezca el ancho de las columnas, si lo desea/
1. Muestre la hoja de trabajo.

En el ejemplo que se muestra a continuación, hemos creado un objeto DataTable y lo hemos llenado con algunos datos extraídos de una tabla de base de datos denominada Productos. Finalmente, hemos importado datos de ese objeto DataTable a una hoja de trabajo deseada usando Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}

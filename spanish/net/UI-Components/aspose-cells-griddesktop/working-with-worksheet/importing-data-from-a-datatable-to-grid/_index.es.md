---
title: Importar datos de un DataTable a Grid
type: docs
weight: 50
url: /es/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,importar,dato,datatable
description: Este artículo presenta cómo importar datos en GridDesktop.
---

{{% alert color="primary" %}} 

Desde el lanzamiento del Framework .NET, Microsoft ha proporcionado una excelente manera de almacenar datos en modo sin conexión en forma de un objeto DataTable. Entendiendo las necesidades de los desarrolladores, Aspose.Cells.GridDesktop también admite la importación de datos desde una tabla de datos. Este tema discute cómo hacerlo.

{{% /alert %}} 
## **Ejemplo**
Para importar el contenido de un DataTable utilizando el control Aspose.Cells.GridDesktop:

1. Agregar el control Aspose.Cells.GridDesktop a un formulario.
1. Crear un objeto DataTable que contenga los datos a importar.
1. Obtener la referencia de una hoja de cálculo deseada.
1. Importar los contenidos del DataTable a la hoja de cálculo.
1. Establecer los encabezados de columna de la hoja de cálculo según los nombres de las columnas del DataTable.
1. Establecer el ancho de las columnas, si se desea.
1. Mostrar la hoja de cálculo.

En el ejemplo dado a continuación, hemos creado un objeto DataTable y lo hemos llenado con algunos datos obtenidos de una tabla de base de datos llamada Productos. Finalmente, hemos importado los datos de ese objeto DataTable a una hoja de cálculo deseada utilizando Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}

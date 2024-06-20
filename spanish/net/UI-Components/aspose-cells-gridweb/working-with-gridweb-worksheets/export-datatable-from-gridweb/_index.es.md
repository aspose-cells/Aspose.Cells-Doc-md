---
title: Exportar DataTable desde GridWeb
type: docs
weight: 70
url: /es/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, exportar
description: Este artículo presenta cómo exportar un datatable en GridWeb.
---

{{% alert color="primary" %}} 

[Importar DataView a GridWeb](/cells/es/net/aspose-cells-gridweb/import-dataview-to-gridweb/) habla sobre la importación del contenido de un DataView al control Aspose.Cells.GridWeb. Este tema discute la exportación de los datos desde el control Aspose.Cells.GridWeb a un DataTable.

{{% /alert %}} 
## **Exportar datos de hoja de cálculo**
### **A un datatable específico.**
Para exportar los datos de la hoja de cálculo a un objeto DataTable específico:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Crea un objeto DataTable específico.
1. Exporta los datos de las celdas seleccionadas al objeto DataTable especificado.

El ejemplo a continuación crea un objeto DataTable específico con cuatro columnas. Los datos de la hoja de cálculo se exportan comenzando desde la primera celda con todas las filas y columnas visibles en la hoja de cálculo, a un objeto DataTable ya creado.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **A un nuevo objeto DataTable**
A veces, no deseas crear un objeto DataTable, sino simplemente necesitas exportar los datos de la hoja de cálculo a un nuevo objeto DataTable.

El ejemplo a continuación muestra una manera diferente de mostrar el uso del método de exportación. Toma la referencia de la hoja de cálculo activa y exporta los datos completos de esa hoja de cálculo a un nuevo objeto DataTable. El objeto DataTable ahora puede ser utilizado de la manera que desees. Por ejemplo, es posible ligar el objeto DataTable a un GridView para ver los datos.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

---
title: Exportar tabla de datos desde GridWeb
type: docs
weight: 70
url: /es/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[Importar DataView a GridWeb](/cells/es/net/import-dataview-to-gridweb/)habló sobre importar el contenido de un DataView al control Aspose.Cells.GridWeb. Este tema trata sobre la exportación de datos desde el control Aspose.Cells.GridWeb a un DataTable.

{{% /alert %}} 
## **Exportación de datos de la hoja de trabajo**
### **A una tabla de datos específica**
Para exportar datos de la hoja de cálculo a un objeto DataTable específico:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Cree un objeto DataTable específico.
1. Exporte los datos de las celdas seleccionadas al objeto DataTable especificado.

El siguiente ejemplo crea un objeto DataTable específico con cuatro columnas. Los datos de la hoja de cálculo se exportan a partir de la primera celda con todas las filas y columnas visibles en la hoja de cálculo, a un objeto DataTable ya creado.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **A una nueva tabla de datos**
A veces, no desea crear un objeto DataTable sino que simplemente necesita exportar los datos de la hoja de trabajo a un nuevo objeto DataTable.

El siguiente ejemplo intenta una forma diferente de mostrar el uso del método Exportar. Toma la referencia de la hoja de trabajo activa y exporta los datos completos de esa hoja de trabajo a un nuevo objeto DataTable. El objeto DataTable ahora se puede usar de la forma que desee. Por ejemplo, es posible vincular el objeto DataTable a GridView para ver los datos.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

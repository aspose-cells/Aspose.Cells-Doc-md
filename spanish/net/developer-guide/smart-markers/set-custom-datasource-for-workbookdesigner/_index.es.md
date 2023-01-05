---
title: Establecer fuente de datos personalizada para WorkbookDesigner
type: docs
weight: 60
url: /es/net/set-custom-datasource-for-workbookdesigner/
---
Aspose.Cells ofrece la opción de configurar DataSource personalizado para WorkbookDesigner. El API proporciona un método sobrecargado[WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5)que toma el nombre de la fuente como primer parámetro y la instancia de la clase que implementa[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)como segundo parámetro.

El siguiente fragmento de código demuestra el uso de[WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5)método para establecer el origen de datos personalizado.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-1.cs" >}}

La implementación de*CustomerDataSource*, *Cliente*, y*Lista de clientes* las clases se dan a continuación

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}

Los archivos de Excel de origen y salida se adjuntan como referencia.

[Archivo fuente](95584319.xlsx)

[Archivo de salida](95584320.xlsx)

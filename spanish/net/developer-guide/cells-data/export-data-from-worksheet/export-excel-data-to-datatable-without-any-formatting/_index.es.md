---
title: Exportar datos de Excel a un DataTable sin ningún formato
type: docs
weight: 280
url: /es/net/export-excel-data-to-datatable-without-any-formatting/
description: Aprenda a exportar datos de Excel a un DataTable sin ningún formato a través de la API Aspose.Cells for .NET.
keywords: Exportar datos de Excel a un DataTable sin ningún formato, especificar la estrategia de formato del valor de la celda, agregar estrategia de formato al exportar datos a un DataTable. 
---

{{% alert color="primary" %}}

A veces los usuarios quieren exportar datos de Excel a una tabla de datos sin ningún formato. Por ejemplo, si alguna celda tiene un valor de 0.012345 y está formateada para mostrar dos lugares decimales, entonces cuando el usuario exporte datos de Excel a una tabla de datos, se exportará como 0.01 y no como 0.012345. Para resolver este problema, Aspose.Cells ha proporcionado la propiedad [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) que puede tomar uno de estos tres valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Si lo establece en [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), entonces exportará los datos sin ningún formato.

{{% /alert %}}

## Código de Muestra

El siguiente ejemplo explica el uso de la propiedad [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) para exportar datos de Excel con y sin ningún formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Salida de la consola**

A continuación se muestra la salida de depuración de la consola del código de ejemplo anterior

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

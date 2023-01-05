---
title: Exportar datos de Excel a DataTable sin ningún formato
type: docs
weight: 280
url: /es/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

 veces, los usuarios desean exportar datos de Excel a una tabla de datos sin ningún tipo de formato. Por ejemplo, si alguna celda tiene un valor de 0,012345 y está formateada para mostrar dos lugares decimales, cuando el usuario exporte datos de Excel a una tabla de datos, se exportará como 0,01 y no como 0,012345. Para hacer frente a este problema, Aspose.Cells ha proporcionado[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) propiedad que puede tomar uno de estos tres valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.Ninguno

 Si lo configurará en[**CellValueFormatStrategy.Ninguno**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), luego exportará los datos sin ningún formato.

{{% /alert %}}

## Código de muestra

 El siguiente ejemplo explica el uso de[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)propiedad para exportar datos de Excel con y sin formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Salida de consola**

A continuación se muestra la salida de depuración de la consola del código de muestra anterior

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

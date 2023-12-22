---
title: Exportieren Sie Excel-Daten ohne Formatierung in DataTable
type: docs
weight: 280
url: /de/net/export-excel-data-to-datatable-without-any-formatting/
description: Erfahren Sie, wie Sie Excel-Daten ohne Formatierung über Aspose.Cells for .NET API in DataTable exportieren.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

Manchmal möchten Benutzer Excel-Daten ohne Formatierung in eine Datentabelle exportieren. Wenn beispielsweise eine Zelle den Wert 0,012345 hat und so formatiert ist, dass zwei Dezimalstellen angezeigt werden, wird der Benutzer beim Exportieren von Excel-Daten in eine Datentabelle als 0,01 und nicht als 0,012345 exportiert. Um dieses Problem zu lösen, hat Aspose.Cells bereitgestellt[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) Eigenschaft, die einen dieser drei Werte annehmen kann

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Wenn Sie es einstellen möchten[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), dann werden die Daten ohne Formatierung exportiert.

{{% /alert %}}

##  Beispielcode

 Das folgende Beispiel erläutert die Verwendung von[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)Eigenschaft zum Exportieren von Excel-Daten mit und ohne Formatierung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **Konsolenausgabe**

Unten finden Sie die Konsolen-Debug-Ausgabe des obigen Beispielcodes

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

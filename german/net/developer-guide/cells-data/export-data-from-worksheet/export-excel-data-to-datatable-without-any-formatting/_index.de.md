---
title: Exportieren Sie Excel-Daten ohne Formatierung in DataTable
type: docs
weight: 280
url: /de/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

Manchmal möchten Benutzer Excel-Daten ohne Formatierung in eine Datentabelle exportieren. Wenn beispielsweise eine Zelle einen Wert von 0,012345 hat und so formatiert ist, dass zwei Dezimalstellen angezeigt werden, werden Excel-Daten beim Exportieren von Excel-Daten in eine Datentabelle als 0,01 und nicht als 0,012345 exportiert. Um dieses Problem zu lösen, hat Aspose.Cells vorgesehen[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) Eigenschaft, die einen dieser drei Werte annehmen kann

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Wenn Sie es so einstellen[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), dann werden die Daten ohne Formatierung exportiert.

{{% /alert %}}

## Beispielcode

 Das folgende Beispiel erläutert die Verwendung von[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)-Eigenschaft zum Exportieren von Excel-Daten mit und ohne Formatierung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Konsolenausgabe**

Unten ist die Konsolen-Debug-Ausgabe des obigen Beispielcodes

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

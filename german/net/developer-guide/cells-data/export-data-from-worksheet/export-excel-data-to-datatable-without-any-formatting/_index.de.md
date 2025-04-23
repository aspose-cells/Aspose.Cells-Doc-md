---
title: Exportieren von Excel Daten in eine DataTable ohne jegliches Formatieren
type: docs
weight: 280
url: /de/net/export-excel-data-to-datatable-without-any-formatting/
description: Erfahren Sie, wie Sie Excel Daten ohne jegliche Formatierung durch die Aspose.Cells for .NET API in eine DataTable exportieren können.
keywords: Exportieren von Excel Daten in eine DataTable ohne jegliche Formatierung, Festlegen der Zellwertformatstrategie, Hinzufügen der Formatstrategie beim Exportieren von Daten in eine DataTable. 
---

{{% alert color="primary" %}}

Manchmal möchten Benutzer Excel-Daten ohne jegliche Formatierung in eine Daten Tabelle exportieren. Wenn beispielsweise eine Zelle den Wert 0,012345 hat und so formatiert ist, dass sie zwei Dezimalstellen anzeigt, wird beim Exportieren der Excel-Daten in eine Daten Tabelle der Wert als 0,01 und nicht als 0,012345 exportiert. Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) an, die einen von drei Werten annehmen kann.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Wenn Sie es auf [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy) setzen, werden die Daten ohne jegliche Formatierung exportiert.

{{% /alert %}}

## Beispielcode

Das folgende Beispiel erläutert die Verwendung der Eigenschaft [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy), um Excel-Daten mit und ohne jegliche Formatierung zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Konsolenausgabe**

Unten finden Sie die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

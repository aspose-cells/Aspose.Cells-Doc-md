---
title: Exportera Excel data till DataTable och kontrollera blandad datatyp
type: docs
weight: 280
url: /sv/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Lär dig hur man exporterar Excel data till DataTable och kontrollerar blandad datatyp genom Aspose.Cells for .NET API.
keywords: Exportera Excel data till DataTable och kontrollera blandad datatyp, Exportera Arbeitsbokdata till DataTable och kontrollera blandad datatyp, Exportera data till DataTable och kontrollera blandad datatyp, Exportera arbetsbladsdata till DataTable och kontrollera blandad datatyp.
---

## **Möjliga användningsscenario**
Om en kolumn innehåller data av olika typer kommer programmet att kasta ett typfel vid export av data till en DataTable. För att exportera datatabell utvärderar, som standard, Aspose.Cells datatypen för värden baserat på det allra första (cell)värdet i kolumnen. Så om värdet är ett nummer innebär det att kolumnens datatyp skulle vara numerisk, vilket är rimligt. Om det allra första värdet är nummer men det finns alfanumeriska data eller värden i kolumnen bör en strängdatatyp tilldelas. För att hantera detta, använd [ExportDataTable overload](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) som innefattar [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) och försök att ställa in [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Boolean-attribut till "true" om en kolumn har både numeriska och strängvärden för att undvika fel.

## **Exportera Excel-data till DataTable och kontrollera blandad datatyp**

Följande exempel förklarar användningen av [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) egenskap för att exportera excel-data till datatabel. Se det [exempel Excel-filen](sample.xlsx), dess skärmbild och konsoloutput för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Skärmdump**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Konsoloutput**

Nedan är konsoldebugoutput av ovanstående exempelkod

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

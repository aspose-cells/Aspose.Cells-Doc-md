---
title: Exportera Excel-data till DataTable och kontrollera blandad datatyp
type: docs
weight: 280
url: /sv/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Lär dig hur du exporterar Excel-data till datatabell och kontrollerar blandad datatyp via Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Möjliga användningsscenarier**
Om en kolumn innehåller data av olika typer, kommer programmet att skapa ett typundantag när data exporteras till en DataTable. För export av datatabell, som standard, utvärderar Aspose.Cells datatypen för värdena baserat på det allra första (cell) värdet i kolumnen. Så om värdet är nummer betyder det att datatypen för kolumnen skulle vara numerisk, vilket är rimligt. Om det allra första värdet är nummer men det finns alfanumeriska data eller värden i kolumnen, bör en strängdatatyp tilldelas. För att klara av det, använd[ExportDataTable överbelastning](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) vilket involverar[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) och försök ställa in[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Booleskt attribut till "true" om en kolumn har både numeriska och strängvärden för att undvika fel.

##  **Exportera Excel-data till DataTable och kontrollera blandad datatyp**

 Följande exempel förklarar användningen av[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) egenskap för att exportera Excel-data till datatabell. Vänligen se[exempel på Excel-fil](sample.xlsx), dess skärmdump och konsolutgången för en referens.

###  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Skärmdump**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Konsolutgång**

Nedan är konsolens felsökningsutgång för ovanstående exempelkod

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}

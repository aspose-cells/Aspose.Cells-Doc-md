---
title: Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till formatet CSV
type: docs
weight: 100
url: /sv/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylark till CSV-formatet genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Möjliga användningsscenarier**

Ibland har din Excel- eller CSV-fil ledande tomma kolumner eller rader. Tänk till exempel på den här linjen

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de tre första cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, kasserar Microsoft Excel dessa inledande tomma rader och kolumner.

 Som standard kasserar inte Aspose.Cells for Python via .NET inledande tomma kolumner och rader vid sparande, men om du vill ta bort dem precis som Microsoft Excel gör, så ger Aspose.Cells for Python 071633**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** fast egendom. Vänligen ställ in den på**Sann**och sedan kommer alla de tomma raderna och kolumnerna att slängas när du sparar.

{{% alert color="primary" %}}

 Före lanseringen av Aspose.Cells for Python via .NET 20.4 var standardvärdet för**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**var**falsk**. Sedan versionen 20.4 har standardvärdet **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** är**Sann.**

{{% /alert %}}

##  **Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till formatet CSV**

 Följande exempelkod laddar[source excel-fil](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först excel-filen i CSV-format utan några ändringar och sedan ställer den in**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** egendom till**Sann** och sparar den igen. Skärmdumpen visar[source excel-fil](sampleTrimBlankColumns.xlsx), [utgång CSV fil utan trimning](outputWithoutTrimBlankColumns.csv), och den[utgång CSV fil med trimning](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}

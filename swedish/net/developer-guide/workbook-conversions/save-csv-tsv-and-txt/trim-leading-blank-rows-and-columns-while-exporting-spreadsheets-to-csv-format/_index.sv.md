---
title: Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till CSV-format
type: docs
weight: 100
url: /sv/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Möjliga användningsscenarier**

Ibland har din Excel- eller CSV-fil ledande tomma kolumner eller rader. Tänk till exempel på den här linjen

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de tre första cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, kasserar Microsoft Excel dessa tomma rader och kolumner.

 Som standard kasserar Aspose.Cells inte inledande tomma kolumner och rader när du sparar, men om du vill ta bort dem precis som Microsoft Excel gör, ger Aspose.Cells**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** fast egendom. Vänligen ställ in den på**Sann**och sedan kommer alla de tomma raderna och kolumnerna att slängas när du sparar.

{{% alert color="primary" %}}

 Före lanseringen av Aspose.Cells för .NET 20.4 var standardvärdet för**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** var**falsk** . Sedan versionen 20.4 har standardvärdet på**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** är**Sann.**

{{% /alert %}}

## **Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till CSV-format**

 Följande exempelkod laddar[source excel-fil](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först excel-filen i CSV-format utan några ändringar och sedan ställer den in**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** egendom till**Sann** och sparar den igen. Skärmdumpen visar[source excel-fil](sampleTrimBlankColumns.xlsx), [mata ut CSV-fil utan trimning](outputWithoutTrimBlankColumns.csv), och den[ut CSV-fil med trimning](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}

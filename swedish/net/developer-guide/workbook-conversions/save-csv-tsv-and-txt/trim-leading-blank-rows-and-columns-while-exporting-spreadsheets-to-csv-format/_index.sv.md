---
title: Strimla ledande tomma rader och kolumner vid export av kalkylblad till CSV format
type: docs
weight: 100
url: /sv/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Möjliga användningsscenario**

Ibland har din Excel eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg den här raden

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard tar inte Aspose.Cells bort ledande tomma kolumner och rader vid sparandet, men om du vill ta bort dem precis som Microsoft Excel gör, så tillhandahåller Aspose.Cells [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) egenskapen. Ställ in den till **true** och sedan kommer alla ledande tomma rader och kolumner att tas bort vid sparandet.

{{% alert color="primary" %}}

Innan utgivningen av Aspose.Cells for .NET 20.4, var standardvärdet för [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) **false**. Sedan 20.4-utgåvan är standardvärdet för [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) **true.**

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Den följande exempelkoden laddar [käll-excelfilen](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först excelfilen i CSV-format utan ändringar och sedan ställer den in [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)-egenskapen till **true** och sparar den igen. Skärmdumpen visar [käll-excelfilen](sampleTrimBlankColumns.xlsx), [utdata-CSV-filen utan beskärning](outputWithoutTrimBlankColumns.csv) och utdata-CSV-filen med beskärning(outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}

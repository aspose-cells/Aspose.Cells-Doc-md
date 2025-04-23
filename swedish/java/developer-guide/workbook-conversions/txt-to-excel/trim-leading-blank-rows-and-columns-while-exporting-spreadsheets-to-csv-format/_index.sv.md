---
title: Strimla ledande tomma rader och kolumner vid export av kalkylblad till CSV format
type: docs
weight: 50
url: /sv/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Möjliga användningsscenario**

Ibland har din Excel eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg den här raden

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard tar inte Aspose.Cells bort ledande tomma kolumner och rader vid sparandet, men om du vill ta bort dem precis som Microsoft Excel gör, så tillhandahåller Aspose.Cells [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) egenskapen. Ställ in den till **true** och sedan kommer alla ledande tomma rader och kolumner att tas bort vid sparandet.

{{% alert color="primary" %}}

Innan utgivningen av Aspose.Cells for .NET 20.4, var standardvärdet för [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) **false**. Sedan 20.4-utgåvan är standardvärdet för [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) **true.**

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Följande exempelkod laddar den ursprungliga excel-filen som har två ledande tomma kolumner. Först sparar den excel-filen i CSV-formatet utan några ändringar och sedan ställer den in [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)-egenskapen till **true** och sparar den igen. Skärmbilden visar [övergångs excel-filen](sampleTrimBlankColumns.xlsx), [utdata CSV-fil utan strimling](outputWithoutTrimBlankColumns.csv), och [utdata CSV-fil med strimling](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}

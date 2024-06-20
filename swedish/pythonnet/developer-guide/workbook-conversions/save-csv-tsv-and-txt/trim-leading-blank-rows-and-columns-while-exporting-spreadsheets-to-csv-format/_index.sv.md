---
title: Strimla ledande tomma rader och kolumner vid export av kalkylblad till CSV format
type: docs
weight: 100
url: /sv/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Beskär ledande tomma rader och kolumner vid export av kalkylblad till CSV format med Aspose.Cells för Python via .NET API.
keywords: Python Beskär ledande tomma rader och kolumner vid export av kalkylblad till CSV format, Beskär ledande tomma rader och kolumner vid sparande excelfilen till CSV format i Python via NET, Python Beskär ledande tomma rader och kolumner vid export av excelfil till CSV format.
---

## **Möjliga användningsscenario**

Ibland har din Excel eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg den här raden

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard kasserar Aspose.Cells för Python via .NET inte ledande tomma kolumner och rader vid sparning men om du vill ta bort dem precis som Microsoft Excel gör, då tillhandahåller Aspose.Cells för Python via .NET [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)-egenskapen. Vänligen ställ in den till **true** och då kommer alla ledande tomma rader och kolumner att kasseras vid sparandet.

{{% alert color="primary" %}}

Innan utgåvan av Aspose.Cells för Python via .NET 20.4 var standardvärdet för [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) **false**. Sedan utgåvan 20.4 är standardvärdet för [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) **true**.

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Den följande exempelkoden laddar [käll-excelfilen](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först excelfilen i CSV-format utan ändringar och sedan ställer den in [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)-egenskapen till **true** och sparar den igen. Skärmdumpen visar [käll-excelfilen](sampleTrimBlankColumns.xlsx), [utdata-CSV-filen utan beskärning](outputWithoutTrimBlankColumns.csv) och utdata-CSV-filen med beskärning(outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}

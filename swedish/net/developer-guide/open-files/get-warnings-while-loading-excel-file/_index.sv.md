---
title: Få varningar när du laddar Excel-fil
type: docs
weight: 110
url: /sv/net/get-warnings-while-loading-excel-file/
---
## **Möjliga användningsscenarier**

Ibland försöker användaren ladda arbetsboken som är något korrupt men laddningsbar. I sådana fall skickar Aspose.Cells varningar när arbetsboken laddas. Du kan fånga dessa varningar genom att implementera**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** gränssnitt och inställning**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**fast egendom.

## **Få varningar när du laddar Excel-fil**

 Följande exempelkod förklarar hur du får varningar när du laddar excel-fil. Koden laddar[exempel på excel-fil](sampleDuplicateDefinedName.xlsx) som kastar**[DuplicateDefinedName](https://reference.aspose.com/cells/net/aspose.cells/warningtype)** varning vid lastning. Denna varning fångas sedan av**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** metod som skriver ut varningsmeddelanden på konsolen. Koden sparar sedan arbetsboken som[output excel-fil](outputDuplicateDefinedName.xlsx)Om du öppnar exemplet på Excel-filen i Microsoft Excel kommer den också att visa dig denna varning som visas i den här skärmdumpen. Vänligen kontrollera också konsolutgången för koden nedan för mer förståelse.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsolutgång**

 Här är konsolutgången för ovanstående kod när den körs med den medföljande[exempel på excel-fil](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}

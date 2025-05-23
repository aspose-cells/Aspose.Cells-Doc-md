---
title: Få varningar när Excel filen laddas
type: docs
weight: 110
url: /sv/net/get-warnings-while-loading-excel-file/
---

## **Möjliga användningsscenario**

Ibland försöker användaren ladda arbetsboken som är något korrupt men laddningsbar. I sådant fall kastar Aspose.Cells varningar när arbetsboken laddas. Du kan fånga dessa varningar genom att implementera [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) gränssnittet och ställa in [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback) egenskapen.

## **Få varningar vid inläsning av Excel-fil**

Följande exempelkod förklarar hur man får varningar när man laddar excelfil. Koden laddar [exempelfilen](sampleDuplicateDefinedName.xlsx) som kastar [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) varning vid laddning. Denna varning fångas sedan av [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) metoden som skriver ut varningsmeddelandena på konsolen. Koden sparar sedan arbetsboken som [utdata-excel-filen](outputDuplicateDefinedName.xlsx). Om du öppnar exempelfilen i Microsoft Excel kommer den också visa dig denna varning som visas på denna skärmbild. Kolla också konsolens utdata för den här koden nedan för mer förståelse.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsoloutput**

Här är konsolens utdata för ovanstående kod när den körs med den medföljande [exempelfilen](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

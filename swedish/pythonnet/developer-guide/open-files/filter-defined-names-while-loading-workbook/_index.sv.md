---
title: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/python-net/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET tillåter dig att filtrera eller ta bort definierade namn i arbetsboken. Använd [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) för att ladda definierade namn och ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) för att ta bort dem när du laddar arbetsboken. Observera att om du tar bort definierade namn kan formlerna i arbetsboken gå sönder.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempelkod laddar den [exempel-Excel-filen](61767860.xlsx) som innehåller en formel i cell **C1** som innehåller de definierade namnen, dvs. * =SUM(MyName1, MyName2) *. Eftersom vi använder ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) för att ta bort de definierade namnen när arbetsboken laddas, bryts formeln i cell C1 i [utdata Excel-filen](61767861.xlsx) och du ser * #NAME? * istället. Se följande skärmbild som visar effekten av koden på den exempel-Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}

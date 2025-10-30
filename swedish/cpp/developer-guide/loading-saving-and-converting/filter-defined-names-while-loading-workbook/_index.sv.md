---
title: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/cpp/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att filtrera eller ta bort definierade namn som finns i arbetsboken. Använd [**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) för att ladda de definierade namnen och använd ~[**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) för att ta bort dem när du laddar arbetsboken. Observera att om du tar bort definierade namn kan formler inne i arbetsboken brytas.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempelkod laddar den [exempel-Excel-filen](61767860.xlsx) som innehåller en formel i cell **C1** som innehåller de definierade namnen, dvs. * =SUM(MyName1, MyName2) *. Eftersom vi använder ~[**LoadDataFilterOptions::DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) för att ta bort de definierade namnen när arbetsboken laddas, bryts formeln i cell C1 i [utdata Excel-filen](61767861.xlsx) och du ser * #NAME? * istället. Se följande skärmbild som visar effekten av koden på den exempel-Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

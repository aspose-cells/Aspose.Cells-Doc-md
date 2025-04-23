---
title: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/java/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att filtrera eller ta bort definierade namn som finns i arbetsboken. Använd [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) för att ladda de definierade namnen och använd ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) för att ta bort dem när du laddar arbetsboken. Observera att om du tar bort definierade namn kan formler inne i arbetsboken brytas.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempelkod laddar [sample Excel fil](61767873.xlsx) som har en formel i cell C1 som innehåller de definerade namnen det vill säga *=SUM(MyName1, MyName2)*. Eftersom vi använder ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) för att ta bort de definierade namnen vid inläsningen av arbetsboken, bryts formeln i cell C1 i [output Excel fil](61767872.xlsx) upp och du ser *#NAME?* istället. Se följande skärmdump som visar effekten av koden på den exempel Excel filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}

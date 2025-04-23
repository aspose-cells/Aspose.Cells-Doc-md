---
title: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att filtrera eller ta bort definierade namn som finns i arbetsboken. Vänligen använd [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) för att ladda definierade namn vid inläsning av arbetsboken. Observera att om du tar bort definierade namn kan formlerna i arbetsboken gå sönder.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempel kod laddar [exempel-Excel-fil](61767860.xlsx), som har en formel i cell **C1** som innehåller de definierade namnen, dvs. *=SUM(MyName1, MyName2)*. Eftersom vi använder ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) för att ta bort de definierade namnen vid inläsning av arbetsboken, går formeln i cell C1 i [utdata-Excel-filen](61767861.xlsx) sönder och visas istället *#NAME?*. Se följande skärmbild som visar effekten av koden på exempel-Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}

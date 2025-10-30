---
title: Specificera formelfält vid import av data till kalkylblad med Golang via C++
linktitle: Ange formelfält vid import av data till kalkylbladet
type: docs
weight: 300
url: /sv/go-cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Lär dig hur du specificerar formelfält vid import av data till arbetsblad via API n Aspose.Cells for C++.
keywords: Specificera formelfält vid import av data till kalkylblad, Ange formelfält när du lägger till data till kalkylbladet
---

## **Möjliga användningsscenario**

Du kan ange formelfält när du importerar data till ditt kalkylblad med hjälp av [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/go-cpp/importtableoptions/getisformulas/). Denna egenskap tar emot en boolesk array där värdet 'true' betyder att fältet är ett formelfält. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje värdet i arrayen att vara 'true'.

## **Ange formelfält vid import av data till kalkylbladet**

Vänligen se följande exempelkod som förklarar hur man specificerar formelfält vid import av data till ett kalkylblad. Se [utdata Excel-filen](61767838.xlsx) som genereras av koden och skärmdumpen som visar effekten av koden på utdatan från Excel-filen.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyFormulaFieldsWhileImportingDataToWorksheet.go" >}}

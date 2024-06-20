---
title: Ange formelfält vid import av data till kalkylbladet
type: docs
weight: 300
url: /sv/net/specify-formula-fields-while-importing-data-to-worksheet/
description: Lär dig hur du specificerar formelfält vid import av data till kalkylbladet med hjälp av Aspose.Cells for .NET API.
keywords: Specificera formelfält vid import av data till kalkylblad, Ange formelfält när du lägger till data till kalkylbladet
---

## **Möjliga användningsscenario**

Du kan ange formelfält när du importerar data till ditt kalkylblad med hjälp av [**ImportTableOptions.IsFormulas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/isformulas). Denna egenskap tar emot en boolesk array där värdet 'true' betyder att fältet är ett formelfält. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje värdet i arrayen att vara 'true'.

## **Ange formelfält vid import av data till kalkylbladet**

Vänligen se följande exempelkod som förklarar hur man specificerar formelfält vid import av data till ett kalkylblad. Se [utdata Excel-filen](61767838.xlsx) som genereras av koden och skärmdumpen som visar effekten av koden på utdatan från Excel-filen.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.cs" >}}

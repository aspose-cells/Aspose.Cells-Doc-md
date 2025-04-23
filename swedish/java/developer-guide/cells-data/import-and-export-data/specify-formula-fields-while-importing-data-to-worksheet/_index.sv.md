---
title: Ange formelfält vid import av data till kalkylbladet
type: docs
weight: 220
url: /sv/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Möjliga användningsscenario**

Du kan ange formelfält när du importerar data till ditt kalkylark med hjälp av [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas)-metoden. Denna metod tar emot en boolesk array där värdet **true** betyder att fältet är ett formelfält. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje värdet i arrayen att vara **true**.

## **Ange formelfält vid import av data till kalkylbladet**

Vänligen se följande provkod som förklarar hur man specificerar formelfält vid import av data till ett kalkylark. Vänligen se den [utdata Excel-filen](61767850.xlsx) som genererats av koden och skärmbilden som visar effekten av koden på utdata Excel-filen.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}

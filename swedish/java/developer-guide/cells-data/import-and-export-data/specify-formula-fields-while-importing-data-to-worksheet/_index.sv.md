---
title: Ange formelfält när du importerar data till kalkylblad
type: docs
weight: 220
url: /sv/java/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Möjliga användningsscenarier**

 Du kan ange formelfält när du importerar data till ditt kalkylblad med hjälp av[**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas) metod. Denna metod tar den booleska arrayen där värdet**Sann**betyder att fältet är ett formelfält. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje värdet i matrisen att vara**Sann**.

## **Ange formelfält när du importerar data till kalkylblad**

 Se följande exempelkod som förklarar hur du anger formelfältet när du importerar data till ett kalkylblad. Vänligen se[utdata Excel-fil](61767850.xlsx) genereras av koden och skärmdumpen som visar effekten av koden på den utgående Excel-filen.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}

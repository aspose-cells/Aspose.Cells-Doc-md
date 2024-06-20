---
title: Specificera betydande siffror som ska lagras i Excel fil
type: docs
weight: 20
url: /sv/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Möjliga användningsscenario**

Som standard lagrar Aspose.Cells 17 betydande siffror i dubbla värden i kalkylblad jämfört med Excel-applikationen som endast lagrar 15 betydande siffror. Du kan ändra beteendet för detta fall, dvs. du kan ändra antalet betydande siffror från 17 till 15 medan du använder [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) egenskap.

## **Specificera betydande siffror som ska lagras i Excel-fil**

Följande exempelkod tvingar Aspose.Cells att använda 15 betydande siffror medan man lagrar dubbla värden i Excel-filen. Ändra dess förlängning till .zip och packa upp den så ser du, endast 15 betydande siffror lagras i Excel-filen. Följande skärmbild förklarar effekten av [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) egenskapen på utmatningsfilen i Excel.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}

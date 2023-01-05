---
title: Ange betydande siffror som ska lagras i Excel-fil
type: docs
weight: 20
url: /sv/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Möjliga användningsscenarier**

Som standard lagrar Aspose.Cells 17 signifikanta siffror med dubbla värden i kalkylblad till skillnad från Excel-applikationen som endast lagrar 15 signifikanta siffror. Du kan ändra standardbeteendet för Aspose.Cells för det här fallet, det vill säga; du kan ändra antalet signifikanta siffror från 17 till 15 medan du använder[**CellsHelper.Significant Digits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)fast egendom.

## **Ange betydande siffror som ska lagras i Excel-fil**

 Följande exempelkod tvingar Aspose.Cells att använda 15 signifikanta siffror samtidigt som dubbla värden lagras i excel-filen. Vänligen kontrollera[output excel-fil](23166982.xlsx) . Ändra dess tillägg till .zip och packa upp det och du kommer att se att endast 15 signifikanta siffror lagras i excel-filen. Följande skärmdump förklarar effekten av[**CellsHelper.Significant Digits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)egenskap på utdata excel-filen.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}

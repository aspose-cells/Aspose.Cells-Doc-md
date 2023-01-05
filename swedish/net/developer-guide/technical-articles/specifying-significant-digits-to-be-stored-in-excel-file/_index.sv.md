---
title: Ange betydande siffror som ska lagras i Excel-fil
type: docs
weight: 30
url: /sv/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Möjliga användningsscenarier**

Som standard lagrar Aspose.Cells 17 signifikanta siffror med dubbla värden inuti excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra standardbeteendet för Aspose.Cells från 17 signifikanta siffror till 15 signifikanta siffror med hjälp av[**CellsHelper.Significant Digits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)fast egendom.

## **Ange betydande siffror som ska lagras i Excel-fil**

 Följande exempelkod tvingar Aspose.Cells att använda 15 signifikanta siffror samtidigt som dubbla värden lagras i excel-filen. Vänligen kontrollera[output excel-fil](22774105.xlsx) . Ändra dess tillägg till .zip och packa upp det och du kommer att se att endast 15 signifikanta siffror lagras i excel-filen. Följande skärmdump förklarar effekten av[**CellsHelper.Significant Digits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)egenskap på utdata excel-filen.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}

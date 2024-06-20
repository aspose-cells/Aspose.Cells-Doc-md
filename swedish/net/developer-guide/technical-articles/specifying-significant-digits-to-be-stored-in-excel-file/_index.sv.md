---
title: Ange signifikanta siffror som ska lagras i Excel fil
type: docs
weight: 30
url: /sv/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Möjliga användningsscenario**

Som standard lagrar Aspose.Cells 17 signifikanta siffror av dubbla värden i excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra standardbeteendet för Aspose.Cells från 17 signifikanta siffror till 15 signifikanta siffror med hjälp av egenskapen [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **Ange signifikanta siffror som ska lagras i Excel-fil**

Följande kodexempel tvingar Aspose.Cells att använda 15 signifikanta siffror vid lagring av dubbla värden i excel-filen. Ändra dess filändelse till .zip och packa upp den, och du kommer se att endast 15 signifikanta siffror lagras i excel-filen. Följande skärmbild förklarar effekten av [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)-egenskapen på resultatexcel-filen.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}

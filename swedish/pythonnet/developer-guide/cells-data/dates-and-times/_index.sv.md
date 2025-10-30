---
title: Komma åt och hantera datum och tider
type: docs
weight: 600
url: /sv/python-net/how-to-manage-dates-and-times/
description: Lär dig hur man Hanterar datum och tider med Aspose.Cells för Python via .NET API.
keywords: Komma åt och hantera datum och tider, 1900 datumsystemet, 1904 datumsystemet, Ange datum och tider, Hämta datum och tider, Hantera datum och tider, Lagra datum och tider i Excel, Visa datum och tider i celler.
---

## **Hur man lagrar datum och tider i Excel**
Datum och tider lagras i celler som nummer. Därför är värdena i celler som innehåller datum och tider av numerisk typ. Ett nummer som specificerar ett datum och en tid består av datumet (heltalsdelen) och tiden (bråkdelen). Egenskapen Cell.DoubleValue returnerar detta nummer.

## **Hur man visar datum och tider i Aspose.Cells**
För att visa ett nummer som ett datum och tid, tillämpa det obligatoriska datum- och tidsformatet på en cell via egenskapen [Style.number](https://reference.aspose.com/cells/python-net/aspose.cells/style/number/) eller [Style.Custom]() . CellValue.DateTimeValue-egenskapen returnerar DateTime-objektet, som specificerar datum och tid som representeras av numret som finns i en cell.
<br>
<image src="1.png" width="70%" />

## **Hur man växlar mellan två datum system i Aspose.Cells**
MS-Excel lagrar datum som nummer som kallas seriella värden. Ett seriellt värde är ett heltal som är antalet passerade dagar från den första dagen i datum systemet. Excel stöder följande datum system för seriella värden:

1. 1900-datum systemet. Det första datumet är den 1 januari 1900 och dess seriella värde är 1. Det sista datumet är den 31 december 9999 och dess seriella värde är 2 958 465. Detta datum system används som standard i arbetsboken.
1. Det 1904-datasystemet. Det första datumet är 1 januari 1904, och dess serienummer är 0. Det sista datumet är 31 december 9999, och dess serienummer är 2 957 003. För att använda detta datorsystem i arbetsboken, ställ in egenskapen [**Workbook.settings.date1904**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/date1904/) till sant.


Detta exempel visar att de seriella värden som lagras på samma datum i olika datum system är olika.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Datetime-1904.py" >}}
Resultat av utmatning:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Hur man anger datumvärde i Aspose.Cells**
Detta exempel anger ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och nummerformat för A2, och sedan skriver ut värdetyperna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Set-Datetime.py" >}}

Resultat av utmatning:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Hur man får DateTime-värde i Aspose.Cells**
Detta exempel anger ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och nummerformat för A2, kontrollerar värdetyperna för två celler, och sedan skriver ut DateTime-värdet och formaterad sträng.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Get-Datetime.py" >}}

Resultat av utmatning:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="python-net" >}}

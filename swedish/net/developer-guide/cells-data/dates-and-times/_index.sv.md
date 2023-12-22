---
title: Hur man hanterar datum och tider
type: docs
weight: 600
url: /sv/net/how-to-manage-dates-and-times/
description: Lär dig hur du hanterar datum och tider via Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Hur man lagrar datum och tider i Excel**
Datum och tider lagras i celler som siffror. Således är värdena för celler som innehåller datum och tider av numerisk typ. Ett tal som anger ett datum och en tid består av komponenterna datum (heltalsdel) och tid (bråkdel). Egenskapen Cell.DoubleValue returnerar detta nummer.

##  **Så här visar du datum och tider i Aspose.Cells**
För att visa ett nummer som datum och tid, tillämpa det önskade datum- och tidsformatet på en cell via[Stil nummer](https://reference.aspose.com/cells/net/aspose.cells/style/number/) eller[Style.Custom]() fast egendom. Egenskapen CellValue.DateTimeValue returnerar objektet DateTime, som anger datumet och tiden som representeras av talet i en cell.
<br>
<image src="1.png" width="70%" />

##  **Hur man byter två datumsystem i Aspose.Cells**
MS-Excel lagrar datum som siffror som kallas serievärden. Ett seriellt värde är ett heltal som är antalet dagar som förflutit från den första dagen i datumsystemet. Excel stöder följande datumsystem för serievärden:

1. 1900-talets datumsystem. Det första datumet är 1 januari 1900 och dess serievärde är 1. Det sista datumet är 31 december 9999 och dess serievärde är 2 958 465. Detta datumsystem används som standard i arbetsboken.
1.  1904 års datumsystem. Det första datumet är 1 januari 1904 och dess serievärde är 0. Det sista datumet är 31 december 9999 och dess serievärde är 2 957 003. För att använda detta datumsystem i arbetsboken, ställ in[Arbetsbok.Inställningar.Datum 1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) egendom till sann.


Det här exemplet visar att de serievärden som lagras på samma datum i olika datumsystem är olika.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Utgångsresultat:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Så här ställer du in datum och tid i Aspose.Cells**
Det här exemplet ställer in ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och sifferformat för A2 och matar sedan ut värdetyperna.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Utgångsresultat:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Så här får du DateTime-värde i Aspose.Cells**
Det här exemplet ställer in ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och nummerformat för A2, kontrollerar värdetyperna för två celler och matar sedan ut DateTime-värdet och den formaterade strängen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Utgångsresultat:
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

---
title: Konvertera numeriska textdata till nummer
type: docs
weight: 900
url: /sv/net/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar siffror lagrade som text i Excel till siffror genom att använda Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **Möjliga användningsscenarier**
Ibland vill du konvertera numerisk data som skrivits in som text till siffror. Du kan ange siffror som text i Microsoft Excel genom att sätta en apostrof före ett nummer, till exempel *'12345**. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till tal.


##  Hur man konverterar siffror lagrade som text till siffror i Excel
Du kan konvertera nummer lagrade som text till nummer genom att följa några enkla steg.
1. Välj en enskild cell eller cellområde som har en felindikator i det övre vänstra hörnet.
1.  Bredvid den markerade cellen eller cellintervallet klickar du på felknappen som visas. Klicka på Konvertera till nummer på menyn.
<br>
<img src="4.png" width=70% />
1. Om varningsknappen inte är tillgänglig, välj en kolumn med det här problemet. Om du inte vill konvertera hela kolumnen kan du välja en eller flera celler istället. Se bara till att cellerna du väljer är i samma kolumn, annars kommer den här processen inte att fungera. Knappen Text till kolumner används vanligtvis för att dela upp en kolumn, men den kan också användas för att konvertera en enskild textkolumn till siffror. På fliken Data klickar du på Text till kolumner.
<br>
<img src="1.png" width=70% />
1. Klicka på knappen Slutför i popup-rutan.
<br>
<img src="2.png" width=70% />
1. Siffrorna som lagras som text omvandlas till siffror.
<br>
<img src="3.png" width=70% />

## Hur man konverterar nummer lagrade som text till nummer med Aspose.Cells for .NET
Aspose.Cells tillhandahåller[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)metod som kan användas för att konvertera alla numeriska sträng- eller textdata till siffror.

Följande skärmdump visar strängnummer i cellerna *A1:A17**. Strängnummer är justerade till vänster.
<br>
<img src="5.png" width=70% />

 Dessa strängnummer har konverterats till tal med hjälp av[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

##  C# kod för att konvertera sträng numeriska data till faktiska tal

Följande exempelkod illustrerar hur du konverterar alla numeriska strängdata till faktiska tal i alla kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}

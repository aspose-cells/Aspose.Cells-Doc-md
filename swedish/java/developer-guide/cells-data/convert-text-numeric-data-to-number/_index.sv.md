---
title: Konvertera numeriska textdata till nummer
type: docs
weight: 150
url: /sv/java/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar siffror som lagrats som text till siffror genom att använda Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
##  **Möjliga användningsscenarier**
Ibland vill du konvertera numerisk data som skrivits in som text till siffror. Du kan ange siffror som text i Microsoft Excel genom att sätta en apostrof före ett nummer, till exempel *'12345**. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till tal.


## Konvertera siffror som lagras som text till siffror i Excel
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

##  Konvertera nummer lagrade som text till nummer med Aspose.Cells för JAVA
Aspose.Cells for Java API tillhandahåller[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) metod som kan användas för att konvertera alla numeriska sträng- eller textdata till siffror.

Följande skärmdump visar strängnummer i cellerna *A1:A17**. Strängnummer är justerade till vänster.
<br>
<img src="5.png" width=70% />

 Dessa strängnummer har konverterats till tal med hjälp av[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

##  Java kod för att konvertera sträng numeriska data till faktiska tal
Följande exempelkod illustrerar hur du konverterar alla numeriska strängdata till faktiska tal i alla kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}

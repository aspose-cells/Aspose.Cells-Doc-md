---
title: Konvertera numerisk textdata till nummer
type: docs
weight: 150
url: /sv/java/convert-text-numeric-data-to-number/
description: Lär dig hur man konverterar nummer som lagras som text till nummer med hjälp av Aspose.Cells for Java API.
keywords: excel konvertera text till tal, excel konvertera text till tal java, excel konvertera text numeriska data till tal, excel konvertera text numeriska data till tal java, excel konvertera numerisk text till tal, excel konvertera numerisk text till tal java, excel konvertera numerisk text till tal med java, konvertera numerisk text till tal i excel med java, konvertera numerisk text till tal i excel med java, konvertera numerisk sträng till tal i excel med java, excel konvertera text numeriska data till tal java, excel konvertera numerisk sträng till tal java
---

## **Möjliga användningsscenario**
Ibland vill du konvertera numeriska data som matats in som text till nummer. Du kan mata in nummer som text i Microsoft Excel genom att sätta en apostrof före ett nummer, t.ex. ** ' 12345. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till nummer.


## Konvertera siffror lagrade som text till siffror i Excel
Du kan konvertera nummer som lagras som text till nummer genom att följa några enkla steg.
1. Välj en enda cell eller ett cellintervall som har en felindikator i övre vänstra hörnet.
1. Bredvid den valda cellen eller cellintervallet klickar du på felknappen som visas. På menyn klickar du på Konvertera till Nummer. 
<br>
<img src="4.png" width=70% />
1. Om varningsknappen inte är tillgänglig, välj en kolumn med detta problem. Om du inte vill konvertera hela kolumnen kan du istället välja en eller flera celler. Se bara till att cellerna du väljer är i samma kolumn, annars fungerar inte den här processen. Knappen Text till kolumner används vanligtvis för att dela upp en kolumn, men den kan också användas för att konvertera en enda kolumn med text till nummer. På fliken Data, klicka på Text till kolumner.
<br>
<img src="1.png" width=70% />
1. Klicka på Avsluta-knappen i popup-rutan.
<br>
<img src="2.png" width=70% />
1. Siffrorna som är lagrade som text omvandlas till nummer.
<br>
<img src="3.png" width=70% />

## Konvertera siffror lagrade som text till siffror med Aspose.Cells för JAVA
Aspose.Cells for Java API tillhandahåller metoden {0 som kan användas för att konvertera all sträng- eller textnumerisk data till siffror.

Följande skärmdump visar strängnumren i cellerna **A1:A17**. Strängnumren är vänsterjusterade.
<br>
<img src="5.png" width=70% />

Dessa strängnummer har konverterats till nummer med [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

## Java-kod för att konvertera strängnumeriska data till faktiska siffror
Följande kodexempel visar hur du konverterar all strängnumriska data till faktiska nummer i alla arbetsblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: Konvertera numerisk textdata till nummer
type: docs
weight: 900
url: /sv/nodejs-cpp/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar nummer som lagrats som text i Excel till nummer med Aspose.Cells for Node.js via C++ API.
keywords: excel konvertera text till nummer, excel konvertera text till nummer Node js kod, excel konvertera numerisk data till nummer, excel konvertera numerisk data till nummer Node js kod, excel konvertera numerisk text till nummer, excel konvertera numerisk text till nummer Node js kod, excel konvertera numerisk text till nummer med Node js kod, konvertera numerisk text till nummer i excel med Node js kod, konvertera numerisk sträng till nummer i excel med Node js kod, excel konvertera text numerisk data till nummer Node js kod, excel konvertera numerisk sträng till nummer Node js kod
---

## **Möjliga användningsscenario**
Ibland vill du konvertera numerisk data som matats in som text till nummer. Du kan mata in nummer som text i Microsoft Excel genom att lägga ett apostrof framför ett nummer, till exempel **'12345**. Excel behandlar då numret som en sträng. Aspose.Cells for Node.js via C++ låter dig konvertera strängar till nummer.


## Hur man konverterar nummer som lagras som text till nummer i Excel
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

## Hur man konverterar nummer som lagrats som text till nummer med Aspose.Cells for Node.js via C++
Aspose.Cells for Node.js via C++ tillhandahåller metoden [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) som kan användas för att konvertera all sträng- eller textnumerisk data till nummer.

Följande skärmdump visar strängnumren i cellerna **A1:A17**. Strängnumren är vänsterjusterade.
<br>
<img src="5.png" width=70% />

Dessa strängnummer har konverterats till nummer med [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

## Node.js kod för att konvertera strängnumerisk data till faktiska nummer

Följande kodexempel visar hur du konverterar all strängnumriska data till faktiska nummer i alla arbetsblad.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}

---
title: Konvertera numerisk textdata till nummer
type: docs
weight: 900
url: /sv/python-net/convert-text-numeric-data-to-number/
description: Lär dig hur man konverterar nummer lagrade som text i Excel till nummer genom att använda Aspose.Cells for Python via .NET API.
keywords: python excel konvertera text till nummer, python excel konvertera text till nummer, python excel konvertera text numeriska data till nummer, python excel konvertera text numeriska data till nummer, python excel konvertera numerisk text till nummer, python excel konvertera numerisk text till nummer, excel konvertera numerisk text till nummer med python, konvertera numerisk text till nummer i excel med python, konvertera numerisk text till nummer i excel med python, konvertera numerisk sträng till nummer i excel med python excel bibliotek, python excel konvertera text numeriska data till nummer, python excel konvertera numerisk sträng till nummer.
---

## **Möjliga användningsscenario**
Ibland vill du konvertera numeriska data som angetts som text till nummer. Du kan ange nummer som text i Microsoft Excel genom att sätta en apostrof före ett nummer, till exempel **'12345**. Excel behandlar sedan numret som en sträng. Aspose.Cells for Python via .NET tillåter dig att konvertera strängar till nummer.


## **Hur man konverterar nummer lagrade som text till nummer i Excel**
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

## **Hur man konverterar nummer lagrade som text till nummer med hjälp av Aspose.Cells for Python Excel Library**
Aspose.Cells for Python via .NET tillhandahåller metoden [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) som kan användas för att konvertera alla sträng- eller text-numeriska data till nummer.

Följande skärmdump visar strängnumren i cellerna **A1:A17**. Strängnumren är vänsterjusterade.
<br>
<img src="5.png" width=70% />

Dessa strängnummer har konverterats till nummer med [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

## **Python-kod för att konvertera sträng-numeriska data till faktiska nummer**

Följande kodexempel visar hur du konverterar all strängnumriska data till faktiska nummer i alla arbetsblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}

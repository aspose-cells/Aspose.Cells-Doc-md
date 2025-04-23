---
title: Formatera områden
type: docs
weight: 105
url: /sv/net/how-to-format-a-range/
---

## **Möjliga användningsscenario**
När du behöver tillämpa en stil på ett område kan du använda områdesformatering.

## **Hur man formaterar ett område i Excel**

För att formatera ett område med celler i Excel kan du använda de inbyggda formateringsalternativen som tillhandahålls av Excel. Så här kan du formatera en område med celler direkt i Excel:

1. Öppna Excel och öppna arbetsboken som innehåller det område du vill formatera.

2. Välj det område med celler som du vill formatera. Du kan klicka och dra för att markera området, eller så kan du använda tangentbordsgenvägar som Skift + Piltangenter för att utöka markeringen.

3. När området är markerat högerklickar du på det markerade området och väljer "Formatera celler" från snabbmenyn. Alternativt kan du gå till fliken Start i Excel-ribbonen, klicka på rullgardinsmenyn "Format" i gruppen "Celler" och välja "Formatera celler".

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på det markerade området. Till exempel kan du ändra teckensnittsstil, teckenstorlek, teckenfärg, nummerformat, linjer, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. Efter att ha gjort de önskade formateringsändringarna klickar du på "OK"-knappen för att tillämpa formateringen på det markerade området.


## **Hur man formaterar ett område med hjälp av C#**

För att formatera ett område med hjälp av Aspose.Cells kan du använda följande metoder:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


## **Exempelkod**
I det här exemplet skapar vi en Excel-arbetsbok, lägger till en del provdata, får åtkomst till den första arbetsbladet och definierar två intervall("A1:C3" och "A4:C5"). Sedan skapar vi nya stilar, ställer in olika formateringsalternativ (t.ex., teckenfärg, fetstil) och tillämpar stilen på intervallet. Slutligen sparar vi arbetsboken i en ny fil.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
{{< app/cells/assistant language="csharp" >}}

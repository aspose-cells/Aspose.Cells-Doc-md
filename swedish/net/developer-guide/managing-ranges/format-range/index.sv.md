---
title: Formatintervall
type: docs
weight: 105
url: /sv/net/how-to-format-a-range/
---
##  **Möjliga användningsscenarier**
När du behöver tillämpa en stil på ett intervall kan du använda intervallformatering.

##  **Hur man formaterar ett intervall i Excel**

För att formatera en rad celler i Excel kan du använda de inbyggda formateringsalternativen som tillhandahålls av Excel. Så här kan du formatera ett cellintervall direkt i Excel:

1. Öppna Excel och öppna arbetsboken som innehåller intervallet du vill formatera.

2. Välj det cellintervall som du vill formatera. Du kan klicka och dra för att välja intervallet, eller så kan du använda kortkommandon som Skift + Piltangenter för att utöka markeringen.

3. När intervallet är valt högerklickar du på det valda intervallet och väljer "Formatera Cells" från snabbmenyn. Alternativt kan du gå till fliken Hem i Excel-bandet, klicka på rullgardinsmenyn "Format" i gruppen "Cells" och välja "Format Cells".

4. Dialogrutan "Format Cells" visas. Här kan du välja olika formateringsalternativ att tillämpa på det valda intervallet. Du kan till exempel ändra teckensnittsstil, teckenstorlek, teckensnittsfärg, nummerformat, ramar, bakgrundsfärg etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. När du har gjort de önskade formateringsändringarna klickar du på knappen "OK" för att tillämpa formateringen på det valda området.


##  **Hur man formaterar ett intervall med C#**

För att formatera ett intervall med Aspose.Cells kan du använda Du kan använda följande metoder:
1. [Range.ApplyStyle(Style style, StyleFlag flagga)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **Exempelkod**
det här exemplet skapar vi en Excel-arbetsbok, lägger till några exempeldata, kommer åt det första kalkylbladet och definierar två intervall ("A1:C3" och "A4:C5"). Sedan skapar vi nya stilar, ställer in olika formateringsalternativ (t.ex. teckensnittsfärg, fetstil) och tillämpar stilen på intervallet. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}

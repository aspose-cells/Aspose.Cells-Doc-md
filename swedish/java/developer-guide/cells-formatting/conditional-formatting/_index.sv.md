---
title: Villkorlig formatering
type: docs
weight: 120
url: /sv/java/conditional-formatting/
---

{{% alert color="primary" %}} 

Villkorlig formatering är en avancerad funktion i Microsoft Excel som låter dig tillämpa format på en cell eller cellintervall och få den formateringen att ändras beroende på cellens värde eller värdet av en formel. Till exempel kan du få en cell att visas fet när värdet av cellen är större än 500. När värdet på cellen uppfyller villkoret tillämpas det angivna formatet på cellen. Om värdet på cellen inte uppfyller villkoret används standardformateringen. I Microsoft Excel väljer du **Format**, sedan **Villkorlig formatering** för att öppna dialogrutan för villkorlig formatering.

**Villkorlig formatering i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells stödjer tillämpning av villkorlig formatering på celler under körning. Den här artikeln förklarar hur.

{{% /alert %}} 
## **Tillämpa villkorlig formatering**
Aspose.Cells stödjer villkorlig formatering på två sätt:

- [Använda en designerkalkylblad](/cells/sv/java/conditional-formatting/).
- [Skapa villkorlig formatering under körning](/cells/sv/java/conditional-formatting/).
### **Använda designerkalkylblad**
Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylbladet med Aspose.Cells. Aspose.Cells laddar och sparar designerkalkylbladet och behåller alla inställningar för villkorlig formatering. Läs mer om designerkalkylblad i [Vad är ett designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/).
## **Tillämpa villkorlig formatering under körning**
Aspose.Cells stödjer tillämpning av villkorlig formatering under körning.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Ange font**
**Inställning av teckensnitt i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Ange ram**
**Inställning av ramar i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Ange mönster**
**Ange ett cellmönster i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Fortsatta ämnen**
- [Lägg till villkorliga ikoner inställda med celltexten](/cells/sv/java/add-conditional-icons-set-with-the-cell-text/)
- [Lägga till 2-färgskala och 3-färgskala villkorliga formateringar](/cells/sv/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Tillämpa villkorlig formatering i arbetsblad](/cells/sv/java/apply-conditional-formatting-in-worksheets/)
- [Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering](/cells/sv/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)


---
title: Villkorlig formatering
type: docs
weight: 120
url: /sv/java/conditional-formatting/
---
{{% alert color="primary" %}} 

 Villkorlig formatering är en avancerad Microsoft Excel-funktion som låter dig tillämpa format på en cell eller ett cellområde och få den formateringen att ändras beroende på cellens värde eller värdet på en formel. Du kan till exempel bara låta en cell vara fetstil när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller villkoret används standardformateringen. Välj i Microsoft Excel**Formatera** , då**Villkorlig formatering** för att öppna dialogrutan Villkorlig formatering.

**Villkorlig formatering i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells stöder tillämpning av villkorlig formatering på celler under körning. Den här artikeln förklarar hur.

{{% /alert %}} 
## **Använder villkorlig formatering**
Aspose.Cells stöder villkorlig formatering på två sätt:

- [Använda ett designerkalkylblad](/cells/sv/java/conditional-formatting/).
- [Skapar villkorlig formatering vid körning](/cells/sv/java/conditional-formatting/).
### **Använder Designer-kalkylblad**
Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylarket med Aspose.Cells. Aspose.Cells läser in och sparar designerkalkylarket och behåller alla inställningar för villkorlig formatering. För att ta reda på mer om designerkalkylblad, läs[Vad är ett designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/).
## **Använda villkorlig formatering vid körning**
Aspose.Cells stöder tillämpning av villkorlig formatering vid körning.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Ställ in teckensnitt**
**Ställa in teckensnitt i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Ställ in gräns**
**Ställa in gränser i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Ställ in mönster**
**Ställa in ett cellmönster i Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Förhandsämnen**
- [Lägg till villkorliga ikoner med texten Cell](/cells/sv/java/add-conditional-icons-set-with-the-cell-text/)
- [Lägga till villkorlig formatering i 2-färgsskala och 3-färgsskala](/cells/sv/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Använd villkorlig formatering i kalkylblad](/cells/sv/java/apply-conditional-formatting-in-worksheets/)
- [Använd skuggning på alternativa rader och kolumner med villkorlig formatering](/cells/sv/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)


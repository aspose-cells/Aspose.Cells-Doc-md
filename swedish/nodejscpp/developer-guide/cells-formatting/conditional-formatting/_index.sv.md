---  
title: Ställ in villkorlig formatering för Excel och ODS filer
linktitle: Villkorliga format  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/conditional-formatting/  
description: Hur man tillämpar villkorlig formatering på Excel och ODS filer i Node.js via C++.  
keywords: tillämpa villkorsstyrd formatering Node.js via C++  
---  

## **Introduktion**

Villkorsstyrd formatering är en avancerad funktion som tillåter dig att tillämpa format på en cell eller ett cellområde och få formateringen att ändras beroende på cellens värde eller värdet av en formel. Till exempel kan du få en cell att visas i fet stil endast när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller villkoret används cellens standardformat. I Microsoft Excel, välj **Format**, sedan **Villkorsstyrd formatering** för att öppna dialogrutan för villkorsstyrd formatering.

Aspose.Cells stöder tillämpning av villkorlig formatering på celler vid körning. Den här artikeln förklarar hur. Den förklarar också hur man beräknar färgen som Excel använder för färgskala av villkorlig formatering.

## **Tillämpa villkorlig formatering**

Aspose.Cells stöder villkorlig formatering på flera sätt:

- Använda designerkalkylblad
- Använda kopieringsmetoden
- Skapa villkorlig formatering vid körning

### **Använda designerkalkylblad**

Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylbladet med Aspose.Cells. Aspose.Cells laddar och sparar designerkalkylbladet och behåller alla inställningar för villkorlig formatering.

### **Använda kopieringsmetoden**

Aspose.Cells tillåter utvecklare att kopiera inställningar för villkorlig formatering från en cell till en annan i kalkylbladet genom att anropa [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-)-metoden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Tillämpa villkorlig formatering under körning**

Aspose.Cells låter dig både lägga till och ta bort villkorlig formatering vid körning. Kodsamplerna nedan visar hur man ställer in villkorlig formatering:

1. Skapa en arbetsbok.
1. Lägg till en tom villkorlig formatering.
1. Ange det intervall som formateringen ska tillämpas på.
1. Definiera formateringsvillkoren.
1. Spara filen.

Efter det här exemplet följer ett antal mindre exempel som visar hur man tillämpar teckensnittsinställningar, kantlinjeinställningar och mönster.

Microsoft Excel 2007 lade till mer avancerad villkorsstyrd formatering som även Aspose.Cells stöder. Exemplen här visar hur man använder enkel formatering, medan Microsoft Excel 2007-exemplen visar hur man tillämpar mer avancerad villkorsstyrd formatering.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Ange font**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Du kan bara ändra teckensnittsstil, textfärg, understrykningsstil och överstrykningsstil.

{{% /alert %}}

### **Ange ram**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Du kan endast använda tunn linjestil för kantens kontur. Diagonala linjer är inte tillåtna.

{{% /alert %}}

### **Ange mönster**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Fortsatta ämnen**  
- [Lägga till 2-färgskala och 3-färgskala villkorliga formateringar](/cells/sv/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Tillämpa villkorlig formatering i arbetsblad](/cells/sv/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering](/cells/sv/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generera bilder för databarformat i villkorlig formatering](/cells/sv/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Hämta ikonsatser, databarer eller färgskalor som används i villkorlig formatering](/cells/sv/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  



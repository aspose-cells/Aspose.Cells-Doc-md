---
title: Ställa in villkorliga format i Excel och ODS filer.
linktitle: Villkorliga format
type: docs
weight: 60
url: /sv/net/conditional-formatting/
description: Hur man tillämpar villkorliga format på Excel och ODS filer i CSharp.
keywords: tillämpa villkorliga format 
---

## **Introduktion**

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör att du kan tillämpa format på en cell eller en cellintervall och få den formateringen att ändras beroende på cellens värde eller värdet av en formel. Till exempel kan du låta en cell visas fetstilad endast när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering. I Microsoft Excel väljer du **Format**, sedan **Villkorlig formatering** för att öppna dialogrutan för villkorlig formatering.

Aspose.Cells stöder tillämpning av villkorlig formatering på celler vid körning. Den här artikeln förklarar hur. Den förklarar också hur man beräknar färgen som Excel använder för färgskala av villkorlig formatering.

## **Tillämpa villkorlig formatering**

Aspose.Cells stöder villkorlig formatering på flera sätt:

- Använda designerkalkylblad
- Använda kopieringsmetoden
- Skapa villkorlig formatering vid körning

### **Använda designerkalkylblad**

Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylbladet med Aspose.Cells. Aspose.Cells laddar och sparar designerkalkylbladet och behåller alla inställningar för villkorlig formatering.

### **Använda kopieringsmetoden**

Aspose.Cells tillåter utvecklare att kopiera inställningar för villkorlig formatering från en cell till en annan i kalkylbladet genom att anropa [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)-metoden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Tillämpa villkorlig formatering under körning**

Aspose.Cells låter dig både lägga till och ta bort villkorlig formatering vid körning. Kodsamplerna nedan visar hur man ställer in villkorlig formatering:

1. Skapa en arbetsbok.
1. Lägg till en tom villkorlig formatering.
1. Ange det intervall som formateringen ska tillämpas på.
1. Definiera formateringsvillkoren.
1. Spara filen.

Efter det här exemplet följer ett antal mindre exempel som visar hur man tillämpar teckensnittsinställningar, kantlinjeinställningar och mönster.

Microsoft Excel 2007 lade till mer avancerad villkorlig formatering som även stöds av Aspose.Cells. Exemplen här illustrerar hur man använder enkel formatering, och Microsoft Excel 2007-exemplen visar hur man tillämpar mer avancerad villkorlig formatering.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Ange font**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Du kan bara ändra teckensnittsstil, textfärg, understrykningsstil och överstrykningsstil.

{{% /alert %}}

### **Ange ram**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Du kan bara använda tunna linjestilar till ytterkanten. Diagonala linjer är inte tillåtna.

{{% /alert %}}

### **Ange mönster**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Fortsatta ämnen**
- [Lägga till 2-färgskala och 3-färgskala villkorliga formateringar](/cells/sv/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Tillämpa avancerad villkorlig formatering](/cells/sv/net/apply-advanced-conditional-formatting/)
- [Tillämpa villkorlig formatering i arbetsblad](/cells/sv/net/apply-conditional-formatting-in-worksheets/)
- [Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering](/cells/sv/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generera bilder för databarformat i villkorlig formatering](/cells/sv/net/generate-conditional-formatting-databars-images/)
- [Hämta ikonsatser, databarer eller färgskalor som används i villkorlig formatering](/cells/sv/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)


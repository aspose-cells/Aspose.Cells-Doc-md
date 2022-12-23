---
title: Ställ in villkorliga format för Excel- och ODS-filer.
linktitle: Villkorliga format
type: docs
weight: 60
url: /sv/net/conditional-formatting/
description: Hur man tillämpar villkorliga format på Excel- och ODS-filer i CSharp.
keywords: apply conditional formats 
---
## **Introduktion**

 Villkorlig formatering är en avancerad Microsoft Excel-funktion som låter dig tillämpa format på en cell eller ett cellområde och få den formateringen att ändras beroende på cellens värde eller värdet på en formel. Du kan till exempel bara låta en cell vara fetstil när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering. Välj i Microsoft Excel**Formatera** , då**Villkorlig formatering** för att öppna dialogrutan Villkorlig formatering.

Aspose.Cells stöder tillämpning av villkorlig formatering på celler under körning. Den här artikeln förklarar hur. Den förklarar också hur man beräknar färgen som används av Excel för villkorlig formatering av färgskala.

## **Använder villkorlig formatering**

Aspose.Cells stöder villkorlig formatering på flera sätt:

- Använder designerkalkylblad
- Använder kopieringsmetoden.
- Skapar villkorlig formatering vid körning.

### **Använder Designer-kalkylblad**

Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylarket med Aspose.Cells. Aspose.Cells läser in och sparar designerkalkylarket och behåller alla inställningar för villkorlig formatering.

### **Använda kopieringsmetoden**

 Aspose.Cells tillåter utvecklare att kopiera villkorliga formatinställningar från en cell till en annan i kalkylbladet genom att anropa[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Använda villkorlig formatering vid körning**

Aspose.Cells låter dig både lägga till och ta bort villkorlig formatering under körning. Kodexemplen nedan visar hur du ställer in villkorlig formatering:

1. Instantiera en arbetsbok.
1. Lägg till ett tomt villkorligt format.
1. Ställ in intervallet som formateringen ska gälla för.
1. Definiera formateringsvillkoren.
1. Spara filen.

Efter det här exemplet kommer ett antal andra mindre exempel som visar hur man använder teckensnittsinställningar, raminställningar och mönster.

Microsoft Excel 2007 lade till mer avancerad villkorlig formatering som Aspose.Cells också stöder. Exemplen här illustrerar hur man använder enkel formatering, exemplen Microsoft Excel 2007 visar hur man tillämpar mer avancerad villkorlig formatering.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Ställ in teckensnitt**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Du kan bara ändra teckensnittsstil, textfärg, understruken stil och genomstruken stil.

{{% /alert %}}

### **Ställ in gräns**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Du kan bara använda tunna linjestilar till konturkanten. Diagonala linjer är inte tillåtna.

{{% /alert %}}

### **Ställ in mönster**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Förhandsämnen**
- [Lägga till villkorlig formatering i 2-färgsskala och 3-färgsskala](/cells/sv/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Använd avancerad villkorlig formatering](/cells/sv/net/apply-advanced-conditional-formatting/)
- [Använd villkorlig formatering i kalkylblad](/cells/sv/net/apply-conditional-formatting-in-worksheets/)
- [Använd skuggning på alternativa rader och kolumner med villkorlig formatering](/cells/sv/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generera villkorlig formatering DataBars-bilder](/cells/sv/net/generate-conditional-formatting-databars-images/)
- [Få ikonuppsättningar, datafält eller färgskalaobjekt som används i villkorlig formatering](/cells/sv/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)


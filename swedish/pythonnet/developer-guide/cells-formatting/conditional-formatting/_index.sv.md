---
title: Ställa in villkorliga format i Excel och ODS filer.
linktitle: Villkorliga format
type: docs
weight: 60
url: /sv/python-net/conditional-formatting/
description: Hur man tillämpar villkorlig formatering på Excel och ODS filer i Python.
keywords: tillämpa villkorliga format 
---

## **Introduktion**

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör att du kan tillämpa format på en cell eller en cellintervall och få den formateringen att ändras beroende på cellens värde eller värdet av en formel. Till exempel kan du låta en cell visas fetstilad endast när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering. I Microsoft Excel väljer du **Format**, sedan **Villkorlig formatering** för att öppna dialogrutan för villkorlig formatering.

 Aspose.Cells för Python via .NET stödjer att tillämpa villkorlig formatering på celler vid körning. Denna artikel förklarar hur. Den förklarar också hur man beräknar vilken färg Excel använder för färgskala villkorlig formatering.

## **Tillämpa villkorlig formatering**

 Aspose.Cells för Python via .NET stöder villkorlig formatering på flera sätt:

- Använda designerkalkylblad
- Använda kopieringsmetoden
- Skapa villkorlig formatering vid körning

### **Använda designerkalkylblad**

 Utvecklare kan skapa ett designat kalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylbladet med Aspose.Cells för Python via .NET. Aspose.Cells för Python via .NET laddar och sparar det designade kalkylbladet och behåller eventuella villkorliga formateringsinställningar.

### **Använda kopieringsmetoden**

 Aspose.Cells för Python via .NET tillåter utvecklare att kopiera inställningar för villkorsstyrd formatering från en cell till en annan i kalkylbladet genom att anropa [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy)-metoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Tillämpa villkorlig formatering under körning**

 Aspose.Cells för Python via .NET låter dig både lägga till och ta bort villkorsstyrd formatering vid körning. Följande kodexempel visar hur man ställer in villkorsstyrd formatering:

1. Skapa en arbetsbok.
1. Lägg till en tom villkorlig formatering.
1. Ange det intervall som formateringen ska tillämpas på.
1. Definiera formateringsvillkoren.
1. Spara filen.

Efter det här exemplet följer ett antal mindre exempel som visar hur man tillämpar teckensnittsinställningar, kantlinjeinställningar och mönster.

 Microsoft Excel 2007 tillförde mer avancerad villkorsstyrd formatering som Aspose.Cells för Python via .NET också stöder. Exemplen här illustrerar hur man använder enkel formatering, de Microsoft Excel 2007-exemplen visar hur man tillämpar mer avancerad villkorsstyrd formatering.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Ange font**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Du kan bara ändra teckensnittsstil, textfärg, understrykningsstil och överstrykningsstil.

{{% /alert %}}

### **Ange ram**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Du kan bara använda tunna linjestilar till ytterkanten. Diagonala linjer är inte tillåtna.

{{% /alert %}}

### **Ange mönster**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Fortsatta ämnen**
- [Lägga till 2-färgskala och 3-färgskala villkorliga formateringar](/cells/sv/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Tillämpa villkorlig formatering i arbetsblad](/cells/sv/python-net/apply-conditional-formatting-in-worksheets/)
- [Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering](/cells/sv/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generera bilder för databarformat i villkorlig formatering](/cells/sv/python-net/generate-conditional-formatting-databars-images/)
- [Hämta ikonsatser, databarer eller färgskalor som används i villkorlig formatering](/cells/sv/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}

---
title: Fontinställningar
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in teckensnittsinställningar för celler, vilket gör det möjligt för användare att anpassa teckensnittsstil och egenskaper för cellerna. Denna artikel introducerar hur man använder Aspose.Cells för Python via .NET biblioteket för att ställa in cellteckensnittsinställningar.
keywords: Aspose.Cells för Python via .NET, Celler, Teckensnittsinställningar, Stilar, Egenskaper
type: docs
weight: 30
url: /sv/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

Utseendet och känslan av en text kan styras genom att ändra teckensnittsinställningarna. Teckensnittsinställningarna kan inkludera namn, stil, storlek, färg och andra effekter av tecknen. Precis som Microsoft Excel stöder Aspose.Cells för Python via .NET också konfiguration av teckensnitt för celler.

{{% /alert %}}

## **Konfigurera fontinställningar**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells tillhandahåller klassens [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) metoder [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) och [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) som används för att hämta och ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) tillhandahåller egenskaper för att konfigurera fontinställningar.

### **Ange fontnamn**

Utvecklare kan tillämpa valfri teckensnitt på texten inuti en cell genom att använda [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-objektets [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/)-egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Ange fontstil till Fetstil**

Utvecklare kan göra texten fet genom att ställa in objektets [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Inställning av fontstorlek**

Ställ in fontstorlek med objektets [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Sätt Typsnittsfärg**

Använd objektets [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) för att ställa in fontfärgen. Välj valfri färg från Color-utseendet (en del av .NET-ramverket) och tilldela den till [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)-egenskapen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Inställning av font underlinjetyp**

Använd [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-objektets [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline)-egenskap för att understryka text. Aspose.Cells för Python via .NET erbjuder olika fördefinierade understrykningsstyper i [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype)-uppräkningen.

|**Font Underline Types**|**Beskrivning**|
| :- | :- |
|BOKFÖRING|Enkel understrykning för bokföring|
|DUBBEL|Dubbel understrykning|
|DUBBEL_BOKFÖRING|Dubbel bokföringsunderstrykning|
|INGEN|Ingen understrykning|
|ENKEL|En enkel understrykning|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Inställning för överstruken effekt**

Tillämpa överstrykning genom att ställa in objektets [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Inställning av understreckningseffekt**

Tillämpa understreckning genom att ställa in objektets [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) egenskap [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Inställning av överstruken effekt på font**

Utvecklare kan applicera överstruken effekt på fonten genom att ställa in [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) egenskapen för objektet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Fortsatta ämnen**
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


{{< app/cells/assistant language="python-net" >}}

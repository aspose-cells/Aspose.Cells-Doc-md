---
title: Fontinställningar
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler. Det stödjer inställning av cellernas fontinställningar, vilket gör det möjligt för användare att anpassa fontstilen och egenskaperna för cellerna. Den här artikeln kommer att introducera hur man använder Aspose.Cells biblioteket för att ställa in cellens fontinställningar.
keywords: Aspose.Cells, Cells, Fontinställningar, Stilar, Egenskaper
type: docs
weight: 30
url: /sv/net/cells-font-settings/
---

{{% alert color="primary" %}}

Utseendet och känslan av en text kan kontrolleras genom att ändra fontinställningarna. Fontinställningarna kan inkludera namn, stil, storlek, färg och andra effekter för teckensnitten. Precis som Microsoft Excel stöder även Aspose.Cells konfigurering av cellernas fontinställningar.

{{% /alert %}}

## **Konfigurera fontinställningar**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje kalkylblad i en Excelfil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells tillhandahåller klassens [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) metoder [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) som används för att hämta och ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) tillhandahåller egenskaper för att konfigurera fontinställningar.

### **Ange fontnamn**

Utvecklare kan applicera vilken som helst font på texten inuti en cell genom att använda objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)-egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Ange fontstil till Fetstil**

Utvecklare kan göra texten fet genom att ställa in objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) till **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Inställning av fontstorlek**

Ställ in fontstorlek med objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Sätt Typsnittsfärg**

Använd objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) för att ställa in fontfärgen. Välj valfri färg från Color-utseendet (en del av .NET-ramverket) och tilldela den till [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)-egenskapen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Inställning av font underlinjetyp**

Använd objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) för att understryka text. Aspose.Cells erbjuder olika fördefinierade teckenstilunderstrykningstyper i [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)-utseendet.

|**Font Underline Types**|**Beskrivning**|
| :- | :- |
|Accounting|Enkel redovisningsunderstrykning|
|Double|Dubbel understrykning|
|DoubleAccounting|Dubbel redovisningsunderstrykning|
|None|Ingen understrykning|
|Single|Enkel understrykning|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Inställning för överstruken effekt**

Tillämpa överstrykning genom att ställa in objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) till **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Inställning av understreckningseffekt**

Tillämpa understreckning genom att ställa in objektets [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) egenskap [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) till **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Inställning av överstruken effekt på font**

Utvecklare kan applicera överstruken effekt på fonten genom att ställa in [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) egenskapen för objektet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) till **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Fortsatta ämnen**
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


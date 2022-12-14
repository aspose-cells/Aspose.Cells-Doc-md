---
title: Teckensnittsinställningar
type: docs
weight: 30
url: /sv/net/cells-font-settings/
---
{{% alert color="primary" %}}

Utseendet och känslan av en text kan styras genom att ändra teckensnittsinställningar. Teckensnittsinställningarna kan inkludera namn, stil, storlek, färg och andra effekter av typsnitten. Precis som Microsoft Excel stöder Aspose.Cells också konfigurering av teckensnittsinställningarna för cellerna.

{{% /alert %}}

## **Konfigurera teckensnittsinställningar**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 Aspose.Cells tillhandahåller[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoder som används för att hämta och ställa in en cells formateringsstil. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class tillhandahåller egenskaper för att konfigurera teckensnittsinställningar.

### **Ställa in teckensnittsnamn**

 Utvecklare kan använda vilket typsnitt som helst på text inuti en cell genom att använda[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objekt[namn](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Ställ in teckensnitt till fet stil**

 Utvecklare kan göra text fet genom att ställa in[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objekt[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) egendom till**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Ställa in teckensnittsstorlek**

Ställ in teckenstorleken med[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objekt[**Storlek**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Ställa in teckensnittsfärg**

Använd[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objekt[**Färg**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)egenskap för att ställa in teckensnittsfärgen. Välj valfri färg från färguppräkningen (en del av .NET-ramverket) och tilldela den till[**Färg**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Ställa in typsnitt för understrykning**

Använd[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objekt[**Understrykning**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)egenskap för att understryka text. Aspose.Cells erbjuder olika fördefinierade teckensnittsunderstrykningstyper i[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) uppräkning.

|**Typer av understrykning av teckensnitt**|**Beskrivning**|
|:- |:- |
|Bokföring|En enda redovisningsunderstrykning|
|Dubbel|Dubbel understrykning|
|Dubbelredovisning|Dubbel bokföringsunderstrykning|
|Ingen|Ingen understrykning|
|Enda|En enda understrykning|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Ställa in överstruken effekt**

Använd genomstruken genom att ställa in[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objekt[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)egendom till**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Ställa in Subscript Effect**

Använd prenumeration genom att ställa in[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objekt[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) egendom till**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Ställa in upphöjd effekt på teckensnitt**

Utvecklare kan tillämpa den upphöjda effekten på teckensnittet genom att ställa in[**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) egendom av[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) invända mot**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Förhandsämnen**
- [Använd upphöjda och nedsänkta effekter på teckensnitt](/cells/sv/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok](/cells/sv/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


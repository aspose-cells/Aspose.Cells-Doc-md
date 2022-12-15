---
title: Hantera teckensnittsinställningar
linktitle: Teckensnittsinställningar
type: docs
weight: 20
url: /sv/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

Textens utseende och känsla kan styras genom att ändra dess teckensnittsinställningar. Dessa teckensnittsinställningar kan inkludera namn, stil, storlek, färg och andra effekter av teckensnitten som visas nedan i figuren:

**Teckensnittsinställningar i Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Precis som Microsoft Excel, stöder Aspose.Cells också konfigurering av teckensnittsinställningarna för cellerna.

{{% /alert %}} 
## **Konfigurera teckensnittsinställningar**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

 Aspose.Cells tillhandahåller[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) metod, som används för att ställa in en cells formatering. Också föremålet för[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class tillhandahåller egenskaper för att konfigurera teckensnittsinställningar.

Den här artikeln visar hur du:

- [Använd ett specifikt teckensnitt på text.](/cells/sv/java/dealing-with-font-settings/)
- [Ställ in text i fetstil](/cells/sv/java/dealing-with-font-settings/).
- [Ställ in teckenstorleken](/cells/sv/java/dealing-with-font-settings/).
- [Ställ in teckensnittsfärgen](/cells/sv/java/dealing-with-font-settings/).
- [Stryk under text](/cells/sv/java/dealing-with-font-settings/).
- [Överstruken text](/cells/sv/java/dealing-with-font-settings/).
- [Ställ in text till subscript](/cells/sv/java/dealing-with-font-settings/).
- [Ställ in text till upphöjd](/cells/sv/java/dealing-with-font-settings/).
### **Ställa in teckensnittsnamn**
 Använd ett specifikt teckensnitt på text i celler med hjälp av[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[Ange namn](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Ställ in teckensnitt till fet stil**
 Ställ in text till fetstil genom att ställa in[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setFet](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) egendom till**Sann**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Ställa in teckensnittsstorlek**
 Ställ in teckenstorleken med hjälp av[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Ställa in typsnitt för understrykning**
 Stryk under texten med[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setUnderlinje](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) fast egendom. Aspose.Cells erbjuder olika fördefinierade teckensnittsunderstrykningstyper i[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)uppräkning.

|**Typer av understrykning av teckensnitt**|**Beskrivning**|
|:- |:- |
|[INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Ingen understrykning|
|[ENDA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|En enda understrykning|
|[DUBBEL](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Dubbel understrykning|
|[BOKFÖRING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|En enda redovisningsunderstrykning|
|[DUBBEL_REKTO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Dubbel bokföringsunderstrykning|
|[RUSA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Streckad underlinje|
|[RUSA_PUNKT_PUNKT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Tjock streck-punkt-punkt understrykning|
|[RUSA_PUNKT_TUNG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Tjock streck-punkt understrykning|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Tjock streckad underlinje|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Lång streckad underlinje|
|[RUSA_LÅNG_TUNG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Tjock lång streckad underlinje|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Streck-Prick understrykning|
|[PUNKT_PUNKT_RUSA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Streck-Prick-Prick understrykning|
|[PRICKAD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Prickad underlinje|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Tjock prickad underlinje|
|[TUNG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Tjock understrykning|
|[VINKA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Vågunderstrykning|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Dubbelvåg understrykning|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Heavy Wave Underline|
|` `[ORD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Understryka endast tecken som inte är mellanslag|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Ställa in teckensnittsfärg**
 Ställ in teckensnittsfärgen med[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) fast egendom. Välj valfri färg från[Färg](https://reference.aspose.com/cells/java/com.aspose.cells/Color) uppräkning och tilldela den valda färgen till[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Ställa in genomstruken effekt på text**
 Överstruken text med[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Ställa in Subscript**
 Gör text upphöjd genom att använda[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Ställa in Upphöjd**
 Använd upphöjd text på text med[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objekt[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Förhandsämnen**
- [Använd upphöjda och nedsänkta effekter på teckensnitt](/cells/sv/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok](/cells/sv/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

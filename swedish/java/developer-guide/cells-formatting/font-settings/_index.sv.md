---
title: Hantera fontinställningar
linktitle: Fontinställningar
type: docs
weight: 20
url: /sv/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

Textens utseende och känsla kan kontrolleras genom att ändra dess fontinställningar. Dessa fontinställningar kan inkludera namn, stil, storlek, färg och andra effekter av fonterna såsom visat nedan i figuren:

**Fontinställningar i Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Precis som Microsoft Excel, stöder även Aspose.Cells konfigurering av cellernas fontinställningar.

{{% /alert %}} 
## **Konfigurera fontinställningar**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje arbetsblad i en Excelfil. Ett arbetsblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klassens [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) metod, som används för att ställa in cellens formatering. Dessutom ger objektet av [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) klass egenskaper för att konfigurera typsnittsinställningar.

Den här artikeln visar hur du:

- [Använd en specifik font för text.](/cells/sv/java/dealing-with-font-settings/)
- [Ställ in text som fet](/cells/sv/java/dealing-with-font-settings/).
- [Ange fontstorleken](/cells/sv/java/dealing-with-font-settings/).
- [Ange fontfärgen](/cells/sv/java/dealing-with-font-settings/).
- [Understruken text](/cells/sv/java/dealing-with-font-settings/).
- [Stryka över text](/cells/sv/java/dealing-with-font-settings/).
- [Ange text som subscript](/cells/sv/java/dealing-with-font-settings/).
- [Ange text som superscript](/cells/sv/java/dealing-with-font-settings/).
### **Ange fontnamn**
Tillämpa en specifik font på text i celler med hjälp av [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objektets [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Ange fontstil till Fetstil**
Ange texten till fetstil genom att ställa [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objektets [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) egenskap till **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Inställning av fontstorlek**
Ange fontstorleken med [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objektets [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Inställning av font underlinjetyp**
Understryk text med [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objektets [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) egenskap. Aspose.Cells erbjuder olika fördefinierade font underlinjetyper i [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) uppräkning.

|**Font Underline Types**|**Beskrivning**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Ingen understrykning|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Enkel understrykning|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Dubbel understrykning|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Enkel bokföringsunderstrykning|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|Dubbel bokföringslinje|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Streckad understrykning|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|Tjock punktstreck-linje|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|Tjock streck-punkt-linje|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|Tjock streckad linje|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|Lång streckad linje|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|Tjock lång streckad linje|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|Streck-punkt-linje|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|Doppelt streck-punkt-linje|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Prickad understrykning|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|Tjock prickad linje|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Tjock Underline|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Våg Underline|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|Dubbel vågig linje|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|Tung vågig linje|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Underline Endast Tecken Utan Mellanslag|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Sätt Typsnittsfärg**
Ställ in typsnittsfärg med [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-objektets [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)-egenskap. Välj en färg från [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-uppräkningen och tilldela den valda färgen till [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-objektets [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Ställ in Strikeout-effekt på text**
Stryk över text med [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-objektets [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)-egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Ställa in subscript**
Gör text upphöjd genom att använda [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-objektets [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)-egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Ställa in superscript**
Använda superscript på text med [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-objektets [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)-egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Fortsatta ämnen**
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="java" >}}

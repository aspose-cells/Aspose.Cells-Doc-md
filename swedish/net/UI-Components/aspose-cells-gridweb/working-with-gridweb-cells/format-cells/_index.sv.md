---
title: Formatera cell
type: docs
weight: 40
url: /sv/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb, format, stil
description: Den här artikeln introducerar hur man ställer in eller tillämpar stilformat för en cell (GridCell) i GridWeb.
---

{{% alert color="primary" %}} 

Detta ämne ger en detaljerad diskussion om hur man formaterar celler.

Det täcker formatering av celler i GUI-läge med hjälp av Aspose.Cells.GridWeb-kontrollens stil-dialog. Det visar också hur man formaterar celler programmatiskt. Olika formatinställningar som typsnitt, ram och nummerformat diskuteras, illustreras med exempel.

{{% /alert %}} 
## **Formatering av celler med hjälp av stil-dialogen**
Celler kan formateras [programmatiskt](/cells/sv/net/aspose-cells-gridweb/format-cells/) men det enklaste sättet att formatera celler i Aspose.Cells.GridWeb-kontrollen på ett WYSIWYG-sätt är att använda stil-dialogen.

För att använda stil-dialogen:
Välj ett cellintervall och högerklicka sedan för att välja **Formatera cell**. 

**Välja Formatera cell** 

![todo:image_alt_text](format-cells_1.png)



Dialogrutan för stil visas. 

**Stil dialogrutan används för att formatera celler** 

![todo:image_alt_text](format-cells_2.png)

Dialogrutan för stil låter användare formatera celler genom att anpassa font- och kantinställningar.
### **Anpassa fontinställningar**
Du kan anpassa följande fontinställningar med hjälp av stil dialogrutan:

- Fontnamn, välj en önskad font från listan.
- Fontstil, tillämpa en fontstil som fet, kursiv etc.
- Fontstorlek, välj en fontstorlek i punkter.
- Understrykning, understryk text.
- Genomstrykning, tillämpa en genomstryknings effekt på text.
- Horisontell justering, välj horisontell justering.
- Vertikal justering, välj vertikal justering.
- Fontfärg, välj en fontfärg.
- Bakgrund, välj en färg för bakgrunden.

Du kan kontrollera de valda fontinställningarna i en liten förhandsgransknings area.

**Anpassade fontinställningar** 

![todo:image_alt_text](format-cells_3.png)
### **Anpassa kantinställningar**
Kontrollen tillåter också användare att rita en kant runt celler genom att anpassa kantinställningarna i stil dialogrutan.

För att visa kantrelaterade alternativ:
Klicka på **Kanter** i stil dialogrutan.
Kantrelaterade alternativ visas. 

**Kantalternativ i stil dialogrutan** 

![todo:image_alt_text](format-cells_4.png)

Följande kantalternativ kan väljas från stil dialogrutan:

- Kantlinjestil, välj kantstilen som solid, streckad etc.
- Kantlinjebredd, välj kantbredd i pixlar.
- Kantlinjefärg, välj linjefärg.
- Kantlinjer, välj numrering och placering av kantlinjer.

**Anpassade kantinställningar** 

![todo:image_alt_text](format-cells_5.png)
### **Tillämpar inställningar**
Klicka på **OK** i Stil-dialogrutan för att tillämpa ändringarna.

**Teckensnitts- och kantinställningar har tillämpats** 

![todo:image_alt_text](format-cells_6.png)


## **Formaterar celler med hjälp av API:et**
Celler kan också formateras programmatiskt med hjälp av Aspose.Cells.GridWeb API. Varje cell har en Style-egenskap som representerar ett GridTableItemStyle-objekt. Använd Style-egenskapen för att anpassa teckensnitts- och kantinställningar.
### **Inställning av teckensnitt**
För att anpassa teckensnittsinställningar programmatiskt:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
1. Öppna den cell du formaterar.
1. Öppna cellens stil.
1. Ange teckensnittets storlek i punkter.
1. Ange teckensnittets stil.
1. Ange bakgrundsfärg och förgrundsfärg.
1. Ange horisontell och vertikal justering.
1. Återställ stilen till cellen.

**Resultat: anpassade teckensnittsinställningar visas i A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Inställning av kanter**
Kanter kan tillämpas på enskilda celler eller på ett område.
#### **Enskild cell**
För att ställa in kanterna på en enskild cell:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
1. Öppna den cell du ska formatera.
1. Öppna cellens Style-objekt.
1. Ange kanter stil.
1. Ange kanternas bredd i pixlar.
1. Ange kanternas färg.
1. Ange stilen till cellen.

**Anpassade kantinställningar på en enskild cell** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Det är möjligt att ange olika stilar för varje kantlinje med cellens Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle egenskaper.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Intervall av celler**
För att ställa in kanter på en rad celler:

1. Lägg till Aspose.Cells.GridWeb-kontroll i din webbformulär
1. Åtkomst till önskad arbetsblad
1. Instantiera en objekt av klassen WebBorderStyle
1. Ställ in stil på kanten till Solid eller Dashed etc.
1. Ställ in bredd på kanten i pixlar
1. Ställ in färg på kanten
1. Tillämpa kantinställningar som är lagrade i WebBorderStyle-objektet på en angiven cellradsintervall

**Ett cellrad med anpassade kantinställningar** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Inställning av nummerformat**
Aspose.Cells.GridWeb stödjer inställning av nummerformat. Det finns 59 inbyggda nummerformat. För att se dem, var god hänvisa till denna [lista över stödda nummerformat](/cells/sv/net/aspose-cells-gridweb/list-of-supported-number-formats/).

Alla inbyggda nummerformat finns i NumberType-uppräkningen. För att använda ett inbyggt nummerformat, ställ in NumberType med hjälp av SetNumberType-metoden i cellens objekt till ett nummerformat från NumberType-uppräkningen.

För att ställa in anpassat nummerformat, använd cellens SetCustom-metod.

**Nummerformatinställningar som tillämpas på B1 och B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}

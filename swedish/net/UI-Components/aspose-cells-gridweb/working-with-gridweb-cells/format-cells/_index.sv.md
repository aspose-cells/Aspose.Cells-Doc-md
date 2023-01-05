---
title: Format Cells
type: docs
weight: 40
url: /sv/net/format-grid-cells/
---
{{% alert color="primary" %}} 

Det här ämnet ger en detaljerad diskussion om hur man formaterar celler.

Den täcker formatering av celler i GUI-läge med hjälp av Aspose.Cells.GridWeb-kontrollens stildialog. Den visar också hur man formaterar celler programmatiskt. Olika formatinställningar som typsnitt, ram och talformat diskuteras, illustrerade med exempel.

{{% /alert %}} 
## **Formatering Cells Använda stildialogrutan**
 Cells kan formateras[programmatiskt](/cells/sv/net/format-cells/)men det enklaste sättet att formatera celler i Aspose.Cells.GridWeb-kontrollen på ett WYSIWYG-sätt är att använda dialogrutan Stil.

Så här använder du dialogrutan Stil:
 Välj ett cellintervall och högerklicka sedan och välj**Format Cell**. 

**Välj format Cell** 

![todo:image_alt_text](format-cells_1.png)



 Dialogrutan Stil visas.

**Formatdialogen används för att formatera celler** 

![todo:image_alt_text](format-cells_2.png)

Dialogrutan Stil låter användarna formatera celler genom att anpassa teckensnitt och raminställningar.
### **Anpassa teckensnittsinställningar**
Du kan anpassa följande teckensnittsinställningar med hjälp av dialogrutan Stil:

- Teckensnittsnamn, välj önskat teckensnitt i listan.
- Teckensnittsstil, använd en typsnittsstil som fetstil, kursiv etc.
- Teckenstorlek, välj en teckenstorlek i punkter.
- Understryka, understryka text.
- Genomstruken, tillämpa en genomstruken effekt på text.
- Horisontell justering, välj horisontell justering.
- Vertikal justering, välj vertikal justering.
- Teckensnittsfärg, välj en teckensnittsfärg.
- Bakgrund, välj en färg för bakgrunden.

Du kan kontrollera de valda teckensnittsinställningarna i ett litet förhandsvisningsområde.

**Anpassade teckensnittsinställningar** 

![todo:image_alt_text](format-cells_3.png)
### **Anpassa gränsinställningar**
Kontrollen tillåter också användare att rita en ram runt celler genom att anpassa raminställningarna i dialogrutan Stil.

Så här visar du gränsrelaterade alternativ:
 Klick**Gränser** i dialogrutan Stil.
 Kantrelaterade alternativ visas.

**Kantalternativ i stildialogrutan** 

![todo:image_alt_text](format-cells_4.png)

Följande kantalternativ kan väljas från dialogrutan Stil:

- Kantlinjestil, välj kantstil som heldragen, streckad etc.
- Kantlinjebredd, välj kantbredd i pixlar.
- Kantlinjefärg, välj linjefärg.
- Kantlinjer, välj numrering och placering av kantlinjer.

**Anpassade gränsinställningar** 

![todo:image_alt_text](format-cells_5.png)
### **Tillämpa inställningar**
 Klick**OK** i dialogrutan Stil för att tillämpa ändringarna.

**Teckensnitt och kantinställningar tillämpas** 

![todo:image_alt_text](format-cells_6.png)


## **Formatera Cells med API**
Cells kan också formateras programmatiskt med Aspose.Cells.GridWeb API. Varje cell har en Style-egenskap, som representerar ett GridTableItemStyle-objekt. Använd egenskapen Style för att anpassa teckensnitts- och raminställningar.
### **Ställa in teckensnitt**
Så här anpassar du teckensnittsinställningar programmatiskt:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Gå till cellen du formaterar.
1. Få åtkomst till cellens stil.
1. Ställ in teckenstorleken i punkter.
1. Ställ in teckensnittsstilen.
1. Ställ in förgrunds- och bakgrundsfärger.
1. Ställ in horisontell och vertikal justering.
1. Ställ tillbaka stilen till cellen.

**Utdata: anpassade teckensnittsinställningar som visas i A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Ställa in gränser**
Kanter kan tillämpas på enskilda celler eller på ett område.
#### **Singel Cell**
Så här ställer du in gränserna för en enskild cell:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Gå till cellen du ska formatera.
1. Öppna cellens stilobjekt.
1. Ställ in kantstilen.
1. Ställ in kantens bredd i pixlar.
1. Ställ in kantfärgen.
1. Ställ in stilen på cellen.

**Anpassade kantinställningar på en enda cell** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Det är möjligt att ställa in olika stilar för varje kantlinje med cellens egenskaper Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Räckvidd Cells**
Så här ställer du in gränser för ett cellintervall:

1. Lägg till Aspose.Cells.GridWeb-kontroll till ditt webbformulär
1. Öppna ett önskat arbetsblad
1. Instantiera ett objekt av klassen WebBorderStyle
1. Ställ in gränsens stil till solid eller streckad etc.
1. Ställ in kantens bredd i pixlar
1. Ställ in färg på gränsen
1. Tillämpa kantinställningar lagrade i WebBorderStyle-objektet på ett specificerat cellområde

**En rad celler med anpassade raminställningar** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Ställa in talformat**
 Aspose.Cells.GridWeb stöder inställning av nummerformat. Det finns 59 inbyggda talformat. För att se dem, se detta[lista över talformat som stöds](/cells/sv/net/list-of-supported-number-formats/).

Alla inbyggda talformat finns i NumberType-uppräkningen. För att använda ett inbyggt talformat, ställ in NumberType med SetNumberType-metoden för en cells objekt till ett talformat från NumberType-uppräkningen.

Använd cellens SetCustom-metod för att ställa in anpassat talformat.

**Inställningar för nummerformat tillämpas på B1 och B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}

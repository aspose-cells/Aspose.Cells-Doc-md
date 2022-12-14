---
title: Applicera stilar på GridWeb
type: docs
weight: 20
url: /sv/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb har sitt eget standardutseende och känsla men det är möjligt att ändra dess utseende. Aspose.Cells.GridWeb tillhandahåller flera egenskaper för att låta utvecklare helt kontrollera dess utseende. Det här ämnet diskuterar några av dessa egenskaper.

{{% /alert %}} 
## **Tillämpa förinställda eller anpassade stilar på Aspose.Cells.GridWeb**
### **Förinställda stilar**
För att spara på utvecklarnas ansträngningar erbjuder Aspose.Cells.GridWeb några förinställda stilar. Välj helt enkelt en stil från listan för att tillämpa stilen.

|**Stilar**|**Färgschema**|
|:- |:- |
|Standard|Silver|
|Färgglad 1|Reste sig|
|Färgglada 2|Blå|
|Professionell 1|Cyan|
|Professionell 2|Cyan igen|
|Traditionell 1|Mörk|
|Traditionell 2|grå|
|Beställnings|Anpassat|
När en viss stil väljs ändrar den hela utseendet på GridWeb-kontrollen. Utvecklare kan välja en förinställd stil som ska tillämpas på Grid under designtiden, men denna uppgift kan också utföras under körning med det flexibla API:et Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb-kontroll representeras av GridWeb-klassen.

{{% /alert %}} 

Så här väljer du en förinställd stil:

1. Lägg till Aspose.Cells.GridWeb-kontroll i ett webbformulär.
1. Välj en förinställd stil som ska tillämpas på kontrollen.

GridWeb-kontrollen tillhandahåller PresetStyle-egenskapen som utvecklare kan tilldela vilken förinställd stil som helst.

 Utdata från nedanstående kodavsnitt visas nedan.

**GridWeb-kontroll med Colorful1-stilen applicerad på den** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Header Bar Style**
Om du tittar på GridWeb-kontrollen kommer du att märka två rubrikfält. En för kolumner (det vill säga A, B, C, D etc.) och en annan för rader (det vill säga 1, 2, 3, 4 etc.). Aspose.Cells.GridWeb tillåter utvecklare att kontrollera utseendet på dessa sidhuvuden. Utvecklare kan ställa in stilen på sidhuvuden antingen vid designtid eller körning.

{{% alert color="primary" %}} 

GridWeb-kontrollen tillhandahåller egenskapen HeaderBarStyle som tillämpar en stil på kontrollens båda rubrikfält.

{{% /alert %}} 

 Utgången exempelkoden nedan visas här.

**Modifierad stil för Header Bar** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Tabbar stil**
 Det är möjligt att ställa in stilen på flikfältet.

**Ändrade stilar för aktiva och icke-aktiva flikfält** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

I figuren ovan är Sheet4 den aktiva fliken så dess utseende skiljer sig från de andra flikarna, som definieras av exempelkoden nedan.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Återanvändbar anpassad stilfil**
Aspose.Cells.GridWeb stöder också för att bevara dess utseende eller stilinställningar till en fil. När du har ställt in alla utseendeegenskaper för GridWeb-kontrollen kan du spara dessa egenskaper eller inställningar till en diskfil. Detta tillvägagångssätt är mycket användbart för utvecklare att spara tid och ansträngningar genom att återanvända sina gamla stilkonfigurationer från en stilfil istället för att ställa in alla stilegenskaper (eller utseende) för kontrollen en efter en.
### **Sparar stilfil**
När du har ställt in stilegenskaper kan du spara dina stilkonfigurationsinställningar i form av en XML-fil (det beror på att den stilfilen är lagrad som en XML-fil) genom att anropa SaveCustomStyleFile-metoden för GridWeb-kontrollen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Den sparade stilfilen är i XML-format så utvecklare kan också redigera den här filen med valfri textredigerare om så önskas.

{{% /alert %}} 
### **Laddar stilfil**
För att tillämpa stilinställningar från en befintlig stilfil på GridWeb-kontroll kan utvecklare ställa in sökvägen för stilfilen till CustomStyleFileName-egenskapen för kontrollen. Men innan du gör det måste du ställa in PresetStyle-egenskapen för kontroll till Custom. Det beror på att stilfilen innehåller anpassad stilinformation som redan är definierad av en utvecklare.

{{% alert color="primary" %}} 

Det är också möjligt att ladda eller spara stilfil med Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Att ladda stilfilen till GridWeb-kontrollen påverkar inte formateringsinställningarna för kontrollens celler.

{{% /alert %}} 
### **Standardformat för XML-stilmall**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

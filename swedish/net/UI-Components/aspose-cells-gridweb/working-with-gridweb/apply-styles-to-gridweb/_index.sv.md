---
title: Tillämpa stilar på GridWeb
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, stil, stilar
description: Denna artikel introducerar hur man tillämpar eller sätter stil i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb har sin egen standardstil men det är möjligt att ändra dess utseende. Aspose.Cells.GridWeb tillhandahåller flera egenskaper för att låta utvecklare ha full kontroll över dess utseende. Detta ämne diskuterar några av dessa egenskaper.

{{% /alert %}} 
## **Tillämpa förinställda eller anpassade stilar på Aspose.Cells.GridWeb**
### **Förinställda stilar**
För att spara utvecklares ansträngningar erbjuder Aspose.Cells.GridWeb några förinställda stilar. Välj helt enkelt en stil från listan för att tillämpa stilen.

|**Stilar**|**Färgschema**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
När en särskild stil väljs ändras hela utseendet på GridWeb-kontrollen. Utvecklare kan välja en förinställd stil att tillämpas på Grid under designtid men denna uppgift kan också utföras vid körning med hjälp av den flexibla API:et för Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb-kontrollen representeras av GridWeb-klassen.

{{% /alert %}} 

För att välja en förinställd stil:

1. Lägg till Aspose.Cells.GridWeb-kontroll på ett webbformulär.
1. Välj en förinställd stil att tillämpas på kontrollen.

GridWeb-kontrollen tillhandahåller egenskapen PresetStyle till vilken utvecklare kan tilldela en önskad förinställd stil.

Resultatet av kodsnutten nedan visas nedan. 

**GridWeb-kontroll med stil applicerad på Colorful1** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Header Bar Style**
Om du tar en titt på GridWeb-kontrollen kommer du att märka två huvudfält. Ett för kolumner (dvs. A, B, C, D etc.) och ett för rader (dvs. 1, 2, 3, 4 etc.). Aspose.Cells.GridWeb tillåter utvecklare att kontrollera utseendet av dessa huvudfält. Utvecklare kan ange stilen för huvudfälten antingen vid design tid eller körning.

{{% alert color="primary" %}} 

GridWeb-kontrollen tillhandahåller egenskapen HeaderBarStyle som tillämpar en stil på båda headerfälten i kontrollen.

{{% /alert %}} 

Utmatningen av exemplet nedan visas här. 

Modifierad stil för huvudfält 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Tab Bar Style**
Det är möjligt att ställa in stilen för flikfältet. 

Modifierade stilar för aktiva och inaktiva flikfält 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

I figuren ovan är Blad4 den aktiva fliken så dess utseende skiljer sig från de andra flikarna, enligt exemplifierad kod nedan.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Återanvändbar anpassad stilfil**
Aspose.Cells.GridWeb stöder även att bestända sitt utseende eller stilinställningar till en fil. När du har ställt in alla utseendeelement för GridWeb-kontrollen kan du spara dessa egenskaper eller inställningar till en diskfil. Detta tillvägagångssätt är mycket användbart för utvecklare att spara sin tid och ansträngningar genom att återanvända sina gamla stilkonfigurationer från en stilfil istället för att ställa in alla stilegenskaper för kontrollen en och en.
### **Spara stilfil**
När du har avslutat inställningen av stilegenskaper kan du spara dina stilinställningar i form av en XML-fil (detta eftersom stilen sparas som en XML-fil) genom att anropa SaveCustomStyleFile-metoden för GridWeb-kontrollen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Den sparade stilfilen är i XML-format så utvecklare kan också redigera denna fil med en textredigerare om så önskas.

{{% /alert %}} 
### **Laddningsstilfil**
För att tillämpa stilinställningar från en befintlig stilfil på GridWeb-kontrollen kan utvecklare ställa in sökvägen för stilfilen till CustomStyleFileName-egenskapen för kontrollen. Men innan du gör det är det obligatoriskt att ställa in PresetStyle-egenskapen för kontrollen till Anpassad. Det är för att stilfilen innehåller anpassad stilinformation som redan är definierad av en utvecklare.

{{% alert color="primary" %}} 

Det är också möjligt att ladda eller spara stilfilen med hjälp av Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Att ladda stilfilen i GridWeb-kontrollen påverkar inte cellens formateringsinställningar för kontrollen.

{{% /alert %}} 
### **Standardformat för XML-stilmall**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

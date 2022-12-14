---
title: Aktivera GridWeb EditBox
type: docs
weight: 110
url: /sv/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

GridWebs redigeringsruta är ett verktygsfält som återges överst i kontrollen som du kan använda för att se/skriva in eller kopiera data/formel till celler. Den visar också cellens namn som du redigerar. Efter att ha klickat på ramen eller när du börjar skriva data eller skriva en lika (=) symbol, kommer redigeringsrutan att aktiveras.

{{% /alert %}} 
## **Ställa in redigeringsrutan för Aspose.Cells.GridWeb**
GridWeb-kontrollen tillhandahåller egenskapen ShowCellEditBox som utvecklare kan tilldela den till "True" för att aktivera verktygsfältet. Standardvärdet för attributet är False. När du ställer in dess värde till "True", kommer redigeringsrutan att visas överst på GridWeb-kontrollen.

{{% alert color="primary" %}} 

 För att aktivera den här funktionen måste du importera filen "jquery.js" till ditt projekt och hänvisa till den på dina .aspx-sidor för att få det att fungera. Du kan ladda ner jQuery-arkivet från<https://jqueryui.com/download/all/> och lägg biblioteksfilen(erna) i någon mapp i projektet och lägg till referens till biblioteksfilen via<script> tagga i ditt .aspx-webbformulär enligt följande. Alla de senaste jQuery-versionerna är OK.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**GridWeb-kontroll med Edit Box** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Exempel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}

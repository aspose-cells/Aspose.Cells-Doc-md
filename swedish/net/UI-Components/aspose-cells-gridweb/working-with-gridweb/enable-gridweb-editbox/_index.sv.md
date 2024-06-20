---
title: Aktivera GridWeb EditBox
type: docs
weight: 110
url: /sv/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, editbox, formelrad
description: Denna artikel introducerar hur man arbetar med formelrad eller editbox i GridWeb.
---

{{% alert color="primary" %}} 

GridWeb's Edit Box (i Excel kallad formelrad) är en verktygsfält som renderas längst upp i kontrollen och som du kan använda för att visa eller mata in värde eller kopiera data/formel för den markerade cellen. Det visar också cellens namn som du redigerar. Efter att ha klickat på ramen eller när du börjar skriva data eller skriver ett likhetstecken (=) kommer Edit Box att aktiveras.

{{% /alert %}} 
## **Inställning av Aspose.Cells.GridWeb's Edit Box**
GridWeb-kontrollen tillhandahåller egenskapen ShowCellEditBox till vilken utvecklare kan tilldela "True" för att aktivera verktygsfältet. Attributets standardvärde är False. När du anger dess värde som "True" kommer Edit Box att visas längst upp i GridWeb-kontrollen.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

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

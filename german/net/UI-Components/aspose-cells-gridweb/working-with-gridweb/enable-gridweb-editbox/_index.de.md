---
title: GridWeb EditBox aktivieren
type: docs
weight: 110
url: /de/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, Editbox, Formel Leiste
description: Dieser Artikel erläutert, wie Sie mit der Formel Leiste oder der Edit Box in GridWeb arbeiten.
---

{{% alert color="primary" %}} 

Die Edit Box von GridWeb (in Excel Formel-Leiste genannt) ist eine Symbolleiste, die oben auf der Steuerung gerendert wird und die Sie verwenden können, um Werte anzuzeigen oder einzugeben oder Daten/ Formeln für die markierte Zelle zu kopieren. Es zeigt auch den Namen der Zelle an, die Sie bearbeiten. Nach dem Klicken auf den Rahmen oder beim Beginnen der Eingabe von Daten oder dem Schreiben eines Gleichheitszeichens (=) wird die Edit Box aktiviert.

{{% /alert %}} 
## **Konfigurieren der Edit Box von Aspose.Cells.GridWeb**
Die GridWeb-Steuerung bietet die Eigenschaft ShowCellEditBox, auf die Entwickler sie auf "True" setzen können, um die Symbolleiste einzuschalten. Der Standardwert des Attributes ist False. Wenn Sie den Wert auf "True" setzen, wird die Edit Box oben auf der GridWeb-Steuerung angezeigt.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**GridWeb-Steuerung mit Edit Box** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Beispiel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}

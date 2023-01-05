---
title: GridWeb-EditBox aktivieren
type: docs
weight: 110
url: /de/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

Das Bearbeitungsfeld von GridWeb ist eine Symbolleiste, die oben im Steuerelement angezeigt wird und mit der Sie Daten/Formeln anzeigen/eingeben oder in Zellen kopieren können. Es zeigt auch den Namen der Zelle, die Sie bearbeiten. Nachdem Sie auf den Rahmen geklickt haben oder wenn Sie mit dem Schreiben von Daten beginnen oder ein Gleichheitszeichen (=) eingeben, wird das Bearbeitungsfeld aktiviert.

{{% /alert %}} 
## **Festlegen des Bearbeitungsfelds von Aspose.Cells.GridWeb**
Das GridWeb-Steuerelement stellt die ShowCellEditBox-Eigenschaft bereit, der Entwickler sie auf „True“ zuweisen können, um die Symbolleiste zu aktivieren. Der Standardwert des Attributs ist False. Wenn Sie seinen Wert auf "True" setzen, wird das Bearbeitungsfeld oben im GridWeb-Steuerelement angezeigt.

{{% alert color="primary" %}} 

 Um diese Funktion zu aktivieren, müssen Sie die Datei „jquery.js“ in Ihr Projekt importieren und auf Ihren ASPX-Seiten darauf verweisen, damit sie funktioniert. Sie können das jQuery-Archiv von herunterladen<https://jqueryui.com/download/all/> und legen Sie die Bibliotheksdatei(en) in einem Ordner im Projekt ab und fügen Sie einen Verweis auf die Bibliotheksdatei hinzu über<script> -Tag in Ihrem ASPX-Webformular wie folgt. Alle aktuellen jQuery-Versionen sind in Ordnung.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**GridWeb-Steuerelement mit Bearbeitungsfeld** 

![todo: Bild_alt_Text](enable-gridweb-editbox_1.png)
### **Beispiel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}

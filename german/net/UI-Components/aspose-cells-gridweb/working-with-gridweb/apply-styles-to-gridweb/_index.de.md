---
title: Wenden Sie Stile auf GridWeb an
type: docs
weight: 20
url: /de/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells. GridWeb hat sein eigenes Standard-Look & Feel, aber es ist möglich, sein Aussehen zu ändern. Aspose.Cells.GridWeb bietet mehrere Eigenschaften, mit denen Entwickler das Erscheinungsbild vollständig steuern können. In diesem Thema werden einige dieser Eigenschaften erläutert.

{{% /alert %}} 
## **Anwenden von voreingestellten oder benutzerdefinierten Stilen auf Aspose.Cells.GridWeb**
### **Voreingestellte Stile**
Um Entwicklern den Aufwand zu ersparen, bietet Aspose.Cells.GridWeb einige voreingestellte Stile. Wählen Sie einfach einen Stil aus der Liste aus, um den Stil anzuwenden.

|**Stile**|**Farbschema**|
|:- |:- |
|Standard|Silber|
|Bunt1|Rose|
|Bunt2|Blau|
|Profi1|Cyan|
|Profi2|Wieder Cyan|
|Traditionell1|Dunkel|
|Traditionell2|Grau|
|Brauch|Angepasst|
Wenn ein bestimmter Stil ausgewählt wird, ändert er das gesamte Erscheinungsbild des GridWeb-Steuerelements. Entwickler können einen voreingestellten Stil auswählen, der während der Entwurfszeit auf Grid angewendet werden soll, aber diese Aufgabe kann auch zur Laufzeit mit dem flexiblen API von Aspose.Cells.GridWeb ausgeführt werden.

{{% alert color="primary" %}} 

Aspose.Cells. Das GridWeb-Steuerelement wird durch die GridWeb-Klasse dargestellt.

{{% /alert %}} 

So wählen Sie einen voreingestellten Stil aus:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Wählen Sie einen voreingestellten Stil aus, der auf das Steuerelement angewendet werden soll.

Das GridWeb-Steuerelement stellt die PresetStyle-Eigenschaft bereit, der Entwickler jeden gewünschten voreingestellten Stil zuweisen können.

 Die Ausgabe des folgenden Code-Snippets ist unten dargestellt.

**GridWeb-Steuerelement mit darauf angewendetem Colorful1-Stil** 

![todo: Bild_alt_Text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Kopfleistenstil**
Wenn Sie sich das GridWeb-Steuerelement ansehen, werden Sie zwei Kopfleisten bemerken. Eine für Spalten (also A, B, C, D etc.) und eine für Zeilen (also 1, 2, 3, 4 etc.). Aspose.Cells.GridWeb ermöglicht es Entwicklern, das Erscheinungsbild dieser Kopfleisten zu steuern. Entwickler können den Stil von Kopfleisten entweder zur Entwurfszeit oder zur Laufzeit festlegen.

{{% alert color="primary" %}} 

Das GridWeb-Steuerelement stellt die HeaderBarStyle-Eigenschaft bereit, die einen Stil auf beide Kopfleisten des Steuerelements anwendet.

{{% /alert %}} 

 Die Ausgabe des Beispielcodes unten wird hier gezeigt.

**Modifizierter Stil der Kopfleiste** 

![todo: Bild_alt_Text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Registerkartenleistenstil**
 Es ist möglich, den Stil der Registerkartenleiste festzulegen.

**Modifizierte Stile aktiver und nicht aktiver Registerkartenleisten** 

![todo: Bild_alt_Text](apply-styles-to-gridweb_3.png)

In der obigen Abbildung ist Sheet4 die aktive Registerkarte, daher unterscheidet sich ihr Erscheinungsbild von den anderen Registerkarten, wie im folgenden Beispielcode definiert.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Wiederverwendbare benutzerdefinierte Stildatei**
Aspose.Cells. GridWeb unterstützt auch das Beibehalten seiner Darstellungs- oder Stileinstellungen in einer Datei. Wenn Sie alle Darstellungseigenschaften des GridWeb-Steuerelements festgelegt haben, können Sie diese Eigenschaften oder Einstellungen in einer Datenträgerdatei speichern. Dieser Ansatz ist sehr nützlich für Entwickler, um Zeit und Mühe zu sparen, indem sie ihre alten Stilkonfigurationen aus einer Stildatei wiederverwenden, anstatt alle Stil- (oder Darstellungs-)Eigenschaften des Steuerelements einzeln festzulegen.
### **Stildatei speichern**
Nachdem Sie die Stileigenschaften festgelegt haben, können Sie Ihre Stilkonfigurationseinstellungen in Form einer XML-Datei speichern (weil diese Stildatei als XML-Datei gespeichert wird), indem Sie die SaveCustomStyleFile-Methode des GridWeb-Steuerelements aufrufen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Die gespeicherte Stildatei ist im XML-Format, sodass Entwickler diese Datei bei Bedarf auch mit einem beliebigen Texteditor bearbeiten können.

{{% /alert %}} 
### **Style-Datei wird geladen**
Um Stileinstellungen aus einer vorhandenen Stildatei auf das GridWeb-Steuerelement anzuwenden, können Entwickler den Pfad der Stildatei auf die CustomStyleFileName-Eigenschaft des Steuerelements festlegen. Aber bevor Sie dies tun, müssen Sie die PresetStyle-Eigenschaft des Steuerelements auf Custom setzen. Dies liegt daran, dass diese Stildatei benutzerdefinierte Stilinformationen enthält, die bereits von einem Entwickler definiert wurden.

{{% alert color="primary" %}} 

Es ist auch möglich, Stildateien mit Aspose.Cells.GridWeb Designer zu laden oder zu speichern.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Das Laden der Stildatei in das GridWeb-Steuerelement wirkt sich nicht auf die Formatierungseinstellungen der Zellen des Steuerelements aus.

{{% /alert %}} 
### **Standardformat der XML-Stilvorlage**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

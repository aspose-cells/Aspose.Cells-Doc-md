---
title: Stile auf GridWeb anwenden
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, Stil, Stile
description: Dieser Artikel zeigt, wie man Stile in GridWeb anwendet oder einstellt.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb hat sein eigenes Standardaussehen, aber es ist möglich, sein Erscheinungsbild zu ändern. Aspose.Cells.GridWeb bietet mehrere Eigenschaften, um Entwicklern die vollständige Kontrolle über sein Aussehen zu ermöglichen. Dieses Thema erörtert einige dieser Eigenschaften.

{{% /alert %}} 
## **Anwendung voreingestellter oder benutzerdefinierter Stile auf Aspose.Cells.GridWeb**
### **Voreingestellte Stile**
Um den Aufwand der Entwickler zu reduzieren, bietet Aspose.Cells.GridWeb einige voreingestellte Stile an. Wählen Sie einfach einen Stil aus der Liste aus, um ihn anzuwenden.

|**Stile**|**Farbschema**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Wenn ein bestimmter Stil ausgewählt ist, ändert er das gesamte Erscheinungsbild des GridWeb-Steuer elements. Entwickler können einen voreingestellten Stil auswählen, der zur Entwurfszeit auf das Raster angewendet wird, diese Aufgabe kann jedoch auch zur Laufzeit mit der flexiblen API von Aspose.Cells.GridWeb durchgeführt werden.

{{% alert color="primary" %}} 

Das Aspose.Cells.GridWeb-Steuer element wird durch die GridWeb-Klasse repräsentiert.

{{% /alert %}} 

Um einen voreingestellten Stil auszuwählen:

1. Fügen Sie dem Webformular das Aspose.Cells.GridWeb-Steuer element hinzu.
1. Wählen Sie einen voreingestellten Stil aus, der auf das Steuer element angewendet werden soll.

Die GridWeb-Steuerung bietet die Eigenschaft PresetStyle, der Entwickler einen beliebigen voreingestellten Stil zuweisen können.

Der Ausgang des folgenden Code-Schnipsels wird unten angezeigt. 

**GridWeb-Steuerung mit angewendetem Colorful1-Stil** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Kopfzeilen-Stil**
Wenn Sie das GridWeb-Steuer element betrachten, werden Sie feststellen, dass es zwei Kopfzeilen gibt. Eine für Spalten (d.h. A, B, C, D usw.) und eine andere für Zeilen (d.h. 1, 2, 3, 4 usw.). Aspose.Cells.GridWeb ermöglicht es Entwicklern, das Aussehen dieser Kopfzeilen zu steuern. Entwickler können das Aussehen der Kopfzeilen entweder zur Entwurfszeit oder zur Laufzeit festlegen.

{{% alert color="primary" %}} 

Die GridWeb-Steuerung bietet die Eigenschaft HeaderBarStyle, die einen Stil auf beide Kopfzeilen der Steuerung anwendet.

{{% /alert %}} 

Der Ausgang des unten stehenden Beispielcodes wird hier angezeigt. 

**Geänderter Stil der Kopfzeile** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Tab-Leistenstil**
Es ist möglich, den Stil der Registerkarte zu ändern. 

**Geänderte Stile der aktiven und inaktiven Registerkarten** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

Im obigen Bild ist Sheet4 die aktive Registerkarte, daher unterscheidet sich ihr Erscheinungsbild von den anderen Registerkarten, wie im Beispielcode unten definiert.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Wiederverwendbare benutzerdefinierte Stil-Datei**
Aspose.Cells.GridWeb unterstützt auch die Speicherung ihrer Erscheinungs- oder Stil einstellungen in einer Datei. Wenn Sie alle Erscheinungseigenschaften des GridWeb-Steuer elements festgelegt haben, können Sie diese Eigenschaften oder Einstellungen in einer Datei auf dem Datenträger speichern. Dieser Ansatz ist sehr nützlich für Entwickler, um Zeit und Mühe zu sparen, indem sie ihre alten Stil konfigurationen aus einer Stil datei wiederverwenden anstatt alle Stil (oder Erscheinungs-) eigenschaften des Steuer elements einzeln festzulegen.
### **Stildatei speichern**
Nachdem Sie die Stil eigenschaften festgelegt haben, können Sie Ihre Stil konfigurationseinstellungen in Form einer XML-Datei (weil die Stil datei als XML-Datei gespeichert ist) speichern, indem Sie die Methode SaveCustomStyleFile des GridWeb-Steuer elements aufrufen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Die gespeicherte Stil datei liegt im XML-Format vor, so dass Entwickler diese Datei bei Bedarf auch mit einem Texteditor bearbeiten können.

{{% /alert %}} 
### **Stil-Datei laden**
Um style-Einstellungen aus einer bestehenden Style-Datei auf das GridWeb-Steuerelement anzuwenden, können Entwickler den Pfad der Style-Datei auf die CustomStyleFileName-Eigenschaft des Steuerlements setzen. Bevor dies geschieht, muss jedoch die PresetStyle-Eigenschaft des Steuerelements auf Benutzerdefiniert gesetzt werden. Dies liegt daran, dass die Style-Datei benutzerdefinierte Style-Informationen enthält, die bereits von einem Entwickler definiert wurden.

{{% alert color="primary" %}} 

Es ist auch möglich, eine Style-Datei mit dem Aspose.Cells.GridWeb Designer zu laden oder zu speichern.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Das Laden einer Stil-Datei in das GridWeb-Steuerelement hat keine Auswirkungen auf die Formatierungseinstellungen der Zellen des Steuerelements.

{{% /alert %}} 
### **Standardformat der XML-Style-Vorlage**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}

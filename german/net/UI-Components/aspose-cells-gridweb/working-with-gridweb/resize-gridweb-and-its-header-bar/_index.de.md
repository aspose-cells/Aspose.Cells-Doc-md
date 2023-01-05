---
title: Ändern Sie die Größe von GridWeb und seiner Kopfleiste
type: docs
weight: 30
url: /de/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[GridWeb zum Webformular hinzufügen](/cells/de/net/add-gridweb-to-web-form/), erläuterte die Größenänderung des Aspose.Cells.GridWeb-Steuerelements mithilfe von WYSIWYG. In diesem Artikel wird erläutert, wie Sie dasselbe tun, jedoch zur Laufzeit mit dem Aspose.Cells.GridWeb API. Außerdem wird erläutert, wie Sie die Größe der Kopfleisten des Aspose.Cells.GridWeb-Steuerelements ändern, um ihre Daten leichter lesbar zu machen.

{{% /alert %}} 
## **Breite und Höhe von Aspose.Cells.GridWeb ändern**
Das Ändern der Breite und Höhe des Aspose.Cells.GridWeb-Steuerelements ist eine einfache, aber wichtige Funktion. Das Aspose.Cells.GridWeb-Steuerelement wird durch die GridWeb-Klasse in API dargestellt. Um die Breite und Höhe des GridWeb-Steuerelements zu ändern, verwenden Sie einfach seine Breiten- und Höheneigenschaften.

{{% alert color="primary" %}} 

Breite und Höhe des Steuerelements können in Pixeln oder Punkten angegeben werden.

{{% /alert %}} 

Die Ausgabe des folgenden Code-Snippets ist unten dargestellt.

**Geänderte Breite und Höhe des GridWeb-Steuerelements** 

![todo: Bild_alt_Text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Breite und Höhe der Kopfleiste ändern**
Aspose.Cells. Das GridWeb-Steuerelement enthält zwei Kopfleisten wie folgt:

- Obere Kopfleiste, diese Kopfleiste repräsentiert Spalten als A , B , C , D usw.
- Linke Kopfleiste, diese Kopfleiste repräsentiert Zeilen als 1 , 2 , 3 , 4 usw.

Diese beiden Kopfleisten sind unten dargestellt.

**Kopfleisten** 

![todo: Bild_alt_Text](resize-gridweb-and-its-header-bar_2.png)

Ändern Sie die Höhe der oberen Kopfleiste und die Breite der linken Kopfleiste mit den Eigenschaften HeaderBarHeight und HeaderBarWidth des GridWeb-Steuerelements. Die folgende Abbildung zeigt die Ausgabe des folgenden Codebeispiels.

**Breite und Höhe der Kopfleiste geändert** 

![todo: Bild_alt_Text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}

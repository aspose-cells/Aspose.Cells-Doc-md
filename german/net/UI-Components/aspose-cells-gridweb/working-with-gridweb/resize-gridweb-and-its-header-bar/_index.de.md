---
title: GridWeb und seine Headerleiste neu dimensionieren
type: docs
weight: 30
url: /de/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb, anpassen
description: Dieser Artikel zeigt, wie man in GridWeb anpasst.
---

{{% alert color="primary" %}} 

[GridWeb zu Web-Formular hinzufügen](/cells/de/net/aspose-cells-gridweb/add-gridweb-to-web-form/), behandelt die Größenänderung des Aspose.Cells.GridWeb-Steuerelements mit WYSIWYG. In diesem Artikel wird erläutert, wie Sie dasselbe zur Laufzeit mithilfe der Aspose.Cells.GridWeb-API tun können. Es wird auch erklärt, wie Sie die Kopfzeilenleisten des Aspose.Cells.GridWeb-Steuerelements anpassen, um die Daten leichter lesbar zu machen.

{{% /alert %}} 
## **Ändern von Breite & Höhe von Aspose.Cells.GridWeb**
Die Änderung der Breite und Höhe des Aspose.Cells.GridWeb-Steuerelements ist eine einfache, aber wichtige Funktion. Das Aspose.Cells.GridWeb-Steuerelement wird durch die GridWeb-Klasse in der API dargestellt. Um die Breite und Höhe des GridWeb-Steuerelements zu ändern, verwenden Sie einfach seine Breiten- und Höheneigenschaften.

{{% alert color="primary" %}} 

Die Breite und
Höhe des Steuerelements können in Pixel oder Punkten definiert werden.

{{% /alert %}} 

Der Ausgabewert des folgenden Code-Schnipsels wird unten angezeigt.

**Geänderte Breite und Höhe des GridWeb-Steuerelements** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Ändern von Breite & Höhe der Kopfleiste**
Das Aspose.Cells.GridWeb-Steuerelement enthält zwei Kopfleisten wie folgt:

- Obere Kopfzeile, diese Kopfzeile repräsentiert Spalten als A, B, C, usw.
- Linke Kopfzeile, diese Kopfzeile repräsentiert Zeilen als 1, 2, 3, 4, usw.

Beide dieser Kopfleisten sind unten aufgeführt.

**Kopfleisten** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Ändern Sie die Höhe der oberen Kopfzeile und die Breite der linken Kopfzeile mithilfe der Eigenschaften HeaderBarHeight und HeaderBarWidth des GridWeb-Steuerelements. Die Abbildung unten zeigt die Ausgabe des nachfolgenden Codebeispiels.

**Geänderte Kopfzeilenbreite und -höhe** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}

---
title: Standardschriftart und Schriftfarbe des GridDesktop
type: docs
weight: 70
url: /de/net/default-font-and-font-color-of-the-griddesktop/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Sie die Standardschriftart und -farbe des GridDesktop ändern. Verwenden Sie dazu bitte die beiden folgenden Eigenschaften. Auf diese Eigenschaften können Sie je nach Bedarf zur Entwurfszeit oder zur Laufzeit zugreifen.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Ändern Sie die Standardschriftart und -farbe zur Entwurfszeit**
Der folgende Screenshot zeigt, wie Sie die Standardschriftart und Schriftfarbe von GridDesktop zur Entwurfszeit ändern.

![todo: Bild_alt_Text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Standardschriftart und Schriftfarbe zur Laufzeit ändern**
Der folgende Beispielcode erläutert, wie die Standardschriftart und die Schriftfarbe von GridDesktop zur Laufzeit geändert werden.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

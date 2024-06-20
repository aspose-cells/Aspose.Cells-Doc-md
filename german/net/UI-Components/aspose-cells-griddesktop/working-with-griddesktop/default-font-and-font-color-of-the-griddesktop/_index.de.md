---
title: Standard Schriftart und Schriftfarbe des GridDesktop
type: docs
weight: 70
url: /de/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop, Schriftart, Farbe
description: Dieser Artikel stellt die Standard Schriftart und Schriftfarbe in GridDesktop vor.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie die Standard-Schriftart und Schriftfarbe des GridDesktop ändern. Verwenden Sie hierfür bitte die folgenden beiden Eigenschaften. Sie können je nach Bedarf auf diese Eigenschaften zur Entwurfszeit oder zur Laufzeit zugreifen.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Ändern der Standard-Schriftart und Schriftfarbe zur Entwurfszeit**
Der folgende Screenshot zeigt, wie die Standard-Schriftart und Schriftfarbe des GridDesktop zur Entwurfszeit geändert werden.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Ändern der Standard-Schriftart und Schriftfarbe zur Laufzeit**
Der folgende Beispielcode erklärt, wie die Standard-Schriftart und Schriftfarbe des GridDesktop zur Laufzeit geändert werden.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

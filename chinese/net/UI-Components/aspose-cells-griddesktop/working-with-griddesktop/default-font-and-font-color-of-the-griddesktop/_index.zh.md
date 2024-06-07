---
title: GridDesktop的默认字体和字体颜色
type: docs
weight: 70
url: /zh/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop，字体，颜色
description: 本文介绍了GridDesktop中的默认字体和字体颜色。
---

## **可能的使用场景**
有时，您想要更改GridDesktop的默认字体和字体颜色。请使用以下两个属性来实现此目的。您可以根据需要在设计时或运行时访问这些属性。

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **在设计时更改默认字体和字体颜色**
以下截图显示了如何在设计时更改GridDesktop的默认字体和字体颜色。

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **在运行时更改默认字体和字体颜色**
以下示例代码解释了如何在运行时更改GridDesktop的默认字体和字体颜色。

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

---
title: GridDesktop 的默认字体和字体颜色
type: docs
weight: 70
url: /zh/net/default-font-and-font-color-of-the-griddesktop/
---
## **可能的使用场景**
有时，您想更改 GridDesktop 的默认字体和字体颜色。为此，请使用以下两个属性。您可以根据需要在设计时或运行时访问这些属性。

- GridDesktop.DefaultCellFont
- 网格桌面.DefaultCellFontColor
## **在设计时更改默认字体和字体颜色**
以下屏幕截图显示了如何在设计时更改 GridDesktop 的默认字体和字体颜色。

![待办事项：图像_替代_文本](default-font-and-font-color-of-the-griddesktop_1.png)
## **在运行时更改默认字体和字体颜色**
以下示例代码解释了如何在运行时更改 GridDesktop 的默认字体和字体颜色。

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

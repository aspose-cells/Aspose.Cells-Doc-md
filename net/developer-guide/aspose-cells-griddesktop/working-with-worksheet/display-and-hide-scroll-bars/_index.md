---
title: Display and Hide Scroll Bars
type: docs
weight: 140
url: /net/display-and-hide-scroll-bars/
---

{{% alert color="primary" %}} 

Scroll bars are useful for navigating the contents of spreadsheets that are wide and deep, that is, that have many rows and columns. Most applications support two types of scroll bar:

- Vertical scroll bar
- Horizontal scroll bar

Both of these are found in Microsoft Excel.

Aspose.Cell's [GridDesktop API](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.GridDesktop+namespace&linkCreation=true&fromPageId=5017753) provides horizontal and vertical scroll bars for scrolling through the contents of a worksheet. With the Aspose.Cells.GridDesktop APIs, developers can control the visibility of both of these scroll bars.

{{% /alert %}} 
## **Controlling Scroll Bar Visibility**
To control scroll bar's visibility in the GridDesktop, use the IsVerticalScrollBarVisible and IsHorizontalScrollBarVisible properties. The examples below show how to hide and show scroll bars.
### **Programming Samples: Hiding Scroll Bars**
To hide scrollbars, set the properties that control visibility to false.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}
### **Programming Samples: Making Scroll Bars Visible**
To make scrollbars visible, set the properties that control visibility to true.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
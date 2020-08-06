---
title: Custom Row and Custom Column Caption of GridDesktop Worksheet
type: docs
weight: 120
url: /net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---

## **Possible Usage Scenarios**
You can customize row and column caption of GridDesktop worksheet. Normally, row starts from 1 and column starts from A. You can change this behavior and use your own captions for rows and columns of GridDesktop worksheet. In order to change the captions of rows and columns, please implement ICustomRowCaption and ICustomColumnCaption interfaces.
## **Custom Row and Custom Column Caption of GridDesktop Worksheet**
The following sample code implements ICustomRowCaption and ICustomColumnCaption interfaces and changes the captions of rows and columns. The screenshot shows the result of the execution of this sample code for a reference.



![todo:image_alt_text](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Sample Code**
{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}

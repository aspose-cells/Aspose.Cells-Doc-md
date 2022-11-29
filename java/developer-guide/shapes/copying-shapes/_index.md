---
title: Copy Shapes between Worksheets
type: docs
weight: 250
url: /java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Sometimes, you do need to copy different pictures, charts and other drawing objects to different worksheets as per your requirement. Aspose.Cells supports copying shapes between worksheets. The charts, images and other objects are copied with the highest degree of precision.

You might try Office Automation but that has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability, speed, price, and features. In Short, there are many reasons, with the top one being that Microsoft themselves strongly recommends against Office automation from software solutions.

In this article, we create a console application, perform the copying of pictures, charts and other drawing objects between worksheets of a workbook with a few and simplest lines of code using Aspose.Cells.

This document is designed to provide the developers with a detailed understanding on how to copy shapes (pictures, charts, controls and other drawing objects) between worksheets.

{{% /alert %}}

## **Copying Shapes**

This article explains how to:

- [Copy a picture from one worksheet to another](/cells/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copy a chart from one worksheet to another](/cells/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copy controls and other drawing objects from one worksheet to another](/cells/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copying a Picture from one Worksheet to Another**

#### **Step 1: Creating a workbook with picture and chart in Microsoft Excel**

1. Created a new workbook in Microsoft Excel.
1. Add a picture on first worksheet and a chart on second worksheet.

   The following screenshots show the two template worksheets created in Microsoft Excel.

   **Worksheet “Chart” with chart**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Worksheet “Picture” with picture**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Now, copy the picture in worksheet named “Picture” to the last worksheet “Result”.

#### **Step 2: Download Aspose.Cells.Zip**

1. [Download Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Unzip it on your development computer.

   All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

#### **Step 3: Create a Project**

You can either create a project using some Java editor, for example, Eclipse or create a simple program using a NotePad.

#### **Step 4: Add Class Path**

To set a Class Path using Eclipse, please perform the following steps:

1. Extract the Aspose.Cells.jar and dom4j_1.6.1.jar from Aspose.Cells.zip.
1. Set the classpath of project in Eclipse:
1. Select your project in Eclipse and then click menus Project-Properties.
1. Select "Java Build Path" in the left side of the popup window, then select the "Libraries" tab, click "Add JARs" or "Add External JARs" to select Aspose.Cells.jar and dom4j_1.6.1.jar and add them into build paths.
1. Write application to invoke APIs of Aspose's components.

Or you may set it at runtime at DOS prompt in Windows. For example:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Step 5: Copying a picture from one worksheet to another**

Following is the code to accomplish the task. It copies a picture from the worksheet named “Picture” to the worksheet “Result”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Result Task 1:**

After executing the above code, the picture from worksheet “Picture” is now copied to the last worksheet “Result”

**Worksheet “Result” with copied picture**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Task 2: Copying a Chart from One Worksheet to Another**

#### **Step 1: Copy a chart from one worksheet to another**

Following is the actual code used by the component to accomplish the task.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Result Task 2**

After executing the above code, the chart from worksheet “Chart” is copied to the worksheet “Result”. Please see the following snap shot of resultant worksheet.

**Worksheet “Result” with copied picture and chart**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Task 3: Copying Controls and Other Drawing Objects from One Worksheet to Another**

**Worksheet “Control” with textbox and oval**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Please see the following simple steps which you need to perform to get your desired results.

#### **Step 1: Copying a worksheet between workbooks**

The following is the code used by the component to accomplish the task.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Result Task 3**

After executing the above code, the controls from the worksheet “Control” are now copied to worksheet “Result”. Please see the following snap shot of “Result”.

**Worksheet “Result” with copied textbox and oval**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Conclusion**

This article has shown how to copy different shapes like pictures, charts and other drawing objects between using Aspose.Cells. Hopefully, it will give you some insight, and you will be able to utilize these options according to your different scenarios.

Aspose.Cells can offer more flexibility than others for solutions and provides outstanding speed, efficiency and reliability to meet specific business application requirements. The results do show that Aspose.Cells has benefited from years of research, design and careful tuning.

We heartily welcome your queries, comments and suggestions in the [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).

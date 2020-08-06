---
title: Working with Background in ODS Files
type: docs
weight: 170
url: /java/working-with-background-in-ods-files/
---

# **Background in ODS Files**
Background can be added to sheets in ODS files. The background can either be a color background or graphic background. The background is not visible when the file is open but if the file is printed as PDF, the background is visible in the generated PDF. The background is also visible in the print preview dialogue.

Aspose.Cells provides the ability to read the background information and add background in ODS files.
## **Read Background Information from OSD file**
Aspose.Cells provides the [ODSPageBackground](https://apireference.aspose.com/java/cells/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [ODSPageBackground](https://apireference.aspose.com/java/cells/com.aspose.cells/ODSPageBackground) class by loading the [source ODS](https://docs.aspose.com/download/attachments/89981351/GraphicBackground.ods?version=2&modificationDate=1559420178632&api=v2) file and reading the background information. Please see the Console Output generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}
#### **Console Output**
Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER
## **Add Colored Background to ODS file**
Aspose.Cells provides the [ODSPageBackground](https://apireference.aspose.com/java/cells/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [ODSPageBackground.Color](https://apireference.aspose.com/java/cells/com.aspose.cells/odspagebackground#Color) property to add a color background to the ODS file. Please see the [output ODS](https://docs.aspose.com/download/attachments/89981351/ColoredBackground.ods?version=1&modificationDate=1559420178618&api=v2) file generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}
## **Add Graphic Background to ODS file**
Aspose.Cells provides the [ODSPageBackground](https://apireference.aspose.com/java/cells/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [ODSPageBackground.GraphicData](https://apireference.aspose.com/java/cells/com.aspose.cells/odspagebackground#GraphicData) property to add graphic background to the ODS file. Please see the [output ODS](https://docs.aspose.com/download/attachments/89981351/GraphicBackground.ods?version=2&modificationDate=1559420178632&api=v2) file generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
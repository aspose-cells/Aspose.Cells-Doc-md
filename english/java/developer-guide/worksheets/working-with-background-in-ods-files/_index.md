---
title: Working with Background in ODS Files
type: docs
weight: 170
url: /java/working-with-background-in-ods-files/
---

## **Background in ODS Files**

Background can be added to sheets in ODS files. The background can either be a color background or graphic background. The background is not visible when the file is open but if the file is printed as PDF, the background is visible in the generated PDF. The background is also visible in the print preview dialogue.

Aspose.Cells provides the ability to read the background information and add background in ODS files.

## **Read Background Information from OSD file**

Aspose.Cells provides the [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) class by loading the [source ODS](GraphicBackground.ods) file and reading the background information. Please see the Console Output generated by the code for reference.

### **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Console Output**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Add Colored Background to ODS file**

Aspose.Cells provides the [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) property to add a color background to the ODS file. Please see the [output ODS](ColoredBackground.ods) file generated by the code for reference.

### **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Add Graphic Background to ODS file**

Aspose.Cells provides the [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) class to manage background in ODS Files. The following code sample demonstrates the use of [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) property to add graphic background to the ODS file. Please see the [output ODS](GraphicBackground.ods) file generated by the code for reference.

### **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
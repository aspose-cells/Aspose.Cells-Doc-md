---
title: Add Images in Worksheet
type: docs
weight: 20
url: /java/add-images-in-worksheet/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Add Images in Worksheet**
The Picture class is available to handle images in a worksheet.

**Java**

{{< highlight java >}}
 // Get the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

// Insert a string value to a cell
worksheet.getCells().get("C2").setValue("Image");

// Set the 4th row height
worksheet.getCells().setRowHeight(3, 150);

// Set the C column width
worksheet.getCells().setColumnWidth(2, 50);

// Add a picture to the C4 cell
int index = worksheet.getPictures().add(3, 2, 3, 2, dataDir + "aspose.jpg");

// Get the picture object
Picture pic = worksheet.getPictures().get(index);

// Set the placement type
pic.setPlacement(PlacementType.FREE_FLOATING);
{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Add Images in Worksheet**
The Picture class is available to handle images in a worksheet.

**Java**

{{< highlight java >}}
 // Add picture data to this workbook.
InputStream is = new FileInputStream(dataDir + "aspose.jpg");
byte[] bytes = IOUtils.toByteArray(is);
int pictureIdx = wb.addPicture(bytes, Workbook.PICTURE_TYPE_JPEG);
is.close();

CreationHelper helper = wb.getCreationHelper();

// Create sheet
Sheet sheet = wb.createSheet();

// Create the drawing patriarch. This is the top‑level container for all shapes.
Drawing drawing = sheet.createDrawingPatriarch();

// Add a picture shape
ClientAnchor anchor = helper.createClientAnchor();

// Set top‑left corner of the picture,
// subsequent call to Picture#resize() will operate relative to it
anchor.setCol1(3);
anchor.setRow1(2);

Picture pict = drawing.createPicture(anchor, pictureIdx);

// Auto‑size picture relative to its top‑left corner
pict.resize();
{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/addimages)

{{% alert color="primary" %}} 
For more details, visit [Add Image Hyperlinks](/java/add-image-hyperlinks). 
{{% /alert %}}

{{< app/cells/assistant language="java" >}}

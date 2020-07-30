---
title : "Add Images in Worksheet" 
description : "" 
weight : 20594 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/codeinapscls-aph/worksheets/add+images+in+worksheet/
---

# Aspose.Cells for Java : Add Images in Worksheet


## Aspose.Cells - Add Images in Worksheet

`Picture` class is available to deal with Images in Worksheet

**Java**

{{< code lang="java" >}}
//Get the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Insert a string value to a cell
worksheet.getCells().get("C2").setValue("Image");

//Set the 4th row height
worksheet.getCells().setRowHeight(3, 150);

//Set the C column width
worksheet.getCells().setColumnWidth(2,50);

//Add a picture to the C4 cell
int index = worksheet.getPictures().add(3, 2, 3, 2, dataDir + "aspose.jpg");

//Get the picture object
Picture pic = worksheet.getPictures().get(index);

//Set the placement type
pic.setPlacement(PlacementType.FREE_FLOATING);

{{< /code >}}

## Apache POI SS - HSSF XSSF - Add Images in Worksheet

`Picture` class is available to deal with Images in Worksheet

**Java**

{{< code lang="java" >}}
//add picture data to this workbook.
InputStream is = new FileInputStream(dataDir + "aspose.jpg");
byte[] bytes = IOUtils.toByteArray(is);
int pictureIdx = wb.addPicture(bytes, Workbook.PICTURE_TYPE_JPEG);
is.close();

CreationHelper helper = wb.getCreationHelper();

//create sheet
Sheet sheet = wb.createSheet();

// Create the drawing patriarch.  This is the top level container for all shapes.
Drawing drawing = sheet.createDrawingPatriarch();

//add a picture shape
ClientAnchor anchor = helper.createClientAnchor();
//set top-left corner of the picture,
//subsequent call of Picture#resize() will operate relative to it
anchor.setCol1(3);
anchor.setRow1(2);
Picture pict = drawing.createPicture(anchor, pictureIdx);

//auto-size picture relative to its top-left corner
pict.resize();
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/workbook/addimages/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/addimages)

For more details, visit [Add Image Hyperlinks](http://docs.aspose.com:8082/docs/display/cellsjava/Add+Image+Hyperlinks).


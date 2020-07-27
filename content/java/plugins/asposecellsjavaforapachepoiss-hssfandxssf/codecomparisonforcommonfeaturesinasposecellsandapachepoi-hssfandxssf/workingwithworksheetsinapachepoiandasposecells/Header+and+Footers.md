+++
title = "Header and Footers" 
description = "" 
weight = 20598 
+++

Aspose.Cells for Java : Header and Footers  

# Aspose.Cells for Java : Header and Footers


## Aspose.Cells - Header and Footers

The PageSetup class provides method setHeader for adding a header and setFooter for adding a footer to a worksheet. The script is used as an argument for all the above mentioned methods. It represents the script to be used for header or footer.

**Header**

**Java**

{{< code lang="java" >}}
//Obtaining the reference of the PageSetup of the worksheet
PageSetup pageSetup = workbook.getWorksheets().get(0).getPageSetup();

//Setting worksheet name at the left  header
pageSetup.setHeader(0, "&A");

//Setting current date and current time at the central header
//and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

//Setting current file name at the right header and changing the font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");
{{< /code >}}

**Footer**

**Java**

{{< code lang="java" >}}
//Setting a string at the left footer and changing the font of the footer
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

//Setting picture at the central footer
pageSetup.setFooter(1, "&G");

FileInputStream fis = new FileInputStream("data/footer.png");
byte[] picData = new byte[fis.available()];
fis.read(picData);
pageSetup.setFooterPicture(1, picData);
fis.close();

//Setting the current page number and page count at the right footer
pageSetup.setFooter(2, "&Pof&N");
{{< /code >}}

## Apache POI SS - HSSF XSSF - Header and Footers

`Header` class is available to adjust header in spreadsheets.

**Java**

Header header = sheet.getHeader();header.setCenter("Center Header");header.setLeft("Left Header");header.setRight(HSSFHeader.font("Stencil-Normal", "Italic") +                HSSFHeader.fontSize((short) 16) + "Right w/ Stencil-Normal Italic font and size 16");

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/headerandfooter/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/headerandfooter)

For more details, visit [Setting Headers and Footers](http://docs.aspose.com:8082/docs/display/cellsjava/Setting+Headers+and+Footers).


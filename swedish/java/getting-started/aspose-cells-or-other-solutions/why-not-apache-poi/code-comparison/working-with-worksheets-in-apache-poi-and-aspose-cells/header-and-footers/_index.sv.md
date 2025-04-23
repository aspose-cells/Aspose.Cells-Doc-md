---
title: Rubrik och sidfot
type: docs
weight: 60
url: /sv/java/header-and-footers/
---

## **Aspose.Cells - Rubrik och sidfot**
Klassen PageSetup tillhandahåller metoden setHeader för att lägga till en header och setFooter för att lägga till en sidfot i ett arbetsblad. Skriptet används som ett argument för alla ovan nämnda metoder. Det representerar skriptet som ska användas för header eller footer.

**Rubrik**

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.getWorksheets().get(0).getPageSetup();

//Setting worksheet name at the left  header

pageSetup.setHeader(0, "&A");

//Setting current date and current time at the central header

//and changing the font of the header

pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

//Setting current file name at the right header and changing the font of the header

pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

{{< /highlight >}}

**Sidfot**

**Java**

{{< highlight java >}}

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

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Rubrik och sidfot**
Rubrik-klassen finns tillgänglig för att justera rubriken i kalkylblad.

**Java**

{{< highlight java >}}

 Header header = sheet.getHeader();

header.setCenter("Center Header");

header.setLeft("Left Header");

header.setRight(HSSFHeader.font("Stencil-Normal", "Italic") +

                HSSFHeader.fontSize((short) 16) + "Right w/ Stencil-Normal Italic font and size 16");

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/headerandfooter)

{{% alert color="primary" %}} 

För mer information, besök [Inställning av rubriker och sidfötter](/java/setting-headers-and-footers)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: Cells'de Yeni Hat
type: docs
weight: 30
url: /tr/java/new-line-in-cells/
---
## **Aspose.Cells - Cells'de Yeni Hat**
Bir hücredeki metnin okunabilmesini sağlamak için açık satır sonları ve metin kaydırma uygulanabilir. Metin kaydırma, bir hücrede bir satırı birkaç satıra dönüştürür; bu açık satır sonları, tam olarak istediğiniz yerde aralara konur.

Metni bir hücreye kaydırmak için Style.setTextWrapped yöntemini kullanın.

**Java**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Cells'de Yeni Satır**
Sarılmış metin için CellStyle.setWrapText doğru olmalıdır.

**Java**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Satır Sonları ve Metin Sarma](/java/line-breaks-and-text-wrapping).

{{% /alert %}}

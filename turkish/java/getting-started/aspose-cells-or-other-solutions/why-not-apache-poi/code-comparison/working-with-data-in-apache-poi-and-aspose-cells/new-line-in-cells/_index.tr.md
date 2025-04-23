---
title: Hücrelerde Yeni Satır
type: docs
weight: 30
url: /tr/java/new-line-in-cells/
---

## **Aspose.Cells - Hücrelerde Yeni Satır**
Hücredeki metnin okunabilmesi için, açık satır sonları ve metin kaydırma uygulanabilir. Metin kaydırma, hücredeki bir satırı birden fazla satıra dönüştürür, açık satır sonları istediğiniz yerde kesmek için kullanılır.

Bir hücrede metni kaydırmak için, Style.setTextWrapped yöntemini kullanın.

**Java**

{{< highlight java >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Hücrelerde Yeni Satır**
CellStyle.setWrapText, çevrilmiş metin için true olmalıdır.

**Java**

{{< highlight java >}}

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
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Satır Kesmeleri ve Metin Kaydırma](/java/line-breaks-and-text-wrapping) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

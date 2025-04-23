---
title: سطر جديد في الخلايا
type: docs
weight: 30
url: /ar/java/new-line-in-cells/
---

## **Aspose.Cells - سطر جديد في الخلايا**
لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.

لتغليف النص في الخلية، استخدم طريقة setTextWrapped في النمط.

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
## **Apache POI SS - HSSF XSSF - سطر جديد في الخلايا**
يجب أن يكون CellStyle.setWrapText true للنص الملفوف.

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
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [كسر السطر وتفاف النص](/java/line-breaks-and-text-wrapping).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

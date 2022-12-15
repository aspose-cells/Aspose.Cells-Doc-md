---
title: الخط الجديد في Cells
type: docs
weight: 30
url: /ar/java/new-line-in-cells/
---
## **Aspose.Cells - الخط الجديد في Cells**
للتأكد من إمكانية قراءة النص في الخلية ، يمكن تطبيق فواصل أسطر واضحة والتفاف النص. يحول التفاف النص سطرًا واحدًا إلى عدة سطور في خلية ، حيث يتم وضع فواصل الأسطر الصريحة في فواصل في المكان الذي تريده بالضبط.

لالتفاف نص في خلية ، استخدم الأسلوب Style.setTextWrapped.

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
## **Apache POI SS - HSSF XSSF - خط جديد في Cells**
يجب أن يكون CellStyle.setWrapText صحيحًا للنص الملتف.

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
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / datahandling / newlineincells)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[فواصل الأسطر وتغليف النص](/java/line-breaks-and-text-wrapping).

{{% /alert %}}

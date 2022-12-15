---
title: تعيين عناوين الطباعة
type: docs
weight: 10
url: /ar/java/set-print-titles/
---
## **Aspose.Cells - تعيين عناوين الطباعة**
Aspose.Cells يسمح لك بتعيين رؤوس الصفوف والأعمدة لتكرارها على كل صفحات ورقة العمل المطبوعة. للقيام بذلك ، استخدم ملف[اعداد الصفحة](/java/pagesetup)class'setPrintTitleColumns وخصائص setPrintTitleRows.

يتم تحديد الصفوف أو الأعمدة التي سيتم تكرارها عن طريق تمرير أرقام الصفوف أو الأعمدة. على سبيل المثال ، يتم تعريف الصفوف على أنها $ 1: $ 2 ويتم تعريف الأعمدة على أنها $ A: $ B.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **تحميل كود الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ضبط خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}

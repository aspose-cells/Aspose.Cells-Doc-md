---
title: قم بتعيين عناوين الطباعة في xlsx4j
type: docs
weight: 40
url: /ar/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - تعيين عناوين الطباعة**
Aspose.Cells يسمح لك بتعيين رؤوس الصفوف والأعمدة لتكرارها على كل صفحات ورقة العمل المطبوعة. للقيام بذلك ، استخدم ملف[اعداد الصفحة](/java/PageSetup)class'setPrintTitleColumns وخصائص setPrintTitleRows.

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ضبط خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}

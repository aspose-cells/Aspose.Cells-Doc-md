---
title: تعيين عناوين الطباعة في xlsx4j
type: docs
weight: 40
url: /ar/java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - تحديد عناوين الطباعة**
تتيح Aspose.Cells لك تحديد رءوس الصف والعمود لتكرارها على جميع الصفحات لورقة العمل المطبوعة. للقيام بذلك، استخدم خصائص الصفحة الشخصية للفئة [PageSetup](/java/PageSetup)'setPrintTitleColumns و setPrintTitleRows.

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

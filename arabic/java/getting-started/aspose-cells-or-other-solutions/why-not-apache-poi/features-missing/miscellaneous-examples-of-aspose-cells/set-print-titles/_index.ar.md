---
title: تعيين عناوين الطباعة
type: docs
weight: 10
url: /ar/java/set-print-titles/
---

## **Aspose.Cells - تحديد عناوين الطباعة**
تسمح Aspose.Cells لك بتحديد عوندو اسطر واعنوان اعمدة لتكرارها على جميع الصفحات من ورقة العمل المطبوعة. لفعل ذلك، استخدم `PageSetup` `setPrintTitleColumns` و `setPrintTitleRows` الخاصيات.

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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تعيين خيارات الطباعة](/cells/ar/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

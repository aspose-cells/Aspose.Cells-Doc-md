---
title: تحديد الأرقام البارزة التي يجب تخزينها في ملف Excel
type: docs
weight: 30
url: /ar/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

تخزن Aspose.Cells افتراضيًا 17 أرقامًا معنوية من القيم المزدوجة داخل ملف Excel، على عكس MS-Excel الذي يخزن فقط 15 رقمًا معنويًا. يمكنك تغيير السلوك الافتراضي لـ Aspose.Cells من 17 رقمًا معنويًا إلى 15 رقمًا معنويًا باستخدام خاصية [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**

الكود النموذجي التالي يجبر Aspose.Cells على استخدام 15 رقمًا معنويًا أثناء تخزين القيم المزدوجة داخل ملف Excel. يرجى التحقق من [ملف Excel الناتج](22774105.xlsx). قم بتغيير امتداده إلى .zip وقم بفك الضغط عنه وسترى أنه تم تخزين 15 رقمًا معنويًا فقط داخل ملف Excel. اللقطة الشاشية التالية تشرح تأثير خاصية [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) على ملف Excel الناتج.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: تحديد الارقام المهمة التي سيتم تخزينها في ملف اكسل
type: docs
weight: 20
url: /ar/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**

بشكل افتراضي ، يقوم Aspose.Cells بتخزين 17 رقمًا مهمًا من القيم المزدوجة في جداول البيانات بخلاف تطبيق Excel الذي يخزن فقط 15 رقمًا مهمًا. يمكنك تغيير السلوك الافتراضي Aspose.Cells لهذه الحالة ، أي ؛ يمكنك تغيير عدد الأرقام المعنوية من 17 إلى 15 أثناء استخدام[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)خاصية.

## **تحديد الارقام المهمة التي سيتم تخزينها في ملف اكسل**

 يفرض نموذج التعليمات البرمجية التالي Aspose.Cells لاستخدام 15 رقمًا مهمًا أثناء تخزين قيم مزدوجة داخل ملف Excel. رجاء تاكد من[ملف اكسل الناتج](23166982.xlsx) . قم بتغيير امتداده إلى .zip وفك ضغطه وسترى ، يتم تخزين 15 رقمًا مهمًا فقط داخل ملف Excel. توضح لقطة الشاشة التالية تأثير[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)الخاصية على ملف الإخراج إكسل.

![ما يجب القيام به: image_بديل_نص](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}

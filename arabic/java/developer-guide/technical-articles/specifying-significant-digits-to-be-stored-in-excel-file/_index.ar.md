---
title: تحديد الأرقام البارزة التي يجب تخزينها في ملف Excel
type: docs
weight: 20
url: /ar/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

من خلال الافتراضي، تخزن Aspose.Cells 17 أرقامًا بارزة من القيم العشرية في جداول البيانات على عكس تطبيق Excel الذي يخزن فقط 15 رقمًا بارزًا. يمكنك تغيير السلوك الافتراضي لـ Aspose.Cells لهذه الحالة، أي يمكنك تغيير عدد الأرقام البارزة من 17 إلى 15 أثناء استخدام خاصية [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits).

## **تحديد الأرقام البارزة التي يجب تخزينها في ملف Excel**

يجبر الكود العيني التالي Aspose.Cells على استخدام 15 رقمًا بارزًا أثناء تخزين القيم العشرية داخل ملف Excel. يرجى التحقق من [ملف الإكسل الناتج](23166982.xlsx). قم بتغيير الامتداد إلى .zip وفك الضغط عنه سترون، أنه تم تخزين فقط 15 رقمًا بارزًا داخل ملف الإكسل. يشرح اللقطة الشاشية التالية تأثير خاصية [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) على ملف الإكسل الناتج.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}

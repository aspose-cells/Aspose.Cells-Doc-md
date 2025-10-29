---
title: تحديد الأرقام ذات الأهمية التي يجب حفظها في ملف إكسل باستخدام Golang عبر C++
linktitle: تحديد الأرقام المهمة
type: docs
weight: 30
url: /ar/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: تعلم كيفية تحديد الأرقام ذات الأهمية التي يجب تخزينها في ملفات إكسل باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

افتراضيًا، يخزن Aspose.Cells 17 رقماً مهمًا لقيم double داخل ملف Excel، على عكس MS-Excel الذي يخزن فقط 15 رقمًا مهمًا. يمكنك تغيير سلوك الافتراضي لـ Aspose.Cells من 17 رقمًا مهمًا إلى 15 باستخدام الخاصية [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/).

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**

يوضح الكود النموذجي التالي كيف يجبر Aspose.Cells على استخدام 15 رقمًا مهمًا عند تخزين قيم double داخل ملف Excel. يرجى التحقق من ملف Excel الناتج [ملف الإخراج](22774105.xlsx). غيّر امتداده إلى .zip وفك ضغطه، وسترى أن 15 رقمًا مهمًا فقط تم تخزينها داخل ملف Excel. يوضح لقطة الشاشة التالية تأثير الخاصية [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) على ملف الإخراج.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}

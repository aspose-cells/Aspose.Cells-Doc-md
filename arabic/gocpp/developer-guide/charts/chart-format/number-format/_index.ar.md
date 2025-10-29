---
title: تعيين تنسيق رمز قيم سلسلة المخطط باستخدام Golang عبر C++
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/go-cpp/set-the-values-format-code-of-chart-series/
description: تعلم كيفية تعيين رمز تنسيق القيم لسلسلة الرسم البياني في Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية تنسيق بيانات سلسلة الرسوم البيانية الخاصة بك باستخدام رمز التنسيق المناسب، مما يتيح لك عرض بياناتك بدقة واحترافية.
keywords: Aspose.Cells for C++، سلسلة الرسوم البيانية، رمز تنسيق القيم، التنسيق، عرض البيانات، الدقة، الاحترافية.
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تعيين رمز تنسيق القيم للسلسلة باستخدام خاصية [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/). هذه الخاصية ليست مفيدة فقط للسلسلة المبنية على النطاق داخل ورقة العمل ولكنها تعمل بشكل جيد أيضًا للسلسلة التي أنشئت بمصفوفة من القيم.

## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
يضيف رمز العينة التالي سلسلة في الرسم البياني الفارغ الذي لم يكن لديه أي سلسلة من قبل. يضيف السلسلة باستخدام مصفوفة القيم. بمجرد إضافة السلسلة، يتم تنسيقها باستخدام رمز `$#،##0` باستخدام خاصية [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) ويصبح الرقم `10000` `$10,000`. تُظهر لقطة الشاشة تأثير الكود على ملف Excel التجريبي ([ملف Excel التجريبي](51740712.xlsx)) وملف Excel الناتج ([ملف Excel الناتج](51740713.xlsx)) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **الكود المثالي**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}

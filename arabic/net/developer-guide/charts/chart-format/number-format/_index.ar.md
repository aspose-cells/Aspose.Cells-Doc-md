---
title: تعيين كود تنسيق القيم لسلسلة الرسم البياني
description: تعلم كيفية تعيين كود تنسيق القيم لسلسلة الرسم البياني في Aspose.Cells for .NET. سيساعدك دليلنا في فهم كيفية تنسيق بيانات سلسلة الرسم البياني باستخدام الكود المناسب، مما يتيح لك تقديم بياناتك بدقة واحترافية.
keywords: Aspose.Cells for .NET، سلسلة الرسم البياني، كود تنسيق القيم، تنسيق، عرض البيانات، دقة، احترافية.
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/net/set-the-values-format-code-of-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تعيين كود تنسيق القيم لسلسلة الرسم البياني باستخدام خاصية [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). هذه الخاصية مفيدة للسلاسل المعتمدة على المدى داخل ورقة العمل وأيضًا تعمل بشكل جيد للسلاسل التي تم إنشاؤها بمجموعة من القيم.
## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
يضيف الكود النموذجي التالي سلسلة في الرسم البياني الفارغ الذي لا توجد لديه سلاسل قبل ذلك. يقوم بإضافة السلسلة باستخدام مجموعة من القيم. بمجرد إضافة السلسلة، يتم تنسيقها بالكود $#,##0 باستخدام خاصية [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)  ويصبح الرقم 10000 $10,000. يظهر تأثير الكود على [ملف Excel نموذجي](51740712.xlsx) و [ملف Excel الناتج](51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}

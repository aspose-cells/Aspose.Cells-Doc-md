---
title: تعيين كود تنسيق القيم لسلسلة الرسم البياني
description: تعلم كيفية تعيين كود تنسيق القيم لسلسلة الرسم البياني في Aspose.Cells for Java. سيساعدك دليلنا على فهم كيفية تنسيق بيانات سلسلة الرسم الخاصة بك باستخدام رمز التنسيق المناسب، مما يتيح لك تقديم بياناتك بدقة واحترافية.
keywords: Aspose.Cells for Java، سلسلة الرسم البياني، رمز تنسيق القيم، التنسيق، عرض البيانات، دقة، احترافية.
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/java/set-the-values-format-code-of-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تعيين كود تنسيق القيم لسلسلة الرسم البياني باستخدام طريقة  [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) . هذه الطريقة ليست مفيدة فقط للسلسلة التي تستند على المدى داخل ورقة العمل ولكنها تعمل أيضًا بشكل جيد للسلاسل التي تم إنشاؤها بمجموعة من القيم.
## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
الشيفرة المصدرية العينية التالية تُضيف سلسلة في الرسم البياني الفارغ الذي ليس له سلاسل من قبل. تُضيف السلسلة باستخدام مصفوفة القيم. بمجرد أن تُضاف السلسلة، يتم تنسيقها بالشيفرة $#,##0 باستخدام الأسلوب [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) وبهذا يصبح الرقم 10000 هو $10,000. يوضح اللقطة الشاشية تأثير الشيفرة على [ملف إكسل مثالي](51740712.xlsx) و [ملف إكسل الناتج](51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}

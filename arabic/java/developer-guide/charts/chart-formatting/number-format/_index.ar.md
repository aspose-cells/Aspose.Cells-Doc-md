---
title: قم بتعيين رمز تنسيق القيم لسلسلة المخططات
description: تعرف على كيفية تعيين رمز تنسيق القيم لسلسلة المخططات في Aspose.Cells for Java. سيساعدك دليلنا على فهم كيفية تنسيق بيانات سلسلة المخططات الخاصة بك باستخدام رمز التنسيق المناسب، مما يسمح لك بتقديم بياناتك بدقة واحترافية.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: تنسيق الرقم
type: docs
weight: 100
url: /ar/java/set-the-values-format-code-of-chart-series/
---
##  **سيناريوهات الاستخدام المحتملة**
يمكنك تعيين رمز تنسيق القيم لسلسلة المخططات باستخدام[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) طريقة. هذه الطريقة ليست مفيدة فقط للسلسلة التي تعتمد على النطاق الموجود داخل ورقة العمل ولكنها تعمل أيضًا بشكل جيد مع السلسلة التي تم إنشاؤها باستخدام مجموعة من القيم.
##  **قم بتعيين رمز تنسيق القيم لسلسلة المخططات**
 يضيف نموذج التعليمات البرمجية التالي سلسلة في المخطط الفارغ الذي لم يكن له سلسلة من قبل. ويضيف السلسلة باستخدام مجموعة من القيم. بمجرد إضافة السلسلة، يقوم بتنسيقها باستخدام الكود $#,##0 باستخدام ملف[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) الطريقة والرقم 10000 يصبح 10000 دولار. توضح لقطة الشاشة تأثير الكود على[عينة من ملف إكسل](51740712.xlsx) و[إخراج ملف إكسل](51740713.xlsx) بعد التنفيذ.

![ما يجب القيام به:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}

---
title: تحديد عدد الصفحات المولدة  تحويل Excel إلى PDF
type: docs
weight: 180
url: /ar/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: تعلم كيفية تقييد عدد الصفحات التي يتم إنشاؤها أثناء عرض ملف إكسل إلى PDF باستخدام Aspose.Cells لبيثون via .NET API
keywords: تقييد عدد الصفحات التي يتم إنشاؤها أثناء عرض ملف إكسل إلى PDF بواسطة Python, تقييد عدد الصفحات التي تم إنشاؤها أثناء حفظ إكسل إلى PDF باستخدام Python, تعيين عدد الصفحات التي تم إنشاؤها أثناء تحويل إكسل إلى PDF باستخدام Python, التحكم في عدد الصفحات التي تم إنشاؤها لملف PDF في Python
---

{{% alert color="primary" %}}

أحيانًا، ترغب في طباعة مدى صفحات إلى ملف PDF. تتمتع Aspose.Cells لبيثون via .NET بالقدرة على وضع حد لعدد الصفحات التي يتم إنشاؤها عند تحويل جدول بيانات Excel إلى تنسيق ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

إذا كانت جدول البيانات يحتوي على صيغ، فمن الأفضل أن تقوم باستدعاء طريقة [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل عرضها في صيغة PDF. يجب القيام بذلك لضمان إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في ملف الإخراج.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

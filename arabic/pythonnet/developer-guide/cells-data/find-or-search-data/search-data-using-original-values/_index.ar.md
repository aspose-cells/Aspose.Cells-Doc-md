---
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 380
url: /ar/python-net/search-data-using-original-values/
description: تعلم كيفية البحث عن البيانات باستخدام القيم الأصلية من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel ، البحث عن البيانات باستخدام القيم الأصلية في Python ، العثور على البيانات باستخدام القيم الأصلية في Python ، البحث عن البيانات بواسطة القيم الأصلية في Python ، العثور على البيانات بواسطة القيم الأصلية في Python
---

{{% alert color="primary" %}}

بعض الأحيان يتم إخفاء قيمة البيانات لأنها مهيأة بطريقة ما. على سبيل المثال ، نفترض أن الخلية D4 تحتوي على الصيغة =Sum(A1:A2) وقيمتها 20 لكنها تم تهيئتها على شكل --- ، ثم يتم إخفاء القيمة 20 ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك ، يمكنك العثور عليها باستخدام Aspose.Cells for Python via .NET باستخدام [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype).

{{% /alert %}}

الشيفرة العينية التالية توضح النقطة السابقة. إنها تجد الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype). يرجى قراءة التعليقات داخل الشيفرة لمزيد من المعلومات.

## كود Python للبحث عن البيانات باستخدام القيم الأصلية

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}

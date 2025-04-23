---
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 380
url: /ar/net/search-data-using-original-values/
description: تعلم كيفية البحث عن البيانات باستخدام القيم الأصلية من خلال Aspose.Cells for .NET API.
keywords: البحث عن البيانات باستخدام القيم الأصلية, العثور على البيانات باستخدام القيم الأصلية, البحث عن البيانات حسب القيم الأصلية, العثور على البيانات حسب القيم الأصلية
---

{{% alert color="primary" %}}

أحيانًا يكون قيمة البيانات مخفية لأنها مهيأة بطريقة ما. على سبيل المثال، لنفترض أن الخلية D4 لديها صيغة =Sum(A1:A2) وقيمتها 20 ولكنها مهيأة كما ---، عندها تكون القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك، يمكنك العثور عليها باستخدام Aspose.Cells باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype).

{{% /alert %}}

الشيفرة العينية التالية توضح النقطة السابقة. إنها تجد الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). يرجى قراءة التعليقات داخل الشيفرة لمزيد من المعلومات.

## شفرة C# للبحث عن البيانات باستخدام القيم الأصلية

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

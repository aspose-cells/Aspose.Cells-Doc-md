---
title: إدراج أو حذف الصفوف في ورقة عمل Excel
type: docs
weight: 20
url: /ar/net/insert-or-delete-rows-in-an-excel-worksheet/
description: يوفر هذا المقال الرمز C# لإدراج وحذف الصفوف في ورقة عمل Excel
keywords: c# إدراج أو حذف الصفوف في ورقة عمل الإكسل، c# إدراج أو حذف الصفوف في إكسل، c# إدراج الصفوف في إكسل، c# حذف الصفوف في إكسل، إدراج أو حذف الصفوف في ورقة العمل في إكسل باستخدام c#، إدراج أو حذف الصفوف في إكسل بواسطة c#، إدراج الصفوف في إكسل بواسطة c#، حذف الصفوف في إكسل بواسطة c#
---

{{% alert color="primary" %}}

عند إنشاء ورقة عمل جديدة أو العمل مع ورقة عمل موجودة، قد تحتاج في بعض الأوقات إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. في أوقات أخرى، قد تحتاج إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.

{{% /alert %}}

تقدم Aspose.Cells طريقتين لإدراج الصفوف وحذفها: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) و [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). تم تحسين هذه الطرق لتحقيق أداء ممتاز ولإنجاز المهمة بسرعة كبيرة جدًا.

لإدراج أو إزالة عدد من الصفوف، نوصي دائمًا باستخدام ال[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) و ال[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) بدلاً من استخدام ال[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) أو ال[**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) في حلقة.

تعمل Aspose.Cells بنفس الطريقة التي يعمل بها برنامج Microsoft Excel. عند إضافة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأسفل ولليمين. وعند إزالة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في ورقات العمل والخلايا الأخرى عند إضافة أو إزالة الصفوف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

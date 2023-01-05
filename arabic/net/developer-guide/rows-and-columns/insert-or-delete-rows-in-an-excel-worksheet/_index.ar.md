---
title: قم بإدراج أو حذف صفوف في ورقة عمل Excel
type: docs
weight: 20
url: /ar/net/insert-or-delete-rows-in-an-excel-worksheet/
description: توفر هذه المقالة رمز C# لإدراج الصفوف وحذفها في ورقة عمل Excel
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

عند إنشاء ورقة عمل جديدة ، أو العمل باستخدام ورقة عمل موجودة ، قد تحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. في أوقات أخرى ، قد تحتاج إلى حذف صفوف أو أعمدة من مواضع محددة في ورقة العمل.

{{% /alert %}}

 يوفر Aspose.Cells طريقتين لإدخال الصفوف وحذفها:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) و[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). تم تحسين هذه الأساليب للأداء والقيام بالمهمة بسرعة كبيرة.

 لإدراج عدد من الصفوف أو إزالتها ، نوصيك دائمًا باستخدام ملف[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) و[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) طرق بدلاً من استخدام[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) أو[**احذف صف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)طرق في حلقة.

يعمل Aspose.Cells بنفس طريقة عمل Microsoft Excel. عند إضافة صفوف أو أعمدة ، يتم إزاحة محتوى ورقة العمل لأسفل وإلى اليمين. عند إزالة الصفوف أو الأعمدة ، ينتقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في أوراق العمل والخلايا الأخرى عند إضافة صفوف أو إزالتها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}

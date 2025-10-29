---
title: إدراج أو حذف الصفوف في ورقة عمل Excel
type: docs
weight: 20
url: /ar/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: توفر هذه المقالة الكود البرمجي لإدراج وحذف الصفوف في ورقة العمل في Excel باستخدام مكتبة Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel ، إدراج أو حذف الصفوف في ورقة عمل Excel باستخدام Python ، إدراج أو حذف الصفوف في Excel باستخدام Python ، إدراج الصفوف في Excel باستخدام Python ، حذف الصفوف في Excel باستخدام Python
---

{{% alert color="primary" %}}

عند إنشاء ورقة عمل جديدة أو العمل مع ورقة عمل موجودة، قد تحتاج في بعض الأوقات إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. في أوقات أخرى، قد تحتاج إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.

{{% /alert %}}

تقدم Aspose.Cells for Python via .NET طريقتين لإدراج وحذف الصفوف: ال [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) و ال [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). تم تحسين هاتان الطريقتان لتحقيق أفضل أداء وتنفيذ المهمة بسرعة كبيرة.

لإدراج أو إزالة عدد من الصفوف، نوصي دائمًا باستخدام ال[**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) و ال[**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) بدلاً من استخدام ال[**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) أو ال[**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) في حلقة.

يعمل Aspose.Cells for Python via .NET بنفس الطريقة التي تعمل بها Microsoft Excel. عند إضافة صفوف أو أعمدة ، يتم نقل محتوى ورقة العمل لأسفل ولليمين. عند إزالة صفوف أو أعمدة ، يتم نقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في ورقات العمل والخلايا الأخرى عند إضافة أو إزالة الصفوف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

---
title: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: تعلم كيفية احتواء جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام Aspose.Cells for Python via .NET API.
keywords: احتواء جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام Python، احتواء أعمدة الورقة العمل على صفحة PDF واحدة باستخدام Python، حفظ جميع أعمدة الورقة العمل على صفحة PDF واحدة باستخدام Python، حفظ جميع الأعمدة على صفحة PDF واحدة في Python
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إنشاء ملف PDF يلائم جميع أعمدة صفحة العملية على صفحة واحدة. توفر الخاصية [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) هذه الميزة بطريقة سهلة الاستخدام جدًا. يتم التعامل مع الحسابات المعقدة مثل ارتفاع وعرض PDF الناتج داخليًا ويستند إلى البيانات في صفحة العملية.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

تضمن [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) أن تتم عرض كل الأعمدة في صفحة العملية على صفحة PDF واحدة، على الرغم من أن الصفوف قد تمتد إلى عدة صفحات اعتمادًا على البيانات في صفحة العملية.

الكود النموذجي أدناه يوضح كيفية استخدام [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) لعرض صفحة عمل كبيرة تحتوي على 100 عمود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فإن الأفضلية لاصدار [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) الأمر مباشرةً قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي ذلك إلى ضمان إعادة حساب قيم الصيغة التي تعتمد عليها، وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

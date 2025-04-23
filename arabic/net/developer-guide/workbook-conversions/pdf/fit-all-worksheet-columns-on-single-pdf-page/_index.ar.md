---
title: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إنشاء ملف PDF يلائم جميع أعمدة صفحة العملية على صفحة واحدة. توفر الخاصية [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) هذه الميزة بطريقة سهلة الاستخدام جدًا. يتم التعامل مع الحسابات المعقدة مثل ارتفاع وعرض PDF الناتج داخليًا ويستند إلى البيانات في صفحة العملية.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

تضمن [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) أن تتم عرض كل الأعمدة في صفحة العملية على صفحة PDF واحدة، على الرغم من أن الصفوف قد تمتد إلى عدة صفحات اعتمادًا على البيانات في صفحة العملية.

الكود النموذجي أدناه يوضح كيفية استخدام [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) لعرض صفحة عمل كبيرة تحتوي على 100 عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

---
title: تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام Golang عبر C++
linktitle: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل في صفحة واحدة باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان تريد إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل في صفحة واحدة. توفر خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) هذه الميزة بطريقة سهلة جدًا. يتم التعامل مع الحسابات المعقدة مثل ارتفاع وعرض ملف PDF الناتج داخليًا وتستند إلى بيانات ورقة العمل.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

تضمن [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) أن يتم عرض جميع الأعمدة في ورقة العمل في صفحة PDF واحدة، على الرغم من أن الصفوف قد تتوسع لتشغل عدة صفحات اعتمادًا على البيانات الموجودة في ورقة العمل.

يعرض الكود النموذجي أدناه كيفية استخدام خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) لعرض ورقة عمل كبيرة تحتوي على 100 عمود.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}

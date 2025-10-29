---
title: إنشاء إدخال إشارة مرجعية لورقة المخططات باستخدام Golang عبر C++
linktitle: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني
type: docs
weight: 50
url: /ar/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: تعلم كيفية إنشاء PdfBookmarkEntry لورق المخطط باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

سابقًا، كان Aspose.Cells سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) لورقة عادية. ولكن الآن يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) لورقة الرسم البياني. نظرًا لعدم وجود خلية أخرى غير الخلية A1 في رقم الرسم البياني، سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) للخلية A1 فقط.

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**

يُحمّل هذا المثال البرمجي عينة من ملف Excel ([sample Excel file](61767756.xlsx)) الذي يحتوي على أربعة أوراق. ورقتان منهما أوراق عادية والأخريين أوراق مخططات. ينشئ أربع إدخالات علامة مرجعية على النحو التالي:

- إشارة-I
- إشارة-II-Chart1
- إشارة-III
- إشارة-IV-Chart2

تظهر الصورة الملتقطة التالية [PDF المولد](61767757.pdf) بواسطة الكود النموذجي للإشارة.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}

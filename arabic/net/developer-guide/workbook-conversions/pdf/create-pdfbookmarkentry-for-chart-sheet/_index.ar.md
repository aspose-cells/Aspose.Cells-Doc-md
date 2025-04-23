---
title: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني
type: docs
weight: 50
url: /ar/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **سيناريوهات الاستخدام المحتملة**

سابقًا، كان Aspose.Cells سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) لورقة عادية. ولكن الآن يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) لورقة الرسم البياني. نظرًا لعدم وجود خلية أخرى غير الخلية A1 في رقم الرسم البياني، سيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) للخلية A1 فقط.

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**

يقوم الكود النموذجي التالي بتحميل [ملف Excel عينة](61767756.xlsx) الذي يحتوي على أربع صفحات. اثنتان منها عادية والأخرتان صفحات رسم بياني. ويقوم بإنشاء أربعة إدخالات للإشارة كما يلي

- إشارة-I
- إشارة-II-Chart1
- إشارة-III
- إشارة-IV-Chart2

تظهر الصورة الملتقطة التالية [PDF المولد](61767757.pdf) بواسطة الكود النموذجي للإشارة.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}

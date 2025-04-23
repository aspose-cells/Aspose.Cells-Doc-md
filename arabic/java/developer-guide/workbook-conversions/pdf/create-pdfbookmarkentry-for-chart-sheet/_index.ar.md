---
title: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني
type: docs
weight: 50
url: /ar/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **سيناريوهات الاستخدام المحتملة**

سابقًا، كانت Aspose.Cells تقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) لورقة عادية. ولكن الآن يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) لورقة الرسم البياني. نظرًا لعدم وجود ورقة الرسم البياني أي خلية أخرى إلا الخلية A1، فسيقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) لـ الخلية A1 فقط.

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**

الشفرة النموذجية التالية تحمل [ملف إكسل عيني](61767772.xlsx) الذي يحتوي على أربع ورقات. ورقتان منها عاديتان والأخرتان ورقتان رسم بياني. فإنه يخلق أربعة مدخلات للوسم كما يلي

- إشارة-I
- إشارة-II-Chart1
- إشارة-III
- إشارة-IV-Chart2

تُظهر اللقطة الشاشية التالية [ملف بي دي إف الناتج](61767771.pdf) الذي تم إنشاؤه بواسطة الشفرة النموذجية للرجوع إليها.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
{{< app/cells/assistant language="java" >}}

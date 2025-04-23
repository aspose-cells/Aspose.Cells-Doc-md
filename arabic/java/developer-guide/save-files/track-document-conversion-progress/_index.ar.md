---
title: تتبع تقدم تحويل الوثائق
type: docs
weight: 120
url: /ar/java/track-document-conversion-progress/
---

## **سيناريوهات الاستخدام المحتملة**

احياناً يستغرق تحويل ملفات Excel الكبيرة بعض الوقت، وخلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام تطبيقك. تدعم Aspose.Cells تتبع عملية تحويل المستند من خلال تقديم واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). توفر واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) الأساليب [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) و [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) التي يمكنك تنفيذها في الفئة المخصصة. يمكنك أيضاً التحكم في الصفحات المقتبسة كما هو موضح في الفئة المخصصة *TestPageSavingCallback*.

## **تتبع تقدم تحويل الوثائق**

الكود العيني التالي يحمل ملف Excel المصدر ويطبع تقدم تحويله في وحدة التحكم باستخدام فئة المخصصة *TestPageSavingCallback* التي تنفذ واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

فيما يلي الشيفرة لفئة الاختبار *TestPageSavingCallback* المخصصة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

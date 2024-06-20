---
title: تتبع تقدم التحويل من إكسيل إلى TIFF
type: docs
weight: 140
url: /ar/java/track-conversion-progress-of-excel-to-tiff/
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا يمكن أن يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام تطبيقك. تدعم Aspose.Cells تتبع عملية تحويل المستند من خلال تقديم واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). تقدم واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) الطرق [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs)) و [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs)) التي يمكنك تنفيذها في الفئة المخصصة. يمكنك أيضًا التحكم في الصفحات المقتبسة كما هو موضح في فئة *TestTiffPageSavingCallback* المخصصة.

## **تتبع تقدّم تحويل Excel إلى TIFF**

الكود العيني التالي يحمل ملف Excel المصدر ويطبع تقدم تحويله في وحدة التحكم باستخدام فئة *TestTiffPageSavingCallback* المخصصة التي تنفذ واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). الملف الناتج مرفق للرجوع إليه.

ملف الناتج

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

الكود التالي لصنف TestTiffPageSavingCallback المخصص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}
Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10

{{< /highlight >}}

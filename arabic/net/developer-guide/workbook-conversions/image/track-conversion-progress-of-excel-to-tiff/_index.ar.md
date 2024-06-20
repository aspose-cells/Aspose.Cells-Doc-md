---
title: تتبع تقدم التحويل من إكسيل إلى TIFF
type: docs
weight: 190
url: /ar/net/track-conversion-progress-of-excel-to-tiff/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، قد يستغرق تحويل ملفات الإكسيل الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام تطبيقك. تدعم Aspose.Cells تتبع عملية تحويل المستند من خلال توفير واجهة البرمجة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). تقدم واجهة البرمجة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) الواجهة [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) والواجهة [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) التي يمكنك تنفيذها في فئتك المخصصة. كما يمكنك أيضًا التحكم في الصفحات التي تم تقديمها كما هو موضح في فئة الاختبار *TestPageSavingCallback*.

## **تتبع تقدّم تحويل Excel إلى TIFF**

يقوم الكود العيني التالي بتحميل [ملف الإكسيل المصدر](95584311.xlsx) ويطبع تقدم التحويل في وحدة التحكم باستخدام الفئة المخصصة *TestPageSavingCallback* التي تنفذ واجهة البرمجة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). الملف الناتج الذي يتم إنشاؤه مرفق للرجوع إليه.

[Output File](95584312.tiff)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

الكود التالي لصنف TestTiffPageSavingCallback المخصص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
End saving page index 8 of pages 10</br>

{{< /highlight >}}

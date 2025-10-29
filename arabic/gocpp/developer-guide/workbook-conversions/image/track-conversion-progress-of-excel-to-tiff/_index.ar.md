---
title: تتبع تقدم تحويل Excel إلى TIFF باستخدام Golang عبر C++
linktitle: تتبع تقدم التحويل من إكسيل إلى TIFF
type: docs
weight: 190
url: /ar/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: تعلم كيفية تتبع تقدم تحويل ملفات Excel إلى تنسيق TIFF باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام التطبيق الخاص بك. يدعم Aspose.Cells تتبع تقدم تحويل المستند من خلال توفير واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). توفر واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) طرق [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) و [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا السيطرة على الصفحات التي يتم تصييرها كما هو موضح في فئة *TestPageSavingCallback* المخصصة.

## **تتبع تقدّم تحويل Excel إلى TIFF**

يعرض المثال البرمجي التالي تحميل ملف Excel المصدر (95584311.xlsx) وطباعة تقدم التحويل في وحدة التحكم باستخدام فئة *TestPageSavingCallback* التي تنفذ واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). الملف الناتج المرفق هو مرجع لك.

[Output File](95584312.tiff)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
الكود التالي لصنف TestTiffPageSavingCallback المخصص.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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

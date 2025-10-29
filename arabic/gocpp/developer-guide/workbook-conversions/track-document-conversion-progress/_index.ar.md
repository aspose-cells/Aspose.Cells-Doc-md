---
title: تتبع تقدم تحويل المستند مع Golang عبر C++
linktitle: تتبع تقدم تحويل الوثائق
type: docs
weight: 970
url: /ar/go-cpp/track-document-conversion-progress/
description: تعلم كيف تتبع تقدم تحويل المستندات في C++ باستخدام Aspose.Cells لتعزيز قابلية استخدام التطبيق الخاص بك.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلًا من شاشة تحميل فقط لتعزيز قابلية استخدام تطبيقك. يدعم Aspose.Cells تتبع تقدم تحويل المستند عبر تقديم الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). توفر الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) طرق [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) و [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا التحكم في الصفحات التي يتم تقديمها كما هو موضح في فئة `TestPageSavingCallback` المخصصة.

## **تتبع تقدم تحويل الوثائق**

يعتمد المثال التالي على تحميل ملف Excel المصدر [94896151.xlsx](94896151.xlsx) ويطبع تقدمه في لوحة التحكم باستخدام فئة `TestPageSavingCallback` التي تنفذ الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
المثال التالي هو الكود الخاص بفئة `TestPageSavingCallback` المخصصة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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

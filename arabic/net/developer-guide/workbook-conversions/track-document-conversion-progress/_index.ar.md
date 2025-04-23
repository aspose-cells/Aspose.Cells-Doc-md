---
title: تتبع تقدم تحويل الوثائق
type: docs
weight: 970
url: /ar/net/track-document-conversion-progress/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، قد يستغرق تحويل ملفات الإكسيل الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام تطبيقك. تدعم Aspose.Cells تتبع عملية تحويل المستند من خلال توفير واجهة البرمجة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). تقدم واجهة البرمجة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) الواجهة [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) والواجهة [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) التي يمكنك تنفيذها في فئتك المخصصة. كما يمكنك أيضًا التحكم في الصفحات التي تم تقديمها كما هو موضح في فئة الاختبار *TestPageSavingCallback*.

## **تتبع تقدم تحويل الوثائق**

يقوم الرمز العيني الذي يلي بتحميل [ملف الإكسل المصدر](94896151.xlsx) ويطبع تقدم التحويل في وحدة التحكم باستخدام الفئة المخصصة *TestPageSavingCallback* التي تنفذ واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

فيما يلي الشيفرة لفئة الاختبار *TestPageSavingCallback* المخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}

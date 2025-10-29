---
title: إضافة إشارات مرجعية PDF مع وجهات مسماة باستخدام Golang عبر C++
linktitle: إضافة إشارات مرجعية لملف PDF بأهداف مسماة
type: docs
weight: 20
url: /ar/go-cpp/add-pdf-bookmarks-with-named-destinations/
description: تعلم كيفية إضافة إشارات مرجعية في PDF مع وجهات مسماة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 الوجهات المسماة هي أنواع خاصة من العلامات المرجعية أو الروابط في PDF التي لا تعتمد على صفحات PDF. وهذا يعني، إذا تمت إضافة أو حذف صفحات من PDF، قد تصبح العلامات المرجعية غير صالحة ولكن الوجهات المسماة ستظل سليمة. لإنشاء وجهة مسماة، يرجى ضبط خاصية [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/getdestinationname/).

## **إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة**

يرجى الرجوع إلى الكود العيني التالي، و[ملف Excel المصدر](50528348.xlsx)، و[ملف PDF الناتج](50528349.pdf). تُظهر اللقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل ملف PDF الناتج. توصف اللقطة الشاشة أيضا كيفية عرض الوجهات المسماة وأنك بحاجة إلى إصدار احترافي من قارئ أكروبات.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPdfBookmarksWithNamedDestinations.go" >}}

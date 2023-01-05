---
title: قم بإضافة PDF إشارات مرجعية ذات الوجهات المحددة
type: docs
weight: 20
url: /ar/java/add-pdf-bookmarks-with-named-destinations/
---
## **سيناريوهات الاستخدام الممكنة**

الوجهات المسماة هي أنواع خاصة من الإشارات المرجعية أو الروابط الموجودة في PDF والتي لا تعتمد على PDF صفحة. هذا يعني أنه إذا تمت إضافة صفحات أو حذفها من PDF ، فقد تصبح الإشارات المرجعية غير صالحة ولكن ستظل الوجهات المسماة سليمة. لإنشاء وجهة محددة ، يرجى تعيين[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName)خاصية.

## **قم بإضافة PDF إشارات مرجعية ذات الوجهات المحددة**

يرجى الاطلاع على نموذج التعليمات البرمجية التالي ، الخاص به[ملف Excel المصدر](50528370.xlsx)و له[ملف الإخراج PDF](50528369.pdf). تُظهر لقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل الإخراج PDF. توضح لقطة الشاشة أيضًا كيفية عرض الوجهات المسماة وأنك بحاجة إلى إصدار احترافي من برنامج Acrobat Reader.

![ما يجب القيام به: image_بديل_نص](add-pdf-bookmarks-with-named-destinations_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}

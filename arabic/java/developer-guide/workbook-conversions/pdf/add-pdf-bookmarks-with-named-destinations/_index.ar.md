---
title: إضافة إشارات مرجعية لملف PDF بأهداف مسماة
type: docs
weight: 20
url: /ar/java/add-pdf-bookmarks-with-named-destinations/
---

## **سيناريوهات الاستخدام المحتملة**

الوجهات المسماة هي أنواع خاصة من الإشارات المرجعية أو الروابط في ملفات PDF التي لا تعتمد على صفحات PDF. يعني ذلك، إذا تمت إضافة صفحات أو حذفها من PDF، فإن الإشارات المرجعية قد تصبح غير صالحة ولكن الوجهات المسماة ستظل سليمة. لإنشاء وجهة مسماة، يرجى تعيين الخاصية [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName).

## **إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة**

يرجى رؤية كود العينة التالي ، [ملف Excel المصدر](50528370.xlsx)، و [ملف PDF الإخراج](50528369.pdf). يظهر اللقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل ملف PDF الإخراج. كما تصف اللقطة الشاشة أيضًا كيفية عرض الوجهات المسماة وأنه يلزمك نسخة احترافية من Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
{{< app/cells/assistant language="java" >}}

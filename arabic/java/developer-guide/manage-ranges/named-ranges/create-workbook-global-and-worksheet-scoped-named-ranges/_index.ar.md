---
title: قم بإنشاء مصنف (عام) وورقة عمل نطاقات مسماة محددة النطاق
type: docs
weight: 10
url: /ar/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft يسمح Excel للمستخدمين بتعريف النطاقات المسماة بنطاقين مختلفين: المصنف (المعروف أيضًا باسم النطاق العام) وورقة العمل.

- يمكن الوصول إلى النطاقات المسماة بنطاق مصنف من أي ورقة عمل داخل هذا المصنف ببساطة باستخدام اسمه.
- يتم الوصول إلى نطاقات ورقة العمل المحددة النطاق باستخدام مرجع ورقة العمل المحددة التي تم إنشاؤها فيها.

يوفر Aspose.Cells نفس الوظيفة مثل Microsoft Excel لإضافة مصنف وورقة عمل نطاقات مسماة محددة النطاق. عند إنشاء ورقة عمل ذات نطاق مسمى ، يجب استخدام مرجع ورقة العمل في النطاق المسمى لتحديده على أنه نطاق مسمى بورقة عمل.

{{% /alert %}}

 تُظهر نماذج التعليمات البرمجية التالية كيفية إنشاء نطاقات أسماء نطاق ورقة العمل والمصنف باستخدام ملحق[**نطاق**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) صف دراسي.

## **إضافة نطاق مسمى مع نطاق المصنف**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **إضافة نطاق مسمى بنطاق ورقة العمل**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}

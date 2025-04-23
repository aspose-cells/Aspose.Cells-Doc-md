---
title: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 700
url: /ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

عندما تقوم بحذف الأعمدة والصفوف الفارغة في ورقة العمل، تصبح مراجعاتها في ورق العمل الآخرة غير صالحة. إذا كنت ترغب في تجنب هذا السلوك وتريد تحديث تلك المراجعات أيضًا، فيرجى استخدام [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) وضبطه **صحيح**.

{{% /alert %}} 
## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**
يرجى رؤية رمز العينة التالي وناتجه في وحدة التحكم. الخلية E3 في الورقة المرجعية الثانية تحتوي على صيغة =Sheet1!C3 التي تشير إلى الخلية C3 في الورقة المرجعية الأولى. إذا قمت بتعيين [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) بصفته **صحيح**، سيتم تحديث هذه الصيغة وتصبح =Sheet1!A1 عند حذف الأعمدة والصفوف الفارغة في الورقة المرجعية الأولى. ومع ذلك، إذا قمت بتعيين [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) بصفته **خاطئ**، ستظل الصيغة في الخلية E3 للورقة المرجعية الثانية =Sheet1!C3 وتصبح غير صالحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **مخرجات الوحدة**
هذا هو ناتج وحدة التحكم لرمز العينة أعلاه عندما يتم تعيين خاصية [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) بصفته **صحيح**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

هذا هو ناتج وحدة التحكم لرمز العينة أعلاه عندما يتم تعيين خاصية [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) بصفته **خاطئ**. كما ترون، لم يتم تحديث الصيغة في الخلية E3 للورقة المرجعية الثانية وقيمة الخلية الآن 0 بدلاً من 4 وهو غير صالح.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

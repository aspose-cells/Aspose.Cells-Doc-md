---
title: قم بتحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 700
url: /ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 عند حذف أعمدة وصفوف فارغة في ورقة عمل ، تصبح مراجعها في أوراق العمل الأخرى غير صالحة. إذا كنت تريد تجنب هذا السلوك وتريد تحديث هذه المراجع أيضًا ، فيرجى استخدام[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) وضبطها**حقيقي**.

{{% /alert %}} 
## **قم بتحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**
 يرجى الاطلاع على نموذج التعليمات البرمجية التالي وإخراج وحدة التحكم الخاصة به. تحتوي الخلية E3 في ورقة العمل الثانية على الصيغة = Sheet1! C3 التي تشير إلى الخلية C3 في ورقة العمل الأولى. إذا قمت بتعيين[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) الملكية مثل**حقيقي** ، سيتم تحديث هذه الصيغة وتصبح = Sheet1! A1 عند حذف الأعمدة والصفوف الفارغة في ورقة العمل الأولى. ومع ذلك ، إذا قمت بتعيين[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) الملكية مثل**خاطئة**، ستبقى الصيغة في الخلية E3 من ورقة العمل الثانية = Sheet1! C3 وتصبح غير صالحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **إخراج وحدة التحكم**
هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه عندما[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) تم تعيين الخاصية على أنها**حقيقي**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه عندما[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) تم تعيين الخاصية على أنها**خاطئة**. كما ترى ، لم يتم تحديث الصيغة الموجودة في الخلية E3 من ورقة العمل الثانية وأصبحت قيمة الخلية الآن 0 بدلاً من 4 وهي غير صالحة.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}

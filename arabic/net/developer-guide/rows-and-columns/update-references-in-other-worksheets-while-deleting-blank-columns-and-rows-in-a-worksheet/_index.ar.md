---
title: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 5000
url: /ar/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

عند حذف الأعمدة والصفوف الفارغة في ورقة العمل، تصبح مراجعها في ورقات العمل الأخرى غير صالحة. إذا كنت ترغب في تجنب هذا السلوك وتريد تحديث تلك المراجع لورقة العمل الحالية في ورقات العمل الأخرى أيضًا، يرجى استخدام الخاصية [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) وتعيينها على **صحيح**.

{{% /alert %}}

## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**

يرجى رؤية الكود العيني التالي ومخرجات وحدة التحكم الخاصة به. يحتوي الخلية E3 في الورقة العمل الثانية على صيغة =Sheet1!C3 التي تشير إلى الخلية C3 في الورقة العمل الأولى. إذا قمت بتعيين الخاصية [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) ك **صحيح**, سيتم تحديث هذه الصيغة وتصبح =Sheet1!A1 عند حذف الأعمدة والصفوف الفارغة في الورقة العمل الأولى. ومع ذلك، إذا قمت بتعيين الخاصية [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) ك **خطأ**, ستظل الصيغة في الخلية E3 من الورقة العمل الثانية =Sheet1!C3 وتصبح غير صالحة.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للكود العيني أعلاه عندما يتم تعيين الخاصية [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) ك **صحيح**.

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

هذه هي مخرجات وحدة التحكم للكود العيني أعلاه عندما يتم تعيين الخاصية [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) ك **خطأ**. كما ترون، الصيغة في الخلية E3 من الورقة العمل الثانية لم تتم تحديثها وقيمة الخلية الآن هي 0 بدلاً من 4 وهو غير صالحة.

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

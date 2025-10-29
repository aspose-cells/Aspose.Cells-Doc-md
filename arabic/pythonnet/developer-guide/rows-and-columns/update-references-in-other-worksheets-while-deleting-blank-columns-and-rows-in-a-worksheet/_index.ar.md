---
title: تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل
type: docs
weight: 5000
url: /ar/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: يوضح هذا المقال كيفية تحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورق العمل باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel، تحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورق العمل، تحديث المراجع عند حذف الأعمدة والصفوف الفارغة في ورق العمل بلغة Python.
---

{{% alert color="primary" %}}

عند حذف الأعمدة والصفوف الفارغة في ورقة العمل، تصبح مراجعها في ورقات العمل الأخرى غير صالحة. إذا كنت ترغب في تجنب هذا السلوك وتريد تحديث تلك المراجع لورقة العمل الحالية في ورقات العمل الأخرى أيضًا، يرجى استخدام الخاصية [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) وتعيينها على **صحيح**.

{{% /alert %}}

## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**

يرجى رؤية الكود العيني التالي ومخرجات وحدة التحكم الخاصة به. يحتوي الخلية E3 في الورقة العمل الثانية على صيغة =Sheet1!C3 التي تشير إلى الخلية C3 في الورقة العمل الأولى. إذا قمت بتعيين الخاصية [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) ك **صحيح**, سيتم تحديث هذه الصيغة وتصبح =Sheet1!A1 عند حذف الأعمدة والصفوف الفارغة في الورقة العمل الأولى. ومع ذلك، إذا قمت بتعيين الخاصية [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) ك **خطأ**, ستظل الصيغة في الخلية E3 من الورقة العمل الثانية =Sheet1!C3 وتصبح غير صالحة.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للكود العيني أعلاه عندما يتم تعيين الخاصية [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) ك **صحيح**.

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

هذه هي مخرجات وحدة التحكم للكود العيني أعلاه عندما يتم تعيين الخاصية [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) ك **خطأ**. كما ترون، الصيغة في الخلية E3 من الورقة العمل الثانية لم تتم تحديثها وقيمة الخلية الآن هي 0 بدلاً من 4 وهو غير صالحة.

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
{{< app/cells/assistant language="python-net" >}}

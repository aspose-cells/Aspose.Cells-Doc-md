---
title: التعامل مع الأحداث بعد حذف الأعمدة والصفوف في GridDesktop
type: docs
weight: 80
url: /ar/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop ، الأحداث ، حذف صف ، حذف عمود
description: يقدم هذا المقال الأحداث بعد حذف الصف / العمود في GridDesktop.
---

## **سيناريوهات الاستخدام المحتملة**
أضاف Aspose.Cells for GridDesktop حدثين جديدين ألا وهما AfterDeleteColumns و AfterDeleteRows كما هو موضح في اللقطة الناتجة التالية. يتم تشغيل هذه الأحداث عند حذف الأعمدة والصفوف على التوالي.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **التعامل مع الأحداث بعد حذف الأعمدة والصفوف في GridDesktop**
يشرح الكود العيني التالي كيفية الاستفادة من أحداث AfterDeleteColumns و AfterDeleteRows. كلما قمت بحذف بعض الأعمدة أو الصفوف ، سيتم استدعاء الوظيفة المعطاة وإظهار مربع رسالة يعرض فهرس العمود أو الصف المحذوف.
## **الكود المثالي**
{{< highlight java >}}

 private void gridDesktop1_AfterDeleteColumnsAndRows(object sender, Aspose.Cells.GridDesktop.WorksheetEventArgs args)

{

    if(args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.ColumnDeleted)

    {

        MessageBox.Show("Deleted Column Index: " + args.Index);

    }

    if (args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.RowDeleted)

    {

        MessageBox.Show("Deleted Row Index: " + args.Index);

    }

}

{{< /highlight >}}

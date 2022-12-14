---
title: معالجة الأحداث بعد حذف الأعمدة والصفوف في GridDesktop
type: docs
weight: 80
url: /ar/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **سيناريوهات الاستخدام الممكنة**
أضاف Aspose.Cells لـ GridDesktop حدثين جديدين أي AfterDeleteColumns و AfterDeleteRows كما هو موضح في لقطة الشاشة التالية. يتم تشغيل هذه الأحداث عندما تحذف الأعمدة والصفوف على التوالي.

![ما يجب القيام به: image_بديل_نص](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **معالجة الأحداث بعد حذف الأعمدة والصفوف في GridDesktop**
يشرح نموذج التعليمات البرمجية التالي كيفية الاستفادة من الأحداث AfterDeleteColumns و AfterDeleteRows. عندما تقوم بحذف بعض الأعمدة أو الصفوف ، سيتم استدعاء الوظيفة المحددة وإظهار مربع رسالة يعرض فهرس العمود أو الصف المحذوف.
## **عينة من الرموز**
{{< highlight "java" >}}

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

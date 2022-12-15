---
title: محرر جداول البيانات - العمل مع الصفوف والأعمدة
type: docs
weight: 30
url: /ar/java/spreadsheet-editor-working-with-rows-and-columns/
---
**جدول المحتويات**

- [أضف صفًا](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 - WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [أضف عمودًا](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 - WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [حذف صف](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 - WorksheetView.deleteRow
- [احذف عمود](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [عرض العمود وارتفاع الصف](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 - WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [أدخل Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **أضف صفًا**
لإضافة صف جديد:

1. انقر فوق الخلية حيث تريد إضافة صف.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**إضافة صف أعلاه** لإضافة صف أعلى الخلية المحددة.
1.  انقر**إضافة صف أدناه** لإضافة صف أسفل الخلية المحددة.

سيضيف المحرر صفًا جديدًا في الموقع المحدد.

![ما يجب القيام به: image_بديل_نص](jjsornm.png)

**كيف تعمل؟**

 ال**إضافة صف أعلاه** و**إضافة صف أدناه** يتم التعامل معها بواسطة وحدة برامج JSF الخلفية**WorksheetView**. الكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.addRowAbove**
{{< highlight "java" >}}

     public void addRowAbove() {

        try {

            getAsposeWorksheet().getCells().insertRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(currentRowId);

    }

{{< /highlight >}}

#### **WorksheetView.addRowBelow**
{{< highlight "java" >}}

     public void addRowBelow() {

        if (getCurrentRowId() < 0) {

            msg.sendMessage("No cell selected", null);

            return;

        }

        int newRowId = currentRowId + 1;

        try {

            getAsposeWorksheet().getCells().insertRows(newRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(newRowId);

    }

{{< /highlight >}}
### **أضف عمودًا**
لإضافة عمود جديد:

1. انقر فوق الخلية حيث تريد إضافة عمود.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**أضف العمود قبل**لإضافة عمود قبل الخلية المحددة.
1.  انقر**أضف العمود بعد ذلك** لإضافة عمود بعد الخلية المحددة.

سيضيف المحرر عمودًا جديدًا في الموقع المحدد.

![ما يجب القيام به: image_بديل_نص](jjsornm.png)

**كيف تعمل؟**

 ال**أضف العمود قبل** و**أضف العمود بعد ذلك** يتم التعامل معها بواسطة وحدة برامج JSF الخلفية**WorksheetView**. الكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.addColumnBefore**
{{< highlight "java" >}}

     public void addColumnBefore() {

        try {

            getAsposeWorksheet().getCells().insertColumns(getCurrentColumnId(), 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(currentColumnId);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.addColumnAfter**
{{< highlight "java" >}}

     public void addColumnAfter() {

        int newColumnId = currentColumnId + 1;

        try {

            getAsposeWorksheet().getCells().insertColumns(newColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(newColumnId);

        purge();

    }

{{< /highlight >}}
### **حذف صف**
لحذف صف:

1. انقر فوق خلية في الصف الذي تريد حذفه.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**احذف صف** زر.

سيقوم المحرر بحذف الصف الذي يتضمن الخلية المحددة.

![ما يجب القيام به: image_بديل_نص](jjsornm.png)

**كيف تعمل؟**

 ال**احذف صف** يتم التعامل مع الزر بواسطة وحدة برامج JSF الخلفية**WorksheetView** باستخدام الطريقة**WorksheetView.deleteRow**:
#### **WorksheetView.deleteRow**
{{< highlight "java" >}}

     public void deleteRow() {

        try {

            getAsposeWorksheet().getCells().deleteRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete row", cx.getMessage());

            return;

        }

        cells.getRows(workbook.getCurrent()).remove(currentRowId);

        getRowHeight().remove(currentRowId);

        purge();

    }

{{< /highlight >}}
### **احذف عمود**
لحذف عمود:

1. انقر فوق خلية في العمود الذي تريد حذفه.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**حذف العمود** زر.

سيقوم المحرر بحذف العمود الذي يتضمن الخلية المحددة.

![ما يجب القيام به: image_بديل_نص](jjsornm.png)

**كيف تعمل؟**

 ال**حذف العمود** يتم التعامل مع الزر بواسطة وحدة برامج JSF الخلفية**WorksheetView** باستخدام الطريقة**WorksheetView.deleteColumn**:
#### **WorksheetView.deleteColumn**
{{< highlight "java" >}}

     public void deleteColumn() {

        try {

            getAsposeWorksheet().getCells().deleteColumns(currentColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete column", cx.getMessage());

            return;

        }

        cells.getColumns(workbook.getCurrent()).remove(currentColumnId);

        getRowHeight().remove(currentColumnId);

        purge();

    }

{{< /highlight >}}
### **عرض العمود وارتفاع الصف**
لتغيير عرض العمود:

1. انقر فوق أي خلية داخل العمود.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**عرض العمود** زر للفتح**عرض العمود**الحوار.
1. أدخل قيمة جديدة في مربع الحوار.
1.  انقر**قريب**.

سيقوم المحرر بتغيير عرض العمود.

**كيف تغير ارتفاع الصف؟**

لتغيير ارتفاع صف:

1. انقر فوق أي خلية داخل الصف.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**ارتفاع الصف** زر للفتح**ارتفاع الصف**الحوار.
1. أدخل قيمة جديدة في مربع الحوار.
1.  انقر**قريب**.

سيقوم المحرر بتغيير ارتفاع الصف.

**كيف تعمل؟**

 عندما يرسل المستخدم قيمة العرض والارتفاع ، يتم التعامل مع هذه القيم من جانب الخادم**setCurrentRowHeight** و**setCurrentColumnWidth** طرق الفول الخلفية JSF**WorksheetView**.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight "java" >}}

     public void setCurrentRowHeight(int height) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setRowHeightPixel(currentRowId, height);

        reloadRowHeight(currentRowId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}

#### **WorksheetView.setCurrentColumnWidth**
{{< highlight "java" >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **أدخل Cell**
لإضافة خلية جديدة:

1. انقر فوق الخلية حيث تريد الجديد.
1.  التبديل إلى**إدراج علامة التبويب**.
1.  انقر**Cell** زر.
1.  يختار**إزاحة Cells لليمين** أو**إزاحة Cells للأسفل** زر.

سيضيف المحرر خلية جديدة في الموقع المحدد. سيتم تحويل الخلايا المجاورة تلقائيًا إما أفقيًا أو رأسيًا لإنشاء مساحة للخلايا الجديدة.

**كيف تعمل؟**

 ال**إزاحة Cells لليمين** و**إزاحة Cells للأسفل** يتم التعامل معها بواسطة وحدة برامج JSF الخلفية**WorksheetView**. الكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.addCellShift إلى اليمين**
{{< highlight "java" >}}

     public void addCellShiftRight() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.RIGHT);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.addCellShiftDown**
{{< highlight "java" >}}

     public void addCellShiftDown() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.DOWN);

        purge();

    }

{{< /highlight >}}

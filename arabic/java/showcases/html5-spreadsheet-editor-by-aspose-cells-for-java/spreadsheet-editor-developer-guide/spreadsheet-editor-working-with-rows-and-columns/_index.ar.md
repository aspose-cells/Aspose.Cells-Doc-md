---
title: محرر جداول البيانات  العمل مع الصفوف والأعمدة
type: docs
weight: 30
url: /ar/java/spreadsheet-editor-working-with-rows-and-columns/
---

جدول المحتويات

- [إضافة صف](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [إضافة عمود](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [حذف صف](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [حذف عمود](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [عرض العرض وارتفاع الصف](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [إدراج خلية](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **إضافة صف**
لإضافة صف جديد:

1. انقر فوق خلية حيث ترغب في إضافة صف.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على **إضافة صف أعلاه** لإضافة صف أعلاه للخلية المحددة.
1. انقر على **إضافة صف أدناه** لإضافة صف أدناه للخلية المحددة.

سيقوم المحرر بإضافة صف جديد في الموقع المحدد.

![todo:image_alt_text](jjsornm.png)

**كيف يعمل هذا؟**

إضافة صف أعلاه وصف أدناه يتم التحكم فيهما بواسطة حزمة الخلفية JSF bean **WorksheetView**. والكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.addRowAbove**
{{< highlight java >}}

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
{{< highlight java >}}

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
### **إضافة عمود**
لإضافة عمود جديد:

1. انقر على خلية حيث ترغب في إضافة عمود.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على **إضافة عمود قبل** لإضافة عمود قبل الخلية المحددة.
1. انقر على **إضافة عمود بعد** لإضافة عمود بعد الخلية المحددة.

سيقوم المحرر بإضافة عمود جديد في الموقع المحدد.

![todo:image_alt_text](jjsornm.png)

**كيف يعمل هذا؟**

**إضافة العمود قبل** و **إضافة العمود بعد** يتم التعامل معهم بواسطة جافا سكريبت الخلفية JSF bean **WorksheetView**. ومصدر الكود للأساليب المعنية هو كالتالي:
#### **WorksheetView.addColumnBefore**
{{< highlight java >}}

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
{{< highlight java >}}

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

1. انقر على خلية في الصف الذي تريد حذفه.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على زر **حذف الصف**.

سيقوم المحرر بحذف الصف الذي يتضمن الخلية المحددة.

![todo:image_alt_text](jjsornm.png)

**كيف يعمل هذا؟**

زر **حذف الصف** يتم التعامل معه بواسطة جافا سكريبت الخلفية JSF bean **WorksheetView** باستخدام الأسلوب **WorksheetView.deleteRow**:
#### **WorksheetView.deleteRow**
{{< highlight java >}}

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
### **حذف عمود**
لحذف عمود:

1. انقر على خلية في العمود الذي تريد حذفه.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على زر **حذف العمود**.

سيقوم المحرر بحذف العمود الذي يتضمن الخلية المحددة.

![todo:image_alt_text](jjsornm.png)

**كيف يعمل هذا؟**

يتم التعامل مع زر **حذف العمود** عبر شريحة JSF backend bean **WorksheetView** باستخدام الأسلوب **WorksheetView.deleteColumn**: 
#### **WorksheetView.deleteColumn**
{{< highlight java >}}

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
### **عرض العرض وارتفاع الصف**
لتغيير عرض العمود:

1. انقر فوق أي خلية داخل العمود.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر فوق زر **عرض العمود** لفتح مربع الحوار **عرض العمود**.
1. أدخل قيمة جديدة في مربع الحوار.
1. انقر على **إغلاق**.

سيقوم المحرر بتغيير عرض العمود.

**كيفية تغيير ارتفاع الصف؟**

لتغيير ارتفاع صف:

1. انقر فوق أي خلية داخل الصف.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر فوق زر **ارتفاع الصف** لفتح مربع الحوار **ارتفاع الصف**.
1. أدخل قيمة جديدة في مربع الحوار.
1. انقر على **إغلاق**.

سيقوم المحرر بتغيير ارتفاع الصف.

**كيف يعمل هذا؟**

عندما يقوم المستخدم بإرسال قيمة العرض والارتفاع، يتم التعامل مع هذه القيم على الجانب الخادم من خلال أساليب setCurrentRowHeight و setCurrentColumnWidth في شريط الخلفية JSF WorksheetView.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight java >}}

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
{{< highlight java >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **إدراج خلية**
لإضافة خلية جديدة:

1. انقر على الخلية التي تريد الجديدة.
1. التبديل إلى علامة التبويب الإدخال.
1. انقر فوق زر الخلية.
1. اختر زر الانتقال الى الخلايا اليمين او الخلايا الأسفل.

سيقوم المحرر بإضافة خلية جديدة في الموقع المحدد. سيتم نقل الخلايا المجاورة تلقائيًا إما أفقيًا أو رأسيًا لإنشاء مساحة للخلية الجديدة.

**كيف يعمل هذا؟**

الانتقال إلى الخلايا اليمين والخلايا الأسفل يتم التعامل معها من خلال خلفية JSF WorksheetView. كود المصدر للأساليب المعنية على النحو التالي:
#### **WorksheetView.addCellShiftRight**
{{< highlight java >}}

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
{{< highlight java >}}

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

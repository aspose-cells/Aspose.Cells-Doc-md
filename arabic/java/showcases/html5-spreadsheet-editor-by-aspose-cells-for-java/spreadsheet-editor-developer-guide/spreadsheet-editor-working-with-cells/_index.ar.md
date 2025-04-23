---
title: محرر جدول البيانات  العمل مع الخلايا
type: docs
weight: 40
url: /ar/java/spreadsheet-editor-working-with-cells/
---

جدول المحتويات

- [اختيار الخلية](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - اتصال اختيار الخلية
- [حذف الخلية](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [مسح الخلية](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **اختيار الخلية**
استخدم المؤشر للفأرة لتشير إلى الخلية. انقر فوق الخلية لتحديدها. تتميز الخلية المحددة بمستطيل عريض.

**كيف يعمل هذا؟**

عندما ينقر المستخدم على خلية، يتم التعامل مع الحدث من خلال دالة الاستدعاء الخاصة بجافا سكربت المرتبطة بمكون Primefaces.
#### **استدعاء تحديد الخلية**
{{< highlight java >}}

                     var columnId = $(this).find('.ui-cell-editor-input input').attr('data-columnid');

                    var rowId = $(this).find('.ui-cell-editor-input input').attr('data-rowid');

                    var clientId = $(this).find('.ui-cell-editor').attr('id');

                    PF('currentColumnIdValue').jq.val(columnId);

                    PF('currentRowIdValue').jq.val(rowId);

                    PF('currentCellClientIdValue').jq.val(clientId);

                    if ($(this).find('.ui-cell-editor-output div').hasClass('b')) {

                        PF('boldOptionButton').check();

                    } else {

                        PF('boldOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('i')) {

                        PF('italicOptionButton').check();

                    } else {

                        PF('italicOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('u')) {

                        PF('underlineOptionButton').check();

                    } else {

                        PF('underlineOptionButton').uncheck();

                    }

                    PF('fontOptionSelector').selectValue($(this).find('.ui-cell-editor-output div').css('font-family').slice(1, -1));

                    PF('fontSizeOptionSelector').selectValue($(this).find('.ui-cell-editor-output div')[0].style.fontSize.replace('pt', ''));

                    ['al', 'ac', 'ar', 'aj'].forEach(function(v) {

                        if ($(this).find('.ui-cell-editor-output div').hasClass(v)) {

                            // TODO: save the value to PF('alignOptionSelector');

                        }

                    });

                    PF('currentColumnWidthValue').jq.val($(this).width());

                    PF('currentRowHeightValue').jq.val($(this).height());

                    $($this.selectedCell).removeClass('sheet-selected-cell');

                    $(this).addClass('sheet-selected-cell');

                    $this.selectedCell = this;

{{< /highlight >}}
### **حذف الخلية**
لحذف خلية:

1. انقر على الخلية التي تريد حذفها.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على زر **حذف الخلية**.
1. اختيار زر **تحريك الخلايا للأعلى** أو **تحريك الخلايا لليسار**.

سيقوم المحرر بحذف الخلية المحددة. سيتم نقل الخلايا المجاورة تلقائيًا إما أفقيًا أو عموديًا لضبط المساحة.

**كيف يعمل هذا؟**

تُعالج **تحريك الخلايا للأعلى** و **تحريك الخلايا لليسار** بواسطة دمج JSF backend bean **WorksheetView**. ويكون الكود المصدري للطرق المعنية كما يلي:
#### **WorksheetView.removeCellShiftUp**
{{< highlight java >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight java >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **مسح الخلية**
لمسح الخلية:

1. انقر على الخلية التي تريد مسحها.
1. التبديل إلى **علامة التبويب التنسيق**.
1. انقر على زر **مسح الخلية**.
1. اختر الخيارات **التنسيقات**, **المحتويات** أو **الكلاهما**.

سيقوم المحرر بمسح الخلية المحددة.

**كيف يعمل هذا؟**

ال**تنسيقات**, **المحتويات** و **الكلاهما** يتم التحكم فيها بواسطة جافا سكريبت خلفية JSF bean **WorksheetView**. الشيفرة المصدرية للأساليب المعنية هي كما يلي:
#### **WorksheetView.clearCurrentCellFormatting**
{{< highlight java >}}

     public void clearCurrentCellFormatting() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearFormats(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCellContents**
{{< highlight java >}}

     public void clearCurrentCellContents() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearContents(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCell**
{{< highlight java >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

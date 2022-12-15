---
title: محرر جداول البيانات - يعمل مع Cells
type: docs
weight: 40
url: /ar/java/spreadsheet-editor-working-with-cells/
---
**جدول المحتويات**

- [اختيار Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell رد اتصال التحديد
- [حذف Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [مسح Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 - WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **اختيار Cell**
استخدم مؤشر الماوس للإشارة إلى خلية. انقر فوق خلية لتحديدها. يتم تمييز الخلية المحددة بواسطة مستطيل عريض.

**كيف تعمل؟**

عندما ينقر المستخدم على خلية ، تتم معالجة الحدث بواسطة وظيفة رد الاتصال JavaScript المرفقة بمكون Primefaces.
#### **Cell رد اتصال التحديد**
{{< highlight "java" >}}

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
### **حذف Cell**
لحذف خلية:

1. انقر فوق الخلية التي تريد حذفها.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**حذف Cell** زر.
1.  يختار**تحول Cells لأعلى** أو**إزاحة Cells لليسار** زر.

سيقوم المحرر بحذف الخلية المحددة. سيتم نقل الخلايا المجاورة تلقائيًا إما أفقيًا أو رأسيًا لضبط المساحة.

**كيف تعمل؟**

 ال**تحول Cells لأعلى** و**إزاحة Cells لليسار** يتم التعامل معها بواسطة وحدة برامج JSF الخلفية**WorksheetView**. الكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.removeCellShiftUp**
{{< highlight "java" >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight "java" >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **مسح Cell**
لمسح خلية:

1. انقر فوق الخلية التي تريد مسحها.
1.  التبديل إلى**علامة التبويب تنسيق**.
1.  انقر**مسح Cell** زر.
1.  يختار**التنسيقات**, **محتويات** أو**كلاهما** اختيار.

سيقوم المحرر بمسح الخلية المحددة.

**كيف تعمل؟**

 ال**التنسيقات**, **محتويات** و**كلاهما** يتم التعامل معها بواسطة وحدة برامج JSF الخلفية**WorksheetView**. الكود المصدري للطرق المعنية هو كما يلي:
#### **WorksheetView.clearCurrentCellFormatting**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

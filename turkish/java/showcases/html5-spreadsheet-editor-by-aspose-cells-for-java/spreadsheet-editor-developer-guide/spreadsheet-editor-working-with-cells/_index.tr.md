---
title: Hesap Tablosu Düzenleyicisi - Cells ile çalışma
type: docs
weight: 40
url: /tr/java/spreadsheet-editor-working-with-cells/
---
**İçindekiler**

- [Cell seçilmesi](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell seçim geri araması
- [Cell'i silin](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Cell'i temizle](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 - WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Cell seçilmesi**
Bir hücreye işaret etmek için fare işaretçinizi kullanın. Seçmek için bir hücreye tıklayın. Seçilen hücre kalın bir dikdörtgenle vurgulanır.

**Nasıl çalışır?**

Kullanıcı bir hücreyi tıkladığında, olay Primefaces bileşenine eklenen JavaScript geri arama işlevi tarafından işlenir.
#### **Cell seçim geri arama**
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
### **Cell'i silin**
Bir hücreyi silmek için:

1. Silmek istediğiniz bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Cell'i sil** buton.
1.  Seçmek**Shift Cells Yukarı** veya**Shift Cells Sola** buton.

Düzenleyici seçilen hücreyi siler. Bitişik hücreler, alanı ayarlamak için otomatik olarak yatay veya dikey olarak kaydırılacaktır.

**Nasıl çalışır?**

 bu**Shift Cells Yukarı** ve**Shift Cells Sola** JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü**. İlgili yöntemlerin kaynak kodu aşağıdaki gibidir:
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
### **Cell'i temizle**
Bir hücreyi temizlemek için:

1. Temizlemek istediğiniz bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Temizle Cell** buton.
1.  Seçmek**formatlar**, **İçindekiler** veya**İkisi birden** seçenek.

Düzenleyici seçilen hücreyi temizleyecektir.

**Nasıl çalışır?**

 bu**formatlar**, **İçindekiler** ve**İkisi birden** JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü**. İlgili yöntemlerin kaynak kodu aşağıdaki gibidir:
#### **WorksheetView.clearCurrentCellBiçimlendirme**
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

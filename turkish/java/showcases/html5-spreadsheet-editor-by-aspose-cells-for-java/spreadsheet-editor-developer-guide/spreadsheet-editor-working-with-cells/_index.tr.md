---
title: Elektronik Tablo Düzenleyici  Hücrelerle Çalışmak
type: docs
weight: 40
url: /tr/java/spreadsheet-editor-working-with-cells/
---

**İçindekiler**

- [Bir Hücre Seçmek](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Hücre seçim geri araması
- [Bir Hücreyi Silmek](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Bir Hücreyi Temizle](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Bir Hücre Seçmek**
Fare işaretçinizi bir hücreye doğrultun. Bir hücreyi seçmek için tıklayın. Seçilen hücre kalın bir dikdörtgen ile vurgulanır.

**Nasıl çalışır?**

Kullanıcı bir hücreye tıkladığında, olay JavaScript geri arama işlevi tarafından ele alınır ve Primefaces bileşenine bağlanır.
#### **Hücre seçim geri araması**
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
### **Bir Hücreyi Silmek**
Bir hücreyi silmek için:

1. Sileceğiniz hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Hücreyi Sil** düğmesine tıklayın.
1. **Hücreleri Yukarı Kaydır** veya **Hücreleri Sola Kaydır** düğmesini seçin.

Düzenleyici, seçili hücreyi silecektir. Yanındaki hücreler, boşluğu ayarlamak için otomatik olarak yatay veya dikey olarak kaydırılacaktır.

**Nasıl çalışır?**

**Üstteki Hücreleri Kaydır** ve **Soldaki Hücreleri Kaydır** JSF arka uç fasıl tanımı **WorksheetView** tarafından işlenir. İlgili yöntemlerin kaynak kodları şöyle:
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
### **Bir Hücreyi Temizle**
Bir hücreyi temizlemek için:

1. Temizlemek istediğiniz hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Hücreyi Temizle** düğmesine tıklayın.
1. **Biçimler**, **İçerikler** veya **Her İkisi** seçeneğini seçin.

Düzenleyici, seçili hücreyi temizleyecektir.

**Nasıl çalışır?**

**Biçimler**, **İçerikler** ve **Her İkisi** JSF arka uç fasıl tanımı **WorksheetView** tarafından işlenir. İlgili yöntemlerin kaynak kodları şöyle:
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

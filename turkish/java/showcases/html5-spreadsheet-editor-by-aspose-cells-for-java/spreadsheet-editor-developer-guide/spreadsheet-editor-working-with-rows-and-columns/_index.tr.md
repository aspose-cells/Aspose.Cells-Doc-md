---
title: Tablo Düzenleyici  Satırlar ve Sütunlarla Çalışma
type: docs
weight: 30
url: /tr/java/spreadsheet-editor-working-with-rows-and-columns/
---

**İçindekiler**

- [Bir Satır Ekle](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Sütun Ekle](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Satır Sil](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Bir Sütunu Sil](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Sütun Genişliği ve Satır Yüksekliği](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Bir Hücre Ekle](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Bir Satır Ekle**
Yeni bir satır eklemek için:

1. Bir satır eklemek istediğiniz hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. Seçili hücrenin üstüne bir satır eklemek için **Üstte Satır Ekle**'ye tıklayın.
1. Seçili hücrenin altına bir satır eklemek için **Alttan Satır Ekle**'ye tıklayın.

Düzenleyici seçili konuma yeni bir satır ekleyecek.

![todo:image_alt_text](jjsornm.png)

**Nasıl çalışır?**

**Üstte Satır Ekle** ve **Alttan Satır Ekle**, JSF arka uç fasulyesi **WorksheetView** tarafından ele alınır. İlgili yöntemlerin kaynak kodları aşağıdaki gibidir:
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
### **Sütun Ekle**
Yeni bir sütun eklemek için:

1. Bir sütun eklemek istediğiniz hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. Seçili hücrenin yanına bir sütun eklemek için **Öncesine Sütun Ekle**'ye tıklayın.
1. Seçili hücrenin sonrasına bir sütun eklemek için **Sonrasına Sütun Ekle**'ye tıklayın.

Düzenleyici seçili konuma yeni bir sütun ekleyecek.

![todo:image_alt_text](jjsornm.png)

**Nasıl çalışır?**

**Öncesine Sütun Ekle** ve **Sonrasına Sütun Ekle**, JSF arka uç fasulyesi **WorksheetView** tarafından ele alınır. İlgili yöntemlerin kaynak kodları aşağıdaki gibidir:
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
### **Satır Sil**
Bir satırı silmek için:

1. Sileceğiniz satırdaki bir hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Satırı Sil** düğmesine tıklayın.

Düzenleyici seçili hücreyi içeren satırı silecektir.

![todo:image_alt_text](jjsornm.png)

**Nasıl çalışır?**

**Satırı Sil** düğmesi, **WorksheetView.deleteRow** yöntemini kullanarak JSF backend bean **WorksheetView** tarafından işlenir:
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
### **Bir Sütunu Sil**
Bir sütunu silmek için:

1. Sileceğiniz sütundaki bir hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Sütunu Sil** düğmesine tıklayın.

Düzenleyici seçili hücreyi içeren sütunu silecektir.

![todo:image_alt_text](jjsornm.png)

**Nasıl çalışır?**

**Sütunu Sil** düğmesi, **WorksheetView.deleteColumn** yöntemini kullanarak JSF backend bean **WorksheetView** tarafından işlenir:
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
### **Sütun Genişliği ve Satır Yüksekliği**
Bir sütunun genişliğini değiştirmek için:

1. Sütun içinde herhangi bir hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Sütun Genişliği** düğmesine tıklayarak **Sütun Genişliği** iletişim kutusunu açın.
1. İletişim kutusuna yeni bir değer girin.
1. **Kapat**'a tıklayın.

Düzenleyici sütunun genişliğini değiştirecektir.

**Satır yüksekliği nasıl değiştirilir?**

Bir satırın yüksekliğini değiştirmek için:

1. Satır içinde herhangi bir hücreye tıklayın.
1. **Biçim** sekmesine geçin.
1. **Satır Yüksekliği** düğmesine tıklayarak **Satır Yüksekliği** iletişim kutusunu açın.
1. İletişim kutusuna yeni bir değer girin.
1. **Kapat**'a tıklayın.

Düzenleyici satırın yüksekliğini değiştirecektir.

**Nasıl çalışır?**

Kullanıcı genişlik ve yükseklik değerlerini gönderdiğinde, bu değerler JSF backend bean **WorksheetView**'in **setCurrentRowHeight** ve **setCurrentColumnWidth** metodları tarafından sunucu tarafında işlenir.
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
### **Bir Hücre Ekle**
Yeni bir hücre eklemek için:

1. Yeni eklemek istediğiniz hücreye tıklayın.
1. **Ekleme sekmesine** geçin.
1. **Hücre** düğmesine tıklayın.
1. **Sağa Kaydır** veya **Aşağı Kaydır** düğmesini seçin.

Düzenleyici seçilen konumda yeni bir hücre ekleyecektir. Yeni bir hücre için yatay veya dikey olarak bitişik hücreler otomatik olarak kaydırılır.

**Nasıl çalışır?**

**Sağa Kaydır** ve **Aşağı Kaydır** olayları JSF backend bean **WorksheetView** tarafından işlenir. İlgili metodların kaynak kodları aşağıdaki gibidir:
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

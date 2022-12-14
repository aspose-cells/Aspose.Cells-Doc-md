---
title: Hesap Tablosu Düzenleyicisi - Satırlar ve Sütunlarla Çalışma
type: docs
weight: 30
url: /tr/java/spreadsheet-editor-working-with-rows-and-columns/
---
**İçindekiler**

- [Satır Ekle](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
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
- [Cell girin](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Satır Ekle**
Yeni bir satır eklemek için:

1. Satır eklemek istediğiniz hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Yukarıya Satır Ekle** seçili hücrenin üstüne bir satır eklemek için.
1.  Tıklamak**Aşağıya Satır Ekle** seçili hücrenin altına bir satır eklemek için.

Düzenleyici, seçilen konuma yeni bir satır ekleyecektir.

![yapılacaklar:resim_alternatif_Metin](jjsornm.png)

**Nasıl çalışır?**

 bu**Yukarıya Satır Ekle** ve**Aşağıya Satır Ekle** JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü**. İlgili yöntemlerin kaynak kodu aşağıdaki gibidir:
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
### **Sütun Ekle**
Yeni bir sütun eklemek için:

1. Sütun eklemek istediğiniz hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Önce Sütun Ekle**seçili hücreden önce bir sütun eklemek için.
1.  Tıklamak**Sonra Sütun Ekle** seçili hücreden sonra bir sütun eklemek için.

Düzenleyici, seçilen konuma yeni bir sütun ekleyecektir.

![yapılacaklar:resim_alternatif_Metin](jjsornm.png)

**Nasıl çalışır?**

 bu**Önce Sütun Ekle** ve**Sonra Sütun Ekle** JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü**. İlgili yöntemlerin kaynak kodu aşağıdaki gibidir:
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
### **Satır Sil**
Bir satırı silmek için:

1. Silmek istediğiniz satırdaki bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Sırayı sil** buton.

Düzenleyici, seçilen hücreyi içeren satırı siler.

![yapılacaklar:resim_alternatif_Metin](jjsornm.png)

**Nasıl çalışır?**

 bu**Sırayı sil** düğme JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü** yöntem kullanarak**WorksheetView.deleteRow**:
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
### **Bir Sütunu Sil**
Bir sütunu silmek için:

1. Silmek istediğiniz sütundaki bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Sütunu Sil** buton.

Düzenleyici, seçilen hücreyi içeren sütunu siler.

![yapılacaklar:resim_alternatif_Metin](jjsornm.png)

**Nasıl çalışır?**

 bu**Sütunu Sil** düğme JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü** yöntem kullanarak**WorksheetView.deleteColumn**:
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
### **Sütun Genişliği ve Satır Yüksekliği**
Bir sütunun genişliğini değiştirmek için:

1. Sütunun içindeki herhangi bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Sütun genişliği** açmak için düğme**Sütun genişliği**diyalog
1. İletişim kutusuna yeni bir değer girin.
1.  Tıklamak**Kapat**.

Düzenleyici, sütunun genişliğini değiştirecektir.

**Satır yüksekliği nasıl değiştirilir?**

Bir satırın yüksekliğini değiştirmek için:

1. Satır içindeki herhangi bir hücreye tıklayın.
1.  Çevirmek**Biçim sekmesi**.
1.  Tıklamak**Satır yüksekliği** açmak için düğme**Satır yüksekliği**diyalog
1. İletişim kutusuna yeni bir değer girin.
1.  Tıklamak**Kapat**.

Editör satırın yüksekliğini değiştirir.

**Nasıl çalışır?**

 Kullanıcı genişlik ve yükseklik değerini gönderdiğinde, bu değerler sunucu tarafında şu şekilde işlenir:**setCurrentRowHeight** ve**setCurrentColumnWidth** JSF arka uç fasulyesi yöntemleri**Çalışma Sayfası Görünümü**.
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
### **Cell girin**
Yeni bir hücre eklemek için:

1. Yeni yapmak istediğiniz bir hücreye tıklayın.
1.  Çevirmek**Sekme ekle**.
1.  Tıklamak**Cell** buton.
1.  Seçmek**Cells Sağa Kaydır** veya**Vites Cells Aşağı** buton.

Düzenleyici, seçilen konuma yeni bir hücre ekleyecektir. Bitişik hücreler, yenisine yer açmak için otomatik olarak yatay veya dikey olarak kaydırılacaktır.

**Nasıl çalışır?**

 bu**Cells Sağa Kaydır** ve**Vites Cells Aşağı** JSF arka uç çekirdeği tarafından işlenir**Çalışma Sayfası Görünümü**. İlgili yöntemlerin kaynak kodu aşağıdaki gibidir:
#### **WorksheetView.addCellShiftRight**
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

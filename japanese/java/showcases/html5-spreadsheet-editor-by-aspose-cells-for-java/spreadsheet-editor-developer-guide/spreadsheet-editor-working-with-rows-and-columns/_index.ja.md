---
title: スプレッドシート エディター - 行と列の操作
type: docs
weight: 30
url: /ja/java/spreadsheet-editor-working-with-rows-and-columns/
---
**目次**

- [行を追加](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [列を追加する](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [行を削除する](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 WorksheetView.deleteRow
- [列を削除する](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [列の幅と行の高さ](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [Cell を挿入](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **行を追加**
新しい行を追加するには:

1. 行を追加するセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**上に行を追加**選択したセルの上に行を追加します。
1. クリック**下に行を追加**選択したセルの下に行を追加します。

エディターは、選択した場所に新しい行を追加します。

![todo:画像_代替_文章](jjsornm.png)

**使い方？**

の**上に行を追加**と**下に行を追加** JSF バックエンド Bean によって処理されます**ワークシート ビュー**.それぞれのメソッドのソース コードは次のとおりです。
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
### **列を追加する**
新しい列を追加するには:

1. 列を追加するセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**前に列を追加**選択したセルの前に列を追加します。
1. クリック**後に列を追加**選択したセルの後に列を追加します。

エディターは、選択した場所に新しい列を追加します。

![todo:画像_代替_文章](jjsornm.png)

**使い方？**

の**前に列を追加**と**後に列を追加** JSF バックエンド Bean によって処理されます**ワークシート ビュー**.それぞれのメソッドのソース コードは次のとおりです。
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
### **行を削除する**
行を削除するには:

1. 削除する行のセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**行を削除**ボタン。

エディターは、選択したセルを含む行を削除します。

![todo:画像_代替_文章](jjsornm.png)

**使い方？**

の**行を削除**ボタンは JSF バックエンド Bean によって処理されます**ワークシート ビュー**メソッドを使用して**WorksheetView.deleteRow**:
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
### **列を削除する**
列を削除するには:

1. 削除する列のセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**列を削除**ボタン。

エディターは、選択したセルを含む列を削除します。

![todo:画像_代替_文章](jjsornm.png)

**使い方？**

の**列を削除**ボタンは JSF バックエンド Bean によって処理されます**ワークシート ビュー**メソッドを使用して**WorksheetView.deleteColumn**:
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
### **列の幅と行の高さ**
列の幅を変更するには:

1. 列内の任意のセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**列幅**開くボタン**列幅**ダイアログ。
1. ダイアログ ボックスに新しい値を入力します。
1. クリック**近い**.

エディターは列の幅を変更します。

**行の高さを変更するには？**

行の高さを変更するには:

1. 行内の任意のセルをクリックします。
1. 切り替える**フォーマットタブ**.
1. クリック**行の高さ**開くボタン**行の高さ**ダイアログ。
1. ダイアログ ボックスに新しい値を入力します。
1. クリック**近い**.

エディターは行の高さを変更します。

**使い方？**

ユーザーが幅と高さの値を送信すると、これらの値はサーバー側で処理されます**setCurrentRowHeight**と**setCurrentColumnWidth** JSF バックエンド Bean のメソッド**ワークシート ビュー**.
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
### **Cell を挿入**
新しいセルを追加するには:

1. 新規作成するセルをクリックします。
1. 切り替える**挿入タブ**.
1. クリック**Cell**ボタン。
1. 選ぶ**シフト Cells 右**また**シフト Cells 下**ボタン。

エディターは、選択した場所に新しいセルを追加します。隣接するセルは自動的に水平方向または垂直方向にシフトされ、新しいセル用のスペースが作成されます。

**使い方？**

の**シフト Cells 右**と**シフト Cells 下** JSF バックエンド Bean によって処理されます**ワークシート ビュー**.それぞれのメソッドのソース コードは次のとおりです。
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

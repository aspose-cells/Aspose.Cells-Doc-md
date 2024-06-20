---
title: スプレッドシートエディタ  シートの操作
type: docs
weight: 20
url: /ja/java/spreadsheet-editor-working-with-sheets/
---

**目次**

- [シートの追加と削除は?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [シートの名前を変更](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [シート間を切り替える](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **シートの追加と削除は?**
Microsoft Excel では単一ファイル内に複数のシートを持つことができます HTML5 スプレッドシートエディタではユーザーがシートを追加または削除することができます。シートタブにはシートのドロップダウンリストがあります。選択したシートは、エディタによって開かれるシートです。

新しいシートを追加するには:

1. **シートタブ**に切り替えます。
1. **+**(プラス)ボタンをクリックします。

新しいシートが追加され、エディタはそれに切り替わります。

現在選択されているシートを削除するには:

1. **シートタブ**に切り替えます。
1. **-**(マイナス)ボタンをクリックします。

現在選択されているシートが削除され、エディタは前回選択された物に切り替わります。

![todo:image_alt_text](4wgvmu8.png)

**動作仕様**

ユーザが**+** (プラス) および **-** (マイナス) ボタンをクリックすると、JSFバックエンドビーン**WorksheetView**が**WorksheetView.onAddNewSheet**および**WorksheetView.onRemoveActiveSheet**メソッドを使用してイベントを処理します。
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight java >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **シートの名前を変更**
シートの名前を変更するには:

1. **シートタブ**に切り替えます。
1. テキストボックス内のシート名をクリックして編集します。
1. シートの名前を変更します。
1. 終了したら、ENTERキーを押すか、ボックスの外をクリックします。

シートの名前が変更されます。

![todo:image_alt_text](4wgvmu8.png)

**動作仕様**

テキストボックスの値が変更されると、イベントはサーバ上でJSFバックエンドビーン**WorksheetView**によって**WorksheetView.setActiveSheet**メソッドを使用して処理されます。
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **シート間を切り替える**
別のシートに切り替えるには:

1. **シートタブ**に切り替えます。
1. ドロップダウンメニューからシートを選択します。

エディタが選択したシートに切り替わります。

![todo:image_alt_text](4wgvmu8.png)

**動作仕様**

ドロップダウンセレクタの値が変更されると、イベントはサーバ上でJSFバックエンドビーン**WorksheetView**によって**WorksheetView.setActiveSheet**メソッドを使用して処理されます。
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}

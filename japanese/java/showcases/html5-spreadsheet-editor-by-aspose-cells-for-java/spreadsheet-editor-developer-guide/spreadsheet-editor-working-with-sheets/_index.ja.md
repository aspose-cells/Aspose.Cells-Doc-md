---
title: スプレッドシート エディター - シートの操作
type: docs
weight: 20
url: /ja/java/spreadsheet-editor-working-with-sheets/
---
**目次**

- [シートを追加および削除しますか?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [シートの名前を変更](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 WorksheetView.setActiveSheet
- [シートを切り替える](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 WorksheetView.setActiveSheet
### **シートを追加および削除しますか?**
Microsoft Excel では、1 つのファイルに複数のシートを含めることができます。 HTML5 スプレッドシート エディターを使用すると、ユーザーはシートを追加および削除できます。 [シート] タブには、シートのドロップダウン リストがあります。選択したシートは、エディターによって開かれるシートです。

新しいシートを追加するには:

1. 切り替える**シート タブ**.
1. **+** (プラス) ボタンをクリックします。

新しいシートが追加され、エディターがそれに切り替わります。

現在選択されているシートを削除するには:

1. 切り替える**シート タブ**.
1. **-** (マイナス) ボタンをクリックします。

現在選択されているシートが削除され、エディターは最後に選択されたシートに切り替わります。

![todo:画像_代替_文章](4wgvmu8.png)

**使い方？**

ユーザーがクリックすると**+** (プラス) と**-**(マイナス) ボタンがクリックされると、JSF バックエンド Bean**ワークシート ビュー**を使用してイベントを処理します**WorksheetView.onAddNewSheet**と**WorksheetView.onRemoveActiveSheet** メソッド。
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1. 切り替える**シート タブ**.
1. テキスト ボックス内のシート名をクリックして編集します。
1. シートの名前を変更します。
1. 終了したら、ENTER キーを押すか、ボックスの外側をクリックします。

シートの名前が変更されます。

![todo:画像_代替_文章](4wgvmu8.png)

**使い方？**

テキストボックスの値が変更されると、イベントはサーバー上で JSF バックエンド Bean によって処理されます**ワークシート ビュー**メソッドを使用して**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
### **シートを切り替える**
別のシートに切り替えるには:

1. 切り替える**シート タブ**.
1. ドロップダウン メニューからシートを選択します。

エディタが選択したシートに切り替わります。

![todo:画像_代替_文章](4wgvmu8.png)

**使い方？**

ドロップダウン セレクターの値が変更されると、イベントはサーバー上で JSF バックエンド Bean によって処理されます。**ワークシート ビュー**メソッドを使用して**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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

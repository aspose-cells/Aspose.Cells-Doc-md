---
title: スプレッドシート エディター - 関数の操作
type: docs
weight: 60
url: /ja/java/spreadsheet-editor-working-with-functions/
---
**目次**

- [数式バー](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 saveFormulaBarContents
- [関数を挿入する](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **数式バー**
数式バーは、シート領域の上にあるテキスト ボックスです。現在のセルの数式を表示し、ユーザーが編集できるようにします。

**使い方？**

セルを選択すると、数式バーがセルと同期し、数式が表示されます。ユーザーは編集できます。ユーザーが編集して Enter キーを押すと、JavaScript 関数**saveFormulaBarContents**実行される
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **関数を挿入する**
関数または式を挿入するには:

1. セルをクリックして選択します。
1. クリック**挿入機能**上のボタン。
1. の指示に従ってください**挿入機能**ダイアログ。

---
title: スプレッドシートエディター  関数の操作
type: docs
weight: 60
url: /ja/java/spreadsheet-editor-working-with-functions/
---

**目次**

- [数式バー](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [関数の挿入](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **数式バー**
数式バーはシート領域の上にあるテキストボックスです。現在のセルの数式を表示し、ユーザーがそれを編集することを可能にします。

**動作仕様**

セルが選択されると、数式バーが同期されて数式が表示されます。ユーザーは編集が許可されています。ユーザーが編集して Enter キーを押すと、JavaScript 関数**saveFormulaBarContents**が実行されます。
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **関数の挿入**
関数や数式を挿入するには:

1. セルを選択するためにクリックします。
1. 上部の**関数の挿入**ボタンをクリックします。
1. **関数の挿入**ダイアログの指示に従います。

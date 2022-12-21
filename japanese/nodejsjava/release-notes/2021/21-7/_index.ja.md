---
title: Aspose.Cells for Node.js via Java 21.7 リリースノート
type: docs
weight: 6
url: /ja/nodejs-java/aspose-cells-for-node-js-via-java-21-7-release-notes/
---
{{% alert color="primary" %}}

このページには、[Aspose.Cells for Node.js via Java 21.7](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.7/).

{{% /alert %}}

|**鍵**|**概要**|**カテゴリー**|
|:- |:- |:- |
|CELLSJAVA-43477|Aspose.Cells for Java を使用して証明書で VBA コード プロジェクトにデジタル署名する|
|CELLSJAVA-40452|外部データの範囲と詳細を取得する|
|CELLSJAVA-42494|CSS セクションに大量の未使用のスタイルが生成されている|
|CELLSJAVA-41121|SheetRender がフロー チャートを正しくレンダリングしない|
|CELLSJAVA-43331|XLS から HTML への変換中に円内のテキストが欠落する|
|CELLSJAVA-43507|java下にエクセルを挿入するsvgを実行すると異常終了します。|
|CELLSJAVA-41887|ピボット テーブルのパーセンテージ データが HTML で正しく表示されない|
|CELLSJAVA-43482|HTML ドキュメントをワークブックに変換するときに上付き文字と下付き文字が正しく書式設定されない|
|CELLSJAVA-43501|getStringValue() 関数を使用して読み取った値が正しくない|
|CELLSJAVA-43515|MDURATION式の問題|
|CELLSJAVA-43528|作成日時、更新日は抽出できません|
|CELLSJAVA-43529|BuiltInDocumentProperties を抽出できません|
|CELLSJAVA-43530|日時プロパティの結果が異なる|
|CELLSJAVA-41693|TextBox 内の数式が PDF にレンダリングされない|
|CELLSJAVA-43487|Excel から PDF への変換で出力 PDF のテキストが中央に配置されない|
|CELLSJAVA-42867|ODS ファイル形式で形状が取得されない|
|CELLSJAVA-42895|MS Excel チャートの PNG 出力に不一致がある|
|CELLSJAVA-43015|setPrintArea() メソッド使用時の SheetRender.toImage() の問題|
|CELLSJAVA-43258|ワークブックのコピー後にグラフ ポイントのフォントの太字が変更される|
|CELLSJAVA-43436|Aspose Cells は、ダイアグラムで反転された y 軸を無視します|
|CELLSJAVA-43510|Aspose.Cells for Java を使用して Excel ファイルを再保存すると、グラフがめちゃくちゃになる|
|CELLSJAVA-43532|チャート系列名の抽出に関する問題|
|CELLSJAVA-43474|XLS ファイルのロードおよび保存中に形状オブジェクトが変更されました|
|CELLSJAVA-43493|間違ったコメントの作成者が取得されます|
|CELLSJAVA-43527|Aspose.Cells for Java NullPointerException|
|CELLSJAVA-43506|無効なパスワードの例外|

## **Public API および下位互換性のない変更**

以下は、Aspose.Cells for Java に対して行われた下位互換性のない変更と同様に、追加、名前変更、削除、または廃止されたメンバーなど、パブリック API に対して行われた変更のリストです。リストされている変更について懸念がある場合は、 Aspose.Cells サポート フォーラム。

### **PasteOptions.OperationType プロパティと PasteOperationType enum を追加します。**

範囲貼り付け時の操作種別を取得・設定します。

### **PivotFormatCondition.AddColumnAreaCondition(PivotField columnField) メソッドを追加します。**

列フィールドにピボットテーブルの条件付き書式制限を追加します。

### **PivotFormatCondition.AddColumnAreaCondition(String fieldName) メソッドを追加します。**

列フィールドにピボットテーブルの条件付き書式制限を追加します。

### **PivotFormatCondition.AddRowAreaCondition(PivotField rowField) メソッドを追加します。**

行フィールドにピボットテーブルの条件付き書式制限を追加します。

### **PivotFormatCondition.AddRowAreaCondition(String fieldName) メソッドを追加します。**

行フィールドにピボットテーブルの条件付き書式制限を追加します。

### **PivotFormatCondition.AddDataAreaCondition(PivotField dataField) メソッドを追加します。**

データ フィールドにピボットテーブルの条件付き書式の制限を追加します。

### **PivotFormatCondition.AddDataAreaCondition(String fieldName) メソッドを追加します。**

データ フィールドにピボットテーブルの条件付き書式の制限を追加します。

### **PivotFormatCondition.SetConditionalAreas() メソッドを追加します。**

PivotFormatCondition オブジェクトの条件領域を設定します。

### **SeriesCollection.Add(boolean,boolean) メソッドを追加します。**

シリーズを範囲で追加します。

### **SetSeriesNames() メソッドを追加します。**

シリーズの名前として範囲を設定します。


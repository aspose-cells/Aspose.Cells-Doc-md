---
title: Aspose.Cells for Java 8.7.2 リリースノート
type: docs
weight: 120
url: /ja/java/aspose-cells-for-java-8-7-2-release-notes/
---
## **その他の改善と変更**

|**鍵** |**概要** |**カテゴリー** |
|:- |:- |:- |
|CELLSJAVA-41334 |HYPERLINK 式/関数 - ワークシートの Hyperlink コレクションを拡張してオブジェクトを取得します|新機能|
|CELLSJAVA-41788 |順序付きリストの Start' プロパティが正しく機能しない|バグ|
|CELLSJAVA-41763 |Aspose Cells API HTMLファイルの各コンテンツをExcelファイルに変換できない|バグ|
|CELLSJAVA-41759 |スプレッドシートを HTML に保存する際にレイアウトが異なる|バグ|
|CELLSJAVA-41677 |スプレッドシートを HTML に変換すると、定義された名前を指すハイパーリンクがリンク切れになる|バグ|
|CELLSJAVA-41774 |what-if 分析での間違った計算|バグ|
|CELLSJAVA-41748 |ロシアの月名は、Excel と比較して PDF で異なる方法でレンダリングされます|バグ|
|CELLSJAVA-41735 |BMD の通貨形式の Cell は DateTime として検出されます|バグ|
|CELLSJAVA-41648 |SpreadsheetML を XLSX に変換する際に、ロケールに依存する日付形式が固定のカスタム形式に変更される|バグ|
|CELLSJAVA-41777 |出力 XLSB ファイルの問題 - XLS から XLSB への変換|バグ|
|CELLSJAVA-41749 |ヘッダーに画像を設定すると（透かしを作成するため）、フォーマット画像設定がリセットされます|バグ|
|CELLSJAVA-41787 |Excel から PDF への変換に時間がかかる|バグ|
|CELLSJAVA-41762 |スプレッドシートを PDF に変換するときに軸ラベルが重なる|バグ|
|CELLSJAVA-41752 |PDF へのレンダリング中にデータ ラベルが円グラフと重なる|バグ|
|CELLSJAVA-41751 |Chart の PDF 形式では、大文字の水平/垂直軸のタイトル テキストが大文字と小文字で表示されます。|バグ|
|CELLSJAVA-41736 |ワークシートを画像にレンダリングする際のチャートの配置の問題|バグ|
|CELLSJAVA-41755 |Chart の PDF 形式に縦線がありません|バグ|
|CELLSJAVA-41756 |PDF にレンダリングすると、横罫線の太さが実際のグラフの太さよりも大きくなります|バグ|
|CELLSJAVA-41754 |ブックのコピー中に SmartArt がコピーされない|バグ|
|CELLSJAVA-41717 |ODS から XLSX への変換中にチャートの凡例の垂直方向の配置が変更された|バグ|
|CELLSJAVA-41716 |ODS から XLSX への変換中にチャートが見つからない|バグ|
|CELLSJAVA-41636 |Cell フォーマットの問題 - GridWeb (JAVA) で表示値が正しくない|バグ|
|CELLSJAVA-41746 |java.lang.OutOfMemoryError: スプレッドシートを PDF に保存中に GC オーバーヘッドの制限を超えました|例外|
|CELLSJAVA-41768 |ワークシートのコピー中に com.aspose.cells.Name を java.lang.Integer にキャストできない|例外|
## **Public API および下位互換性のない変更**
以下は、Aspose.Cells for .NET に対して行われた下位互換性のない変更と同様に、追加、名前変更、削除、または廃止されたメンバーなど、パブリック API に対して行われた変更のリストです。リストされている変更について懸念がある場合は、 Aspose.Cells サポート フォーラム。
### **TextBoxCollection[string] プロパティを追加します。**
名前でテキスト ボックスを取得します。
### **AbstractCalculationEngine および CalculationData クラスを追加します。**
ユーザーが独自の計算エンジンを実装してデフォルトの計算エンジン Aspose.Cells を拡張するための新しい API。
### **CalculationOptions.CustomEngine プロパティを追加します。**
ユーザーが新しいカスタム計算エンジンを使用して数式を計算できるようにします。

{{% alert color="primary" %}} 

Aspose.Cells for Java のコード ベースは、関連する .NET バージョンのコードと一致するため、Aspose.Cells for .NET v8.7.2 に含まれるほとんどの変更、機能強化、および修正は、この Aspose.Cells for Java v8.7.2 にも含まれています。

{{% /alert %}}

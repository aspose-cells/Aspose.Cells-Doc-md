---
title: スマートマーカーを用いた変数配列のExcelへのスマートなインポート方法
type: docs
weight: 30
url: /ja/net/how-to-import-variable-arrays-with-smart-markers/
---

## **スマートマーカーに変数配列を使用する理由**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. ハードコーディングなしの動的反復：静的マーカーは可変長データ（例：注文アイテム、ユーザー権限）には適さない。配列は動的に反復します。 
2. 簡素化された集計：合計、平均、またはフィルターを直接計算。テンプレート内で手動のJavaScript/C#ロジックを避ける。
3. 表形式/リストデータの表現：自然な適合：表、グリッド、およびリストは本質的に配列にマッピングされる。
4. メモリ効率：配列はテンプレートの複雑さとデータバインディングのオーバーヘッドを削減します。
5. API / データソースとの統合：JSON / 配列中心のデータに対応（例：REST API）。

## **スマートマーカーを使用して可変配列をインポートする方法**
次の例のコードは、スマートマーカーで可変配列を使用する方法を示しています。ワークブックの最初のワークシートのA1セルに可変配列マーカーを配置し、そのマーカーの値を設定し、マーカーに対してデータを埋めるように処理します。最後にExcelファイルを保存します。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **スマートマーカーを使用してHTMLプロパティをインポートする方法**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}

---
title: SmartMarkersで範囲パラメータを使用する方法
type: docs
weight: 10
url: /ja/net/how-to-use-range-parameter-in-smart-markers/
---

## **Smart Markersで範囲パラメータを使用する理由**
SmartMarkersの範囲パラメータは、ソース（例：JSON、データベース）からデータを埋め込む際に、Excelテンプレート内でデータの配置場所と方法を正確に制御するために使用されます。特に、可変長の配列や複雑なグループ化に対応した動的なデータ出力を管理するのに役立ちます。

1. データ配置の制御と重複の防止：データソースに動的配列（例：レコードごとに要素数が異なる）を含む場合、範囲パラメータはデータを定義されたExcel範囲内に収め、隣接するセルやセクションに溢れるのを防ぎます。

2. 動的配列数式の処理：動的配列をトランスポーズ（例：&=TRANSPOSE(DataArray)）する操作の場合、範囲パラメータは出力が実際のデータサイズに適応し、以前の操作から残存する値（例：空欄のゼロ）を残さないようにします。

3. グループ化と階層化のサポート：データのグループ化が必要な場合（例：ネストされたJSON構造）、範囲パラメータは階層的な出力エリアを定義します。例えば、親カテゴリの下にレコードをグループ化し、手動の行調整を避けることができます。範囲が未定義の場合、SmartMarkersはネストされた関係性を正確に表現できない可能性があります。特に、データソースに明示的な階層がない場合。

4. テンプレート設計と一貫性の向上：範囲を指定することで、フォーマット、数式、罫線が出力エリアに一貫して適用されることを保証します。これにより、セルのスタイルの不一致や、生成されたレポート内の壊れた数式の問題を回避できます。

5. パフォーマンスとデータの並べ替えの最適化：範囲パラメータにより、ツールがテンプレートに埋め込む前にデータソースを事前に並べ替えることができ、グループ化されたデータが正しい順序で表示されるようになります。

## **SmartMarkersで範囲パラメータを使用する方法**
時には、SmartMarkersで範囲を並べ替えたり、他の操作を行ったりする必要があります。Aspose.Cellsでは、範囲パラメータの使用が可能です。以下のコードで生成された出力Excelファイルのスクリーンショットとともに、[テンプレートファイル](range.xlsx)と[JSONファイル](range.json)を確認してください。

|**範囲.xlsxファイルの最初のシートに表示されたスマートマーカー**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](range_result.png)|

以下はJSONデータです：
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}

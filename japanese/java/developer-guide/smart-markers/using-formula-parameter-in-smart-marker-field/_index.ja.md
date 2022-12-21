---
title: Smart Marker フィールドで Formula パラメータを使用する
type: docs
weight: 30
url: /ja/java/using-formula-parameter-in-smart-marker-field/
---
## **考えられる使用シナリオ**
スマート マーカー フィールドに数式を埋め込みたい場合があります。この記事では、Formula パラメータを使用してスマート マーカー フィールドに数式を埋め込む方法について説明します。
## **Smart Marker フィールドで Formula パラメータを使用する**
次のサンプル コードは、Test という名前のスマート マーカー変数に数式を埋め込み、そのデータ ソース名も Test であるため、数式パラメーターを含む完全なフィールドは次のようになります。**&=$Test(数式)**コードの実行後、[最終出力Excelファイル](47153156.xlsx)A1からA5までのセルに数式が含まれます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}

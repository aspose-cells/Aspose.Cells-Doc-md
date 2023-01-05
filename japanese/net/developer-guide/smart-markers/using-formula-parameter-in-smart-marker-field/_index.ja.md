---
title: Smart Marker フィールドで Formula パラメータを使用する
type: docs
weight: 40
url: /ja/net/using-formula-parameter-in-smart-marker-field/
---
## **考えられる使用シナリオ**
スマート マーカー フィールドに数式を埋め込みたい場合があります。この記事では、*方式*式をスマート マーカー フィールドに埋め込むためのパラメーター。
## **Smart Marker フィールドで Formula パラメータを使用する**
次のサンプル コードは、TestFormula という名前のスマート マーカー フィールドに数式を埋め込み、そのデータ ソース名は MyDataSource であるため、数式パラメーターを含む完全なフィールドは &=MyDataSource.TestFormula(formula) のようになり、コードの実行後、[最終出力Excelファイル](46465047.xlsx)A1からA5までのセルに数式が含まれます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}

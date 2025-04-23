---
title: Smart MarkerフィールドでFormulaパラメータを使用する
type: docs
weight: 30
url: /ja/java/using-formula-parameter-in-smart-marker-field/
---

## **可能な使用シナリオ**
時々、スマートマーカーフィールドに数式を埋め込みたいことがあります。この記事では、スマートマーカーフィールドに数式を埋め込むためのFormulaパラメータの使用方法について説明します。
## **Smart MarkerフィールドでFormulaパラメータを使用**
次のサンプルコードでは、変数Testとそのデータソース名もTestであるスマートマーカータグに数式を埋め込んだ完全なフィールドが**&=$Test(formula)**のようになります。また、コードの実行後には、[最終出力Excelファイル](47153156.xlsx)にA1からA5までのセルに数式が表示されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
{{< app/cells/assistant language="java" >}}

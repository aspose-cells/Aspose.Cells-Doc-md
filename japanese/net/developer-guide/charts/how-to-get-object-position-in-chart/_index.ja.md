---
title: グラフ内のオブジェクトの位置を取得する方法
description: Excelのグラフ内のオブジェクトの位置を取得する方法について、Aspose.Cells for .NETを使用して学習してください。 
keywords: Aspose.Cells for .NET、Excelグラフ、オブジェクトの位置を取得します。
type: docs
weight: 74
url: /ja/net/how-to-get-object-position-in-chart/
---

## 可能な使用シナリオ
いくつかのシナリオでは、Excelグラフを使用している際に、グラフ内のオブジェクトの位置を取得する必要があります。Aspose.Cellsを使えばこの要件を簡単に実現できます。

## 例：グラフ内のオブジェクト位置の取得

以下のサンプルコードは、[サンプルExcelファイル](TestFile.xlsx)を読み込み、[出力Excelファイル](Output.xlsx)を生成します。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

上記のコードを使用して、チャートのタイトルとチャートのプロットエリアの位置を取得できます。 
位置情報を基に、シェイプを対応する位置に配置することができます。 
結果は次の画像に示されており、1つのシェイプはプロットエリアの左上隅に配置され、もう1つのシェイプはチャートタイトルの下に配置されています。
![todo:image_alt_text](OutputResult.png)

## 単位の説明と変換

グラフ内のオブジェクトの位置には3つの単位があります：

1. グラフエリアの比率単位。

2. 1/4000のグラフエリア単位。これは古いExcelファイルで使用されていた単位で、推奨されません。

3. ピクセル単位。

それらの変換コードは次のコードに示されています： 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}

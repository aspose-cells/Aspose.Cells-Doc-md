---
title: 配置設定
linktitle: 配置設定
description: Aspose.Cellsライブラリでは、ノード.js経由でセルの整列設定を使用してテキストのレイアウトと表示を調整できます。このドキュメントは、セルの整列設定にAspose.Cellsを使用する詳細なステップとサンプルコードを提供します。
keywords: Aspose.Cells、セル整列、水平整列、垂直整列、テキスト折返し Node.js経由のC++
type: docs
weight: 20
url: /ja/nodejs-cpp/cells-alignment-settings/
---

## **配置設定の構成**

### **Microsoft Excelの配置設定**

セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

上記の図から分かるように、異なる種類の配置オプションがあります:

- テキストの配置（水平および垂直）
- インデント
- 方向
- テキスト コントロール。
- テキスト方向。

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。

### **Aspose.Cellsの配置設定**

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。

Aspose.Cellsは、[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)と[**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを提供し、セルの書式設定を取得・設定します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)クラスは整列設定の構成に役立つプロパティを提供します。

任意のテキスト整列タイプを [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) 列挙型から選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype)列挙型に定義されたプリセットのテキスト整列タイプは次の通りです。

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|Bottom| 下部のテキスト配置を表します。
|Center| 中央のテキスト配置を表します。
|CenterAcross| 横方向に中央揃えのテキスト配置を表します。
|Distributed| 分散テキスト配置を表します。
|Fill| 塗りつぶしのテキスト配置を表します。
|General| 一般的なテキスト配置を表します。
|Justify| 両端揃えのテキスト配置を表します。
|Left| 左揃えのテキスト配置を表します。
|Right| 右揃えのテキスト配置を表します。
|Top| 上部のテキスト配置を表します。
|JustifiedLow| アラビア語のテキストに対して調整されたカシダ長でテキストを配置します。
|ThaiDistributed| 特にタイ語のテキストを分散配置し、各文字を単語として扱います。

{{% alert color="primary" %}}

また、[**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-)メソッドを使用して、均等配分設定を適用することもできます。

{{% /alert %}}

#### **水平配置**

[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-)メソッドを使用して、テキストを水平に整列させます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **垂直配置**

水平整列と同様に、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-)メソッドを使用して、テキストを垂直に整列させます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **インデント**

セル内のテキストのインデントレベルを [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) メソッドで設定することが可能です。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **方向**

セル内のテキストの向き（回転角度）を [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) メソッドで設定します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

##### **テキストの折り返し**

セルのテキストの折り返しは、すべてのテキストが収まるようにセルの高さを調整します。これにより、テキストの切り取りや隣接セルへのはみ出しを防ぎます。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-)メソッドを使って折り返しをオンまたはオフに設定します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **収縮に合わせる**

セル内のテキストの折り返しの一つの方法は、セルの寸法に合わせてテキストサイズを縮小することです。これは、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-)メソッドを**true**に設定することで行います。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **セルの結合**

Microsoft Excelのように、Aspose.Cellsは複数のセルを結合して1つにすることをサポートします。Aspose.Cellsはこのタスクに対して2つのアプローチを提供します。一つは [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) メソッドを呼び出す方法です。[**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)メソッドは、セルを結合するために次のパラメータを受け取ります。

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


もう一つは、最初に [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)メソッドを呼び出して、結合するセル範囲を作成し、その範囲の開始と終了を指定した[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)メソッドを実行し、[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)オブジェクトは [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) メソッドも提供し、指定された範囲を [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) オブジェクトにより結合します。

##### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順序は [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) プロパティで設定されます。Aspose.Cellsは、事前定義されたテキスト方向タイプを [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype) 列挙型で提供します。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/nodejs-cpp/line-breaks-and-text-wrapping/)


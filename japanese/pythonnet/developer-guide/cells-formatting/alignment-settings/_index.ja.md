---
title: 配置設定
description: Aspose.Cells for Python via .NETライブラリでは、セルの配置と表示を調整するためにセルの整列設定を使用できます。水平揃え、垂直揃え、テキストの折り返しなどの設定を調整することで、セル内のテキストの流れをより詳細に制御できます。このドキュメントは、Aspose.Cells for Python via .NETでセルの整列設定を使用する方法について詳細な手順とサンプルコードを提供します。
keywords: Aspose.Cells for Python via .NET、セルの整列、水平整列、垂直整列、テキスト折り返し
type: docs
weight: 20
url: /ja/python-net/cells-alignment-settings/
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

これらの整列設定はすべてAspose.Cells for Python via .NETで完全にサポートされており、詳細は以下に記載されています。

### **Aspose.Cells for Python via .NETの整列設定**

Aspose.Cells for Python via .NETは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cells for Python via .NETは、セルの書式を取得・設定するための[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)と[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)メソッドを提供します。[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスは、整列設定を構成するための便利なプロパティを提供します。

[**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) 列挙型を使用して任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) 列挙型の事前定義されたテキスト配置タイプは次のとおりです:

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|GENERAL|一般的なテキスト整列を表す|
|BOTTOM|下部のテキスト整列を表す|
|CENTER|中央のテキスト整列を表す|
|CENTER_ACROSS|横に中央揃えのテキスト整列を表す|
|DISTRIBUTED|分散されたテキスト整列を表す|
|FILL|塗りつぶしのテキスト整列を表す|
|JUSTIFY|両端揃えのテキスト整列を表す|
|LEFT|左寄せのテキスト配置を表す|
|RIGHT|右寄せのテキスト配置を表す|
|TOP|上寄せのテキスト配置を表す|
|JUSTIFIED_LOW|アラビア語テキストのための調整されたカシダの長さでテキストを揃える|
|THAI_DISTRIBUTED|タイ語を特別に分散させる、各文字が単語として扱われるため|

{{% alert color="primary" %}}

また、[**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed) プロパティを使用して両端揃え分散設定を適用できます。

{{% /alert %}}

#### **水平配置**

[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの[**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) プロパティを使用してテキストを水平に配置します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **垂直配置**

水平配置と同様に、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの[**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) プロパティを使用してテキストを垂直に配置します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **インデント**

セル内のテキストのインデントレベルを[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの[**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) プロパティで設定することができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **方向**

セル内のテキストの方向（回転）を[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの[**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) プロパティで設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

##### **テキストの折り返し**

セル内のテキストを折り返すと、テキストが切れたり隣接するセルに流れ出ないようになり、読みやすくなります。テキストの折り返しは、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)の[**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped)プロパティを使用してオンまたはオフに設定できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **収縮に合わせる**

フィールド内のテキストを折り返すオプションは、セルのサイズに合わせてテキストサイズを収縮することもできます。これは、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)の[**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped)プロパティを**true**に設定することで行います。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **セルの結合**

Microsoft Excelのように、Aspose.Cells for Python via .NETは複数のセルを一つに結合することをサポートしています。Aspose.Cells for Python via .NETはこのタスクに2つのアプローチを提供します。ひとつは[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)コレクションの[**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge)メソッドを呼び出す方法です。[**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge)メソッドは次のパラメータを取ってセルを結合します：

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

もう1つの方法は、まず[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)の[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)メソッドを呼び出して結合するセルの範囲を作成する方法です。[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)メソッドは、前述の[**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge)メソッドと同じパラメータを取り、[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)オブジェクトには、[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)オブジェクトで指定された範囲を結合する[**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge)メソッドも用意されています。

##### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順序は、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)オブジェクトの[**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction)プロパティで設定されます。Aspose.Cells for Python via .NETは、[**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype)列挙型にあらかじめ定義されたテキスト方向タイプを提供します。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|CONTEXT|最初に入力された文字の言語と一致した読み取り順|
|LEFT_TO_RIGHT|左から右の読み取り順|
|RIGHT_TO_LEFT|右から左の読み取り順|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}

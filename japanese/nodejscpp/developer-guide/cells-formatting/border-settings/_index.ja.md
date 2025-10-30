---  
title: 罫線設定
linktitle: 罫線設定  
description: C++経由のNode.jsでAspose.Cellsライブラリを使用してセルの枠線スタイルと色を設定する方法。枠線の幅、スタイル、色を調整することで、セルの見た目をより細かくコントロールできます。  
keywords: Aspose.Cells、セルの枠線設定、Node.js経由のC++、枠線の幅、枠線のスタイル、枠線の色  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/cells-border-settings/  
---  

## **セルにボーダーを追加する**  

Microsoft Excelでは、セルに枠線を追加してセルの書式設定を行えます。枠線の種類は追加場所によって異なります。例えば、上枠線はセルのトップ位置に追加されます。ユーザーは線のスタイルや色も変更可能です。  

Aspose.Cells for Node.js via C++を用いて、開発者はExcelと同じ柔軟な方法で枠線を追加し、その見た目をカスタマイズできます。  

### **セルにボーダーを追加する**  

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトです。  

Aspose.Cellsは、[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)メソッドを[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスに提供します。この[**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドはセルの書式設定を行うために使用されます。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)クラスはセルに枠線を追加するためのプロパティを提供します。  

#### **セルに罫線を追加**  

開発者は、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)コレクションを使ってセルに枠線を追加できます。枠線のタイプはインデックスとして[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)コレクションに渡します。すべての枠線タイプは事前に定義された[**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)列挙型に含まれています。  

**境界の列挙**  

|**境界タイプ**|**説明**|  
| :- | :- |  
|BottomBorder|下部の境界線  
|DiagonalDown|左上から右下への対角線  
|DiagonalUp|左下から右上への対角線  
|LeftBorder|左側の境界線  
|RightBorder|右側の境界線  
|TopBorder|上部の境界線  

[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)コレクションはすべての枠線を格納します。[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)コレクション内の各枠線は[**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)オブジェクトで表され、二つのプロパティ[**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-)と[**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-)を持ち、枠線の線の色とスタイルをそれぞれ設定できます。  

枠線の線の色を設定するには、Color列挙型（Node.jsの一部）を使って色を選び、Borderオブジェクトのcolorプロパティに割り当てます。  

枠線のラインスタイルは、[**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype)列挙型からスタイルを選択して設定します。  

**CellBorderType列挙体**  

|**線のスタイル**|**説明**|  
| :- | :- |  
|DashDot|細い点線のような線  
|DashDotDot|細い破線点線のような線  
|Dashed|破線のような線  
|Dotted|点線のような線  
|Double|二重線  
|Hair|細い線  
|MediumDashDot|中くらいの点線のような線  
|MediumDashDotDot|中くらいの破線点線のような線  
|MediumDashed|中くらいの破線のような線  
|None|線なし  
|Medium|中くらいの線  
|SlantedDashDot|対角の中くらいの点線のような線  
|Thick|太い線  
|Thin|細い線  
線スタイルを一つ選び、それを[**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)オブジェクトの[**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-)プロパティに割り当てます。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
線のスタイルと色は同時に設定すべきです。斜めの二つの枠線は同じ線スタイルと色にします。  
{{% /alert %}}  

#### **セルの範囲に境界線を追加する**  

1つのセルだけでなく、範囲に対して枠線を追加することも可能です。そのためには、最初に[**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)メソッドを呼び出し、セル範囲を作成します。引数は以下の通りです：  

- 最初の行、範囲の最初の行。  
- 最初の列、範囲の最初の列を表す。  
- 行数、範囲内の行数。  
- 列数、範囲内の列数。  

[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)メソッドは、指定されたセル範囲を含む[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)オブジェクトは、範囲に枠線を追加するための引数を取る[**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-)メソッドを提供します：  

- **枠線タイプ**：[**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)列挙型から選ばれる枠線タイプ。  
- **ラインスタイル**：枠線のラインスタイル。[**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype)列挙型から選択。  
- **色**、Color 列挙型から選択した線の色。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}

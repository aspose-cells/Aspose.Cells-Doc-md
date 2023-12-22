---
title: Cells 配置を変更し、既存の書式設定を維持する
description: Aspose.Cells ライブラリを使用してセルの配置を変更し、既存の書式設定を保持します
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /ja/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **考えられる使用シナリオ**

場合によっては、複数のセルの配置を変更したいが、既存の書式設定も維持したい場合があります。 Aspose.Cells を使用すると、[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments)財産。 *true** に設定すると、位置合わせの変更が行われます。それ以外の場合は、変更が行われません。ご注意ください、[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトはパラメータとして渡されます[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)実際にセル範囲に書式設定を適用するメソッド。

##  **Cells 配置を変更し、既存の書式設定を維持する**

次のサンプルコードは、[サンプル Excel ファイル](67338585.xlsx) 、範囲を作成し、水平方向と垂直方向に中央揃えにして、既存の書式設定をそのまま保ちます。次のスクリーンショットは、サンプル Excel ファイルと[Excelファイルを出力](67338586.xlsx)セルが水平方向と垂直方向に中央揃えになったことを除き、セルの既存の書式設定がすべて同じであることを示しています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}

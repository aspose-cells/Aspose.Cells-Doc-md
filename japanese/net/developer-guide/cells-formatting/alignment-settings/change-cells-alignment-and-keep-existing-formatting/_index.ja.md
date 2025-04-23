---
title: セルの配置を変更し、既存の書式を保持する
description: Aspose.Cellsライブラリを使用して、セルの配置を変更し、既存の書式設定を保持します
keywords: Aspose.Cells、C＃、セル配置、既存の書式設定を保持
type: docs
weight: 340
url: /ja/net/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

複数のセルの配置を変更したいが、既存の書式設定を保持したい場合、Aspose.Cellsを使用することができます。[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments)プロパティを使用するとそれが可能です。それを**true**に設定すると、配置の変更が適用されますが、そうでない場合は適用されません。また、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトが[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)メソッドにパラメータとして渡され、実際にセルの範囲に書式を適用することになります。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}

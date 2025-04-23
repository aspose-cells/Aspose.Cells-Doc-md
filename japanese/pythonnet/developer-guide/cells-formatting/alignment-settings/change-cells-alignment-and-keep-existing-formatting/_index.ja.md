---
title: セルの配置を変更し、既存の書式を保持する
description: Aspose.Cells for Python via .NETライブラリを使用してセルの配置を変更し、既存の書式を保持する
keywords: Aspose.Cells for Python via .NET、Pythonセル配置、既存の書式を保持
type: docs
weight: 340
url: /ja/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には、複数のセルの配置を変更したいが、既存の書式も保持したい場合があります。Aspose.Cells for Python via .NETはこれを[**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments)プロパティを使用して行うことができます。これを**true**に設定すると配置の変更が行われます。なお、[**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)オブジェクトは[**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style)メソッドのパラメータとして渡され、実際にセル範囲に書式を適用します。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}


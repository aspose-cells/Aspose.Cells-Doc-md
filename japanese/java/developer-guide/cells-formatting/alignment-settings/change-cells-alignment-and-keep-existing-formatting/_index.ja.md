---
title: セルの配置を変更し、既存の書式を保持する
type: docs
weight: 260
url: /ja/java/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には、複数のセルの配置を変更したいときにも、既存の書式を保持したいことがあります。Aspose.Cellsを使用すると、[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments)プロパティを使用してそれを行うことができます。それを**true**に設定すると、配置の変更が適用されますが、それ以外の場合は適用されません。注意してください、[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))メソッドにパラメータとして[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)オブジェクトが渡され、実際にセル範囲に書式を適用するメソッドです。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338592.xlsx)をロードし、範囲を作成し、水平および垂直に中央揃えにして既存の書式を保持します。次のスクリーンショットは、サンプルExcelファイルと[出力Excelファイル](67338591.xlsx)を比較し、セルの既存の書式が変更されていないことを示しています（セルは水平および垂直に中央揃えになっています）。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}

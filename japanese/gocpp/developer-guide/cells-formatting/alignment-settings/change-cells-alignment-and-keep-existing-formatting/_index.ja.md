---
title: Golangを使用してC++経由でセルの配置を変更し、既存の書式設定を維持します
description: Aspose.Cellsライブラリを使用して、セルの配置を変更し、既存の書式設定を保持します
keywords: Aspose.Cells、C++、セルの整列、既存の書式を維持
type: docs
weight: 340
url: /ja/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には、複数のセルの整列を変更したいが、既存の書式設定も維持したい場合があります。Aspose.Cellsはこれを [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/) プロパティを使用して行うことができます。これを **true** に設定すると、整列の変更が適用され、それ以外の場合は適用されません。ご注意：[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)オブジェクトは、実際に範囲に書式を適用する [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) メソッドにパラメータとして渡されます。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}

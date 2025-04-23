---
title: セルの配置を変更し、既存の書式を保持する
linktitle: セルの配置を変更し、既存の書式を保持する
description: Node.jsとC++を使ったセルの配置と既存の書式を維持するためにAspose.Cellsライブラリを使用
keywords: Aspose.Cells、Node.js経由でC++、セルの配置、既存の書式を維持
type: docs
weight: 340
url: /ja/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には複数のセルの配置を変更したいが、既存の書式も維持したい場合があります。Aspose.Cells for Node.js via C++は[**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-)メソッドを使用してこれを可能にします。このメソッドに**true**を設定すると配置の変更が行われ、それ以外の場合は変更されません。なお、[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)オブジェクトは、フォーマットをセル範囲に適用する[**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)メソッドにパラメータとして渡されます。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}

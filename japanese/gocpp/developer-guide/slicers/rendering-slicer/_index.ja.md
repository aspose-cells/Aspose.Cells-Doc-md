---
title: C++経由のGolangによるスライサーのレンダリング
type: docs
weight: 40
url: /ja/go-cpp/rendering-slicer/
description: GolangとC++を使用したAspose.CellsでExcelファイル内のスライサーをレンダリング
---

## **可能な使用シナリオ**
Aspose.Cellsはスライサーのレンダリングをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFまたはHTML形式で保存すると、スライサーが適切にレンダリングされます。
## **スライサーをレンダリングする**
以下のサンプルコードは既存のスライサーを含む[サンプルExcelファイル](67338479.xlsx)を読み込み、スライサーのみをカバーする印刷範囲を設定してシートを画像に変換します。生成された[出力画像](67338480.png)はレンダリングされたスライサーを示しています。ご覧のとおり、スライサーは適切にレンダリングされ、サンプルExcelファイルと同じ見た目になります。

![todo:image_alt_text](rendering-slicer_1)
## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderingSlicer.go" >}}

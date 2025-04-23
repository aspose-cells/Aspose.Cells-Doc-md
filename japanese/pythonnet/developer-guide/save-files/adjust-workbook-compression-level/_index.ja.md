---
title: ワークブックの圧縮レベルを調整する
type: docs
weight: 180
url: /ja/python-net/adjust-workbook-compression-level/
---

## **ワークブックの圧縮レベルを調整する**

開発者は、大きなワークブックを操作する際に、圧縮レベルを調整できます。処理時間よりもファイルサイズを重視する場合やその逆も可能です。Aspose.Cells for Python via .NET は、[**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) 列挙を提供し、これを使用してワークブックの圧縮レベルを設定できます。[**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) 列挙には次のメンバーがあります。

- レベル1：最も速くて効果の低い圧縮。
- レベル2：レベル1よりもやや遅いが、より優れています。
- レベル3：レベル2よりもやや遅いが、より優れています。
- レベル4：レベル3よりもやや遅いが、より優れています。
- レベル5：レベル4よりもやや遅く、より効果的な圧縮。
- レベル6：速度と圧縮効率の良いバランス。
- レベル7：かなり良い圧縮！
- レベル8：レベル7よりも優れた圧縮！
- レベル9："ベスト"の圧縮、ベストは入力データストリームのサイズを最も減らすことを意味します。これは最も遅い圧縮でもあります。

次のコードスニペットは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype)列挙型の使用を示し、Level1、Level6、Level9の変換時間を比較します。また、生成されたファイルのサイズを比較することもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}


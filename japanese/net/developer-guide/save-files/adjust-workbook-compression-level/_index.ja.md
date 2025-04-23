---
title: ワークブックの圧縮レベルを調整する
type: docs
weight: 180
url: /ja/net/adjust-workbook-compression-level/
---

## **ワークブックの圧縮レベルを調整する**

開発者は、より大きなワークブックを扱うときに、ファイルサイズよりも処理時間を優先するか、その逆を優先するかもしれません。Aspose.Cellsは、ワークブックの圧縮レベルを設定するために使用できる[**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)列挙型を提供します。 [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)列挙型は、次のメンバーを提供します。

- レベル1：最も速くて効果の低い圧縮。
- レベル2：レベル1よりもやや遅いが、より優れています。
- レベル3：レベル2よりもやや遅いが、より優れています。
- レベル4：レベル3よりもやや遅いが、より優れています。
- レベル5：レベル4よりもやや遅く、より効果的な圧縮。
- レベル6：速度と圧縮効率の良いバランス。
- レベル7：かなり良い圧縮！
- レベル8：レベル7よりも優れた圧縮！
- レベル9："ベスト"の圧縮、ベストは入力データストリームのサイズを最も減らすことを意味します。これは最も遅い圧縮でもあります。

次のコードスニペットは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)列挙型の使用を示し、Level1、Level6、Level9の変換時間を比較します。また、生成されたファイルのサイズを比較することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

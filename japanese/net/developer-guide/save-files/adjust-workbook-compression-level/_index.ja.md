---
title: ワークブックの圧縮レベルを調整する
type: docs
weight: 180
url: /ja/net/adjust-workbook-compression-level/
---
## **ワークブックの圧縮レベルを調整する**

開発者は、より大きなワークブックを操作するときに、ワークブックの圧縮レベルを調整できます。開発者は、処理時間よりも小さいファイル サイズを優先する場合もあれば、その逆の場合もあります。 Aspose.Cells提供**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**ワークブックの圧縮レベルを設定するために使用できる列挙。の**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**列挙は、次のメンバーを提供します。

- Level1: 最速ですが、効果が最も低い圧縮です。
- レベル 2: レベル 1 より少し遅いですが、より良いです。
- レベル 3: レベル 2 より少し遅いですが、より良いです。
- レベル 4: レベル 3 より少し遅いですが、より良いです。
- レベル 5: レベル 4 よりも少し遅くなりますが、圧縮率が高くなります。
- Level6: 速度と圧縮効率のバランスが良い。
- Level7: かなり良い圧縮!
- Level8: Level7 よりも優れた圧縮率!
- Level9: 「最良」の圧縮。最良とは、入力データ ストリームのサイズを最大限に削減することを意味します。これは、最も遅い圧縮でもあります。

次のコード スニペットは、**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**列挙し、Level1、Level6、および Level9 の変換時間を比較します。生成されたファイルのサイズを比較することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}

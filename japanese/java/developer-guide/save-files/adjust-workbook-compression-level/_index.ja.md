---
title: ワークブックの圧縮レベルを調整する
type: docs
weight: 130
url: /ja/java/adjust-workbook-compression-level/
---
## **ワークブックの圧縮レベルを調整する**

開発者は、より大きなワークブックを操作するときに、ワークブックの圧縮レベルを調整できます。開発者は、処理時間よりも小さいファイル サイズを優先する場合もあれば、その逆の場合もあります。 Aspose.Cells提供**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**ワークブックの圧縮レベルを設定するために使用できる列挙。の**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**列挙は、次のメンバーを提供します。

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: 最速ですが、効果が最も低い圧縮です。
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: レベル 1 より少し遅いですが、より良いです。
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**レベル 2 より少し遅いですが、より良いです。
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: レベル 3 より少し遅いですが、より良いです。
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: レベル 4 よりも少し遅くなりますが、圧縮率が高くなります。
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**：速度と圧縮効率のバランスが良い。
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: なかなかいい圧縮！
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Level7 よりも優れた圧縮率!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**「最良」の圧縮。最良とは、入力データ ストリームのサイズを最大限に削減することを意味します。これは、最も遅い圧縮でもあります。

次のコード スニペットは、**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**列挙し、変換時間を比較します**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**、 と**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**.生成されたファイルのサイズを比較することもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}

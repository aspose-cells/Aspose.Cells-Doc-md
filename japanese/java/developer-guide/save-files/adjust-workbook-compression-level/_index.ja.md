---
title: ワークブックの圧縮レベルを調整する
type: docs
weight: 130
url: /ja/java/adjust-workbook-compression-level/
---

## **ワークブックの圧縮レベルを調整**

開発者は、大きなワークブックを扱う際に、ワークブックの圧縮レベルを調整することができます。開発者は、ファイルサイズを処理時間よりも優先することもできます。Aspose.Cellsは、ワークブックの圧縮レベルを設定するために使用できる[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)列挙型を提供します。[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)列挙型には、次のメンバーが含まれています。

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)：最速ですが、最も効果が低い圧縮です。
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)：レベル1よりも少し遅く、より良い圧縮です。
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)：レベル2よりも少し遅く、より良い圧縮です。
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)：レベル3よりも少し遅く、より良い圧縮です。
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)：レベル4よりも少し遅く、より良い圧縮です。
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)：速度と圧縮効率の良いバランスです。
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)：かなり良い圧縮です！
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)：Level7よりもより良い圧縮です。
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)：最も「良い」圧縮であり、最小の入力データストリームのサイズを最も減少させることを指します。これはまた、最も遅い圧縮です。

下記のコードスニペットでは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)列挙型の使用を示し、[**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)、[**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)、および[**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)の変換時間を比較します。生成されたファイルのサイズを比較することもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}

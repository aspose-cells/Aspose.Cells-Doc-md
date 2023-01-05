---
title: Cells の配置を変更し、既存の書式を維持する
type: docs
weight: 260
url: /ja/java/change-cells-alignment-and-keep-existing-formatting/
---
## **考えられる使用シナリオ**

複数のセルの配置を変更したいが、既存の書式を維持したい場合があります。 Aspose.Cells を使用すると、[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments)財産。設定するなら**真実**、アライメントの変更が行われます。そうでない場合は行われません。ご注意ください、[**スタイルフラグ**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)オブジェクトはパラメータとして渡されます[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) セルの範囲に実際に書式設定を適用するメソッド。

## **Cells の配置を変更し、既存の書式を維持する**

次のサンプル コードは、[サンプル Excel ファイル](67338592.xlsx)、範囲を作成し、中央に配置すると、水平方向と垂直方向に整列され、既存の書式がそのまま維持されます。次のスクリーンショットは、サンプルの Excel ファイルと[出力エクセルファイル](67338591.xlsx)セルが水平方向と垂直方向に中央揃えになっていることを除いて、セルの既存の書式設定はすべて同じであることを示しています。

![todo:画像_代替_文章](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}

---
title: ワークシート内の形状でテキストを回転させる
type: docs
weight: 1300
url: /ja/net/rotate-text-with-shape-inside-the-worksheet/
---
## **考えられる使用シナリオ**

Microsoft Excel を使用して、任意の図形内にテキストを追加できます。非常に古い Microsoft Excel 2003 を使用して図形を追加すると、テキストは図形と共に回転しません。ただし、Microsoft Excel の新しいバージョン (2007、2010、2013、2016 など) を使用して形状を追加すると、テキストは形状と共に回転します。テキストをシェイプに合わせて回転させるかどうかを制御できます。[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)財産。そのデフォルト値は**真実**これは、テキストが形状とともに回転することを意味しますが、次のように設定した場合**間違い**の場合、テキストは形状とともに回転しません。

## **ワークシート内の形状でテキストを回転させる**

次のサンプル コードは、[サンプル Excel ファイル](64716896.xlsx)三角形の形をしており、そのテキストは形に合わせて回転します。 Microsoft Excel でサンプルの Excel ファイルを開いて三角形を回転させると、テキストも一緒に回転します。次に、コードは[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)プロパティとして**間違い**そしてそれをとして保存します[出力エクセルファイル](64716897.xlsx).出力された Excel ファイルを Microsoft Excel で開き、三角形を回転させても、テキストは回転しません。サンプルの Excel ファイルに対するコードの効果を示す次のスクリーンショットを参照してください。

![todo:画像_代替_文章](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}

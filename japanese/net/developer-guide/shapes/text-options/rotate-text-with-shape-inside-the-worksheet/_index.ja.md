---
title: ワークシート内の図形と一緒にテキストを回転する
type: docs
weight: 1300
url: /ja/net/rotate-text-with-shape-inside-the-worksheet/
---

## **可能な使用シナリオ**

Microsoft Excelで任意の図形にテキストを追加できます。Microsoft Excel 2003という非常に古いバージョンで図形を追加すると、テキストは図形とともに回転しません。ただし、Microsoft Excelの新しいバージョン（2007、2010、2013、または2016など）を使用して図形を追加すると、テキストは図形とともに回転します。[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)プロパティを使用して、テキストが図形と一緒に回転するかどうかを制御できます。これのデフォルト値は**true**です。これはテキストが図形と一緒に回転することを意味しますが、**false** に設定すると、テキストは図形と一緒に回転しません。

## **ワークシート内の図形と一緒にテキストを回転する**

次のサンプルコードは、三角形の図形とそのテキストが図形とともに回転する[サンプルエクセルファイル](64716896.xlsx)をロードします。サンプルエクセルファイルをMicrosoft Excelで開き、三角形の図形を回転させると、テキストも一緒に回転します。コード後に、[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)プロパティを**false**に設定し、[出力エクセルファイル](64716897.xlsx)として保存します。今度は、出力エクセルファイルをMicrosoft Excelで開いて三角形の図形を回転させると、テキストは図形と一緒に回転しません。参考のために、コードの効果を示す以下のスクリーンショットをご覧ください。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: ワークシート内の図形と一緒にテキストを回転する
type: docs
weight: 110
url: /ja/java/rotate-text-with-shape-inside-the-worksheet/
---

## **可能な使用シナリオ**

Microsoft Excelを使用して、任意の図形にテキストを追加できます。Microsoft Excel 2003以前を使用して図形を追加すると、テキストは図形と一緒に回転しません。ただし、Microsoft Excel 2007、2010、2013または2016などの新しいバージョンを使用して図形を追加すると、テキストは図形と一緒に回転します。テキストが図形と一緒に回転するかどうかを[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)プロパティを使用して制御できます。デフォルト値は**true**で、これはテキストが図形と一緒に回転することを意味しますが、**false**に設定すると、テキストは図形と一緒に回転しません。

## **ワークシート内の図形と一緒にテキストを回転する**

次のサンプルコードは、図形とそのテキストが一緒に回転する三角形のサンプルExcelファイルをロードします。サンプルExcelファイルをMicrosoft Excelで開き、三角形の図形を回転させると、テキストもそれに従って回転します。次に、[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)プロパティを**false**として設定し、[output Excel file](64716917.xlsx)として保存します。これで、Microsoft Excelで出力Excelファイルを開き、三角形の図形を回転させると、テキストはそれに従って回転しません。参考のために、サンプルExcelファイルへのコードの効果を示すスクリーンショットを参照してください。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}

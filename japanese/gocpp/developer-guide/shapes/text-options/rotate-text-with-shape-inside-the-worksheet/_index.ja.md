---
title: Golangを使ったC++経由でワークシート内のシェイプにテキストを回転させる
linktitle: 図形とともにテキストを回転させる
type: docs
weight: 1300
url: /ja/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aspose.Cells for C++を使用してExcelワークシート内の図形のテキスト回転を制御する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelを使用して任意の図形内にテキストを追加できます。非常に古いMicrosoft Excel 2003を使用して図形を追加すると、テキストは図形とともに回転しません。ただし、Microsoft Excelの新しいバージョン（2007、2010、2013、2016など）を使用して図形を追加すると、テキストも図形とともに回転します。[**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)プロパティを使用して、テキストが図形とともに回転すべきかどうかを制御できます。このプロパティのデフォルト値は**true**であり、テキストは図形とともに回転します。**false**に設定すると、テキストは図形とともに回転しません。

## **ワークシート内の図形と一緒にテキストを回転する**

以下のサンプルコードは、三角形の図形を含むサンプルExcelファイル（64716896.xlsx）を読み込み、その図形とともにテキストが回転する例を示しています。Microsoft ExcelでサンプルExcelファイルを開き、三角形の図形を回転させると、テキストも一緒に回転します。その後、[**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)プロパティを**false**に設定し、[出力Excelファイル](64716897.xlsx)として保存します。次に、Microsoft Excelで出力Excelファイルを開き、三角形の図形を回転させると、テキストは回転しません。コードの効果を示すスクリーンショットも参照してください。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}

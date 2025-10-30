---  
title: Golangを使ったC++経由でワークシート内のコメントやシェイプの余白を設定する  
linktitle: ワークシート内のコメントまたは図形の余白を設定する  
type: docs  
weight: 1500  
url: /ja/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Golangを使ったC++経由でAspose.Cellsを使用してワークシート内のコメントやシェイプの余白を設定する方法。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsでは、[**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/)プロパティを使用して任意の図形やコメントのマージンを設定できます。このプロパティは[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)クラスのオブジェクトを返し、[**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/)、[**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/)、[**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/)、[**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)などのさまざまなプロパティを持ち、上、左、下、右のマージンを設定可能です。  

## **ワークシート内のコメントまたは図形の余白を設定する**  

以下のサンプルコードをご覧ください。これは、2つの図形を含むサンプルExcelファイル（61767851.xlsx）を読み込み、それぞれの図形の上、左、下、右のマージンを設定します。コードによって生成された[出力Excelファイル](61767852.xlsx)と、その効果を示すスクリーンショットを参照してください。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **サンプルコード**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  

---
title: ImageOrPrintOptions の PageIndex および PageCount プロパティを使用したページのシーケンスのレンダリング
type: docs
weight: 100
url: /ja/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用して、Excel ファイルの一連のページを画像にレンダリングできます。[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex)と[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount)プロパティ。これらのプロパティは、ワークシートに非常に多くのページ (たとえば数千ページ) があり、その一部のみをレンダリングしたい場合に役立ちます。これにより、処理時間が節約されるだけでなく、レンダリング プロセスのメモリ消費も節約されます。

## **ImageOrPrintOptions の PageIndex および PageCount プロパティを使用したページのシーケンスのレンダリング**

次のサンプル コードは、[サンプル Excel ファイル](55541812.xlsx)を使用して、ページ 4、5、6、および 7 のみをレンダリングします。[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex)と[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount)プロパティ。コードによって生成されたレンダリングされたページを次に示します。

|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
|:- |:- |
|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}

---
title: ImageOrPrintOptions の PageIndex および PageCount プロパティを使用したページのシーケンスのレンダリング
type: docs
weight: 110
url: /ja/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用して、Excel ファイルの一連のページを画像にレンダリングできます。[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)と[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)プロパティ。これらのプロパティは、ワークシートに非常に多くのページ (たとえば数千ページ) があり、その一部のみをレンダリングしたい場合に役立ちます。これにより、処理時間が節約されるだけでなく、レンダリング プロセスのメモリ消費も節約されます。

## **ImageOrPrintOptions の PageIndex および PageCount プロパティを使用したページのシーケンスのレンダリング**

次のサンプル コードは、[サンプル Excel ファイル](55541781.xlsx)を使用してページ 4、5、6、および 7 のみをレンダリングします。[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)と[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)プロパティ。コードによって生成されたレンダリングされたページを次に示します。

|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
|:- |:- |
|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:画像_代替_文章](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}

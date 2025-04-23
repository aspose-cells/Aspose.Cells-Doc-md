---
title: ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用してページのシーケンスをレンダリングする
type: docs
weight: 110
url: /ja/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **可能な使用シナリオ**

Aspose.Cellsを使用してExcelファイルのページのシーケンスを[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)および[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)のプロパティを使用してイメージにレンダリングできます。これらのプロパティは、ワークシートに多数のページ（数千ページなど）がある場合でも、特定のページのみをレンダリングしたい場合に役立ちます。これにより、処理時間が節約され、レンダリングプロセスのメモリ消費量も節約されます。

## **ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする**

次のサンプルコードは、サンプルExcelファイルをロードし、[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)と[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)のプロパティを使用してページ4、5、6、7のみをレンダリングします。こちらがコードによって生成されたレンダリングされたページです。

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用してページのシーケンスをレンダリングする
type: docs
weight: 10
url: /ja/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする**
Aspose.Cellsを使用してExcelファイルのページを画像にレンダリングするときに、[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) および [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) プロパティが役立ちます。これらのプロパティを使用すると、ワークシートに何千ものページがある場合でも、一部のページのみをレンダリングしたい場合に便利です。これにより処理時間の節約だけでなく、レンダリングプロセスのメモリ消費も節約できます。

次のサンプルコードは、サンプルExcelファイルをロードし、[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) および [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) プロパティを使用してページ4、5、6、7をレンダリングします。以下は、サンプルコードによって生成されたレンダリングされたページの画像です。

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}

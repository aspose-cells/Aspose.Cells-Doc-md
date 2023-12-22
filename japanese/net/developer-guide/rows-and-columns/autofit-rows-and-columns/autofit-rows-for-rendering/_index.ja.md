---
title: レンダリング用に行を自動調整
type: docs
weight: 130
url: /ja/net/autofit-rows-for-rendering/
---
通常、セル内のすべてのテキストを表示したい場合は、Microsoft Excel の標準表示で 100% ズームで行を自動調整できます。これにより、標準表示でテキストが完全に表示され、ファイルを印刷または PDF として保存した場合でも、テキストが正しく表示されます。

ただし、場合によっては、行の自動調整は通常表示では正常に機能しますが、印刷表示に切り替えるか、ファイルを PDF として保存すると、テキストが切り取られてしまいます。ソースファイルを確認してください[Book1.xlsx](Book1.xlsx)そしてスクリーンショット。

![テキストがプリントビューで切り取られる](text_clipped_in_printview.png)

保存された PDF ファイルでテキストがクリップされるのを防ぎたい場合は、行を自動調整できます。[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/)オプション。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

これで、出力 PDF ファイルでテキストがクリップされなくなりました。

![保存された PDF でテキストがクリップされない](text_not_clipped_in_saved_pdf.png)
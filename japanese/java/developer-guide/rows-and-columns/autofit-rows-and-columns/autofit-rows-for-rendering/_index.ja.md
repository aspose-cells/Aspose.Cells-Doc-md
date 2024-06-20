---
title: 描画用に行を自動調整する
type: docs
weight: 130
url: /ja/java/autofit-rows-for-rendering/
---

通常ビューでセル内の全テキストを表示する場合、Microsoft Excel で 100% ズームで通常ビューで行を自動調整できます。これによりテキストが通常ビューで完全に表示され、印刷やファイルを PDF として保存しても、テキストが正しく表示されます。

ただし、ある場合には、通常ビューで行の自動調整が正常に機能しますが、印刷ビューに切り替えたり、ファイルを PDF として保存すると、テキストが切り取られます。 ソースファイル [Book1.xlsx](Book1.xlsx) とスクリーンショットをご確認ください。

![印刷ビューでテキストが切り取られた場合](text_clipped_in_printview.png)

保存した PDF ファイルでテキストが切り取られるのを防止したい場合、[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) オプションを使用して行を自動調整できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

今、テキストは出力された PDF ファイルで切り取られていません。

![保存した PDF でテキストが切り取られていない場合](text_not_clipped_in_saved_pdf.png)

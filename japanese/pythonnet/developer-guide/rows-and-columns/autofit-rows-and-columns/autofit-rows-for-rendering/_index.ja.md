---
title: 描画用に行を自動調整する
type: docs
weight: 130
url: /ja/python-net/autofit-rows-for-rendering/
description: Python via .NET APIを使用して、Aspose.Cells for Python via .NET APIを介してのレンダリングのための行の自動調整方法を学びます。
keywords: Python Excelライブラリ、PythonのレンダリングのためのPython自動調整行、Excelファイルを開いた時に行の高さが自動的に調整されます。 
---

通常ビューでセル内の全テキストを表示する場合、Microsoft Excel で 100% ズームで通常ビューで行を自動調整できます。これによりテキストが通常ビューで完全に表示され、印刷やファイルを PDF として保存しても、テキストが正しく表示されます。

ただし、ある場合には、通常ビューで行の自動調整が正常に機能しますが、印刷ビューに切り替えたり、ファイルを PDF として保存すると、テキストが切り取られます。 ソースファイル [Book1.xlsx](Book1.xlsx) とスクリーンショットをご確認ください。

![印刷ビューでテキストが切り取られた場合](text_clipped_in_printview.png)

保存されたPDFファイルでテキストの切り取りを防止したい場合は、[AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/)のオプションで行の自動調整を行うことができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

今、テキストは出力された PDF ファイルで切り取られていません。

![保存した PDF でテキストが切り取られていない場合](text_not_clipped_in_saved_pdf.png)

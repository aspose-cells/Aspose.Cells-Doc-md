---
title: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for Python via NET を使用して、HTML をインポートする際に行区切り後の余分なスペースを削除する方法を示すトピック。
keywords: HTML をインポートする際に行区切り後の余分なスペースを削除し、html をインポートする際に余分なスペースを削除します。
---

{{% alert color="primary" %}}

改行タグの後に余分なスペースが来る場合は、[**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) プロパティを使用し、**true**に設定してすべての余分なスペースを削除してください。デフォルトではこのプロパティは**false**であり、余分なスペースは出力されたExcelファイルに保持されます。

{{% /alert %}}

HTMLLoadOptions.delete_redundant_spaces プロパティを false と true に設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

次のサンプルコードは [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) プロパティの使用例を示しています。上記のスクリーンショットに示されているように、true または false に設定してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}

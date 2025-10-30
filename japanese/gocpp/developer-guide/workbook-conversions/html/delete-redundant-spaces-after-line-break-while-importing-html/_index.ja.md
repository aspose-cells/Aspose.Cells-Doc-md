---
title: HTMLをインポートする際に改行後の余分な空白を削除する（GolaingとC++経由）
linktitle: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for C++を使用してHTMLをインポートする際に行間の余分なスペースを削除する方法を学びます。
---

{{% alert color="primary" %}}

[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) プロパティを使用し、それを **true** に設定して、改行タグの後に来るすべての余分なスペースを削除してください。デフォルトではこのプロパティは **false** であり、余分なスペースは出力されるExcelファイルに保持されます。

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces プロパティをfalse や trueに設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

次のサンプルコードは [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) プロパティの使用例を示しています。上記のスクリーンショットに示されているように、true または false に設定してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}

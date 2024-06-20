---
title: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

改行タグの後に余分なスペースが来る場合は、[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) プロパティを使用し、**true**に設定してすべての余分なスペースを削除してください。デフォルトではこのプロパティは**false**であり、余分なスペースは出力されたExcelファイルに保持されます。

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces プロパティをfalse や trueに設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

次のサンプルコードは [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) プロパティの使用例を示しています。上記のスクリーンショットに示されているように、true または false に設定してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}

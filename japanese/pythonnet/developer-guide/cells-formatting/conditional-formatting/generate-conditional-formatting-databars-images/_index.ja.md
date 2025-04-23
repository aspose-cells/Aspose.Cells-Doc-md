---
title: 条件付き書式のデータバー画像を生成
description: Aspose.Cells for Python via .NETは、スプレッドシートファイルを操作するためのPythonライブラリです。条件付き書式のデータバーや画像を生成することをサポートしており、セルの値に基づいて表示をカスタマイズできます。この記事では、Aspose.Cells for Pythonを使用して条件付き書式データバーや画像を生成する方法を紹介します。
keywords: Aspose.Cells for Python via .NET、条件付き書式、データバー、画像、スプレッドシート
type: docs
weight: 40
url: /ja/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時には、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image)メソッドを使用してこれらの画像を生成できます。この記事では、Aspose.Cells for Python via .NETを使用してデータバーの画像を生成する方法を示します。

{{% /alert %}}

次のサンプルコードは、セルC1のDataBar画像を生成します。まず、セルの書式条件オブジェクトにアクセスし、そのオブジェクトから、[**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar)オブジェクトにアクセスして、その[**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image)メソッドを使用してセルの画像を生成します。最後に、画像をディスクに保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}

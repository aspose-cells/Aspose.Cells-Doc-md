---
title: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 270
url: /ja/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for Python via .NET API を通じて、セルの値がシングルクォートマークで始まるかどうかを検索する方法を学びます。
keywords: Python Excel ライブラリ、シングルクォートマークで値が始まるセルを検索するPython
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、シングルクォートマークで値が始まるセルを見つけるための [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) プロパティを提供します。このプロパティがない場合、sample や 'sample などの文字列を区別する方法がありません。

{{% /alert %}}

以下のサンプルコードは、sampleと 'sampleのような文字列を[**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/)プロパティで区別できないことを説明します。そのため、それらを区別するには[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)プロパティを使用する必要があります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
{{< app/cells/assistant language="python-net" >}}

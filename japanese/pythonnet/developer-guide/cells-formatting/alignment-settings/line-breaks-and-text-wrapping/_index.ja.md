---
title: 改行とテキストの折り返し
description: Aspose.Cells for Python via .NETライブラリを使用してテキスト折返しと自動改行を実装する方法。Aspose.Cells for Python via .NETを使えば、セル内に簡単にテキストを挿入し、手動のword wrapや自動改行などの方法を設定できます。このドキュメントはこれらの機能の実装方法を詳細に説明し、サンプルコードも提供します。
keywords: Aspose.Cells for Python via .NET、改行、テキスト折返し、テキストレイアウト
type: docs
weight: 60
url: /ja/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

{{% /alert %}}

## **セル内でテキストを折り返す**

セル内でテキストを折り返すには、[**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped)プロパティを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **明示的な改行を使用する**

C#では、セル内に明示的な改行を挿入するために、「\n」、VB.NETでは「vbLf」を使用できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

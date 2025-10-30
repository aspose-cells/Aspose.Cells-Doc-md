---
title: Überprüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 270
url: /de/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Erfahren Sie, wie Sie feststellen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt, durch die Aspose.Cells for Python via .NET API.
keywords: Python Excel Bibliothek, Python Suchen Sie den Zellenwert, der mit einem einfachen Anführungszeichen beginnt, Python Suchen Sie den Zellenwert, der mit einem einfachen Anführungszeichen beginnt
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET bietet jetzt die [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)-Eigenschaft, um festzustellen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenfolgen wie Beispiel und 'Beispiel usw. zu unterscheiden.

{{% /alert %}}

Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie Muster und 'Muster nicht mit der [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/)-Eigenschaft differenziert werden können. Daher müssen wir die [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)-Eigenschaft verwenden, um sie zu unterscheiden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
{{< app/cells/assistant language="python-net" >}}

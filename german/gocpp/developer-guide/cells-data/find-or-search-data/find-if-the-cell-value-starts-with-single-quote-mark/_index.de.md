---
title: Ob der Zellwert mit Anführungszeichen beginnt, mit Golang via C++ suchen
linktitle: Überprüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 270
url: /de/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ feststellen, ob der Zellwert mit einem einzelnen Anführungszeichen beginnt.
keywords: Prüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Suchen Sie den Zellenwert, der mit einem einfachen Anführungszeichen beginnt.
---

{{% alert color="primary" %}}

Aspose.Cells bietet jetzt die [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) Eigenschaft, um zu überprüfen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenfolgen wie Muster und 'Muster usw. zu unterscheiden.

{{% /alert %}}

Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie Muster und 'Muster nicht mit der [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)-Eigenschaft differenziert werden können. Daher müssen wir die [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)-Eigenschaft verwenden, um sie zu unterscheiden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}

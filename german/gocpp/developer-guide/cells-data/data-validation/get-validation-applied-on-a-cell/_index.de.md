---
title: Auf Validation in einer Zelle angewandte Validierung mit Golang via C++ abrufen
linktitle: Angewendete Validierung auf einer Zelle erhalten.
type: docs
weight: 200
url: /de/go-cpp/get-validation-applied-on-a-cell/
description: In diesem Artikel wird gezeigt, wie man Validierung auf eine Zelle mit Golang via C++ anwendet.
keywords: Zellvalidierung in Excel mit C++ anwenden, Validierung auf eine Zelle in Excel mit C++ anwenden, Validierung in Excel mit C++, Zellvalidierung in Excel mit C++, C++ Zellvalidierung in Excel, C++ Validierung auf eine Zelle in Excel, C++ Zellvalidierung in Excel, C++ Zellvalidierung
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die auf eine Zelle angewendete Validierung zu erhalten. Aspose.Cells bietet die [**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/) Methode für diesen Zweck. Wenn keine Validierung auf die Zelle angewendet wird, gibt sie null zurück.

Ebenso können Sie die [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/) Methode verwenden, um die auf eine Zelle angewendete Validierung durch Angabe ihrer Zeilen- und Spaltenindizes zu erhalten.

{{% /alert %}}

## C++ Code zum Erhalten der auf eine Zelle angewendeten Validierung

Der folgende Code zeigt, wie Validierungen auf eine Zelle angewendet werden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## Verwandte Artikel

- [Datenüberprüfung](/cells/de/cpp/data-validation/)

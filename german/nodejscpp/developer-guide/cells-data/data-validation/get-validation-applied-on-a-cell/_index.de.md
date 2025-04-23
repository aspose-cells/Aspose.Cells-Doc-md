---
title: Angewendete Validierung auf einer Zelle erhalten.
type: docs
weight: 200
url: /de/nodejs-cpp/get-validation-applied-on-a-cell/
description: Dieser Artikel zeigt, wie man Validierung auf eine Zelle mit Node.js über C++ anwendet.
keywords: Wenden Sie Zellvalidierung in Excel mit Node.js über C++ an, Validierung auf eine Zelle in Excel mit Node.js über C++ anwenden, Validierung in Excel mit Node.js über C++, Zellvalidierung in Excel mit Node.js über C++, Node.js über C++ wendet Zellvalidierung in Excel an, Node.js über C++ wendet Validierung auf eine Zelle in Excel an, Node.js über C++ Zellvalidierung in Excel
---

{{% alert color="primary" %}}

Sie können Aspose.Cells für Node.js verwenden, um die auf eine Zelle angewendete Validierung abzurufen. Aspose.Cells bietet dafür die [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--)-Methode. Wenn keine Validierung auf die Zelle angewendet ist, gibt sie null zurück.

Ebenso können Sie die [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) Methode verwenden, um die auf eine Zelle angewendete Validierung durch Angabe ihrer Zeilen- und Spaltenindizes zu erhalten.

{{% /alert %}}

## Node.js-Code zum Abrufen der auf eine Zelle angewendeten Validierung

Der folgende Code zeigt, wie Validierungen auf eine Zelle angewendet werden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Verwandte Artikel

- [Datenüberprüfung](/cells/de/nodejs-cpp/data-validation/)

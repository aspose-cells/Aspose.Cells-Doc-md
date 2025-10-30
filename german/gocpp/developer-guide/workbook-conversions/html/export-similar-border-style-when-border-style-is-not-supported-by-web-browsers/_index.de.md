---
title: Exportiere ähnlichen Rahmenstil, wenn Rahmenstil von Webbrowsern nicht unterstützt wird, mit Golang via C++
linktitle: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird
type: docs
weight: 70
url: /de/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Lerne, wie man ähnliche Rahmenstile exportiert, wenn sie von Webbrowsern nicht unterstützt werden, mit Aspose.Cells und Golang via C++.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel unterstützt einige Arten von durchgezogenen Grenzen, die vom Webbrowser nicht unterstützt werden. Wenn Sie eine solche Excel-Datei mit Aspose.Cells in HTML umwandeln, werden diese Grenzen entfernt. Allerdings unterstützt Aspose.Cells auch die Anzeige solcher Grenzen mit der [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)-Eigenschaft. Bitte setzen Sie deren Wert auf **true**; die unsupported borders werden dann ebenfalls in die HTML-Datei exportiert.

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716806.xlsx), die einige unsupported borders enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht außerdem die Auswirkung der [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)-Eigenschaft innerhalb des [Ausgabe-HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}

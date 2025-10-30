---
title: Deaktivieren Sie CSS beim Speichern als HTML mit Golang über C++
linktitle: CSS beim Speichern in HTML deaktivieren
type: docs
weight: 320
url: /de/go-cpp/disable-css-while-saving-to-html/
description: Erfahren Sie, wie Sie CSS beim Speichern von Excel Dateien als HTML mit Aspose.Cells for C++ deaktivieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei auf HTML für eine einzelne Seite speichern, werden die CSS-Elemente normalerweise innerhalb der HTML-Datei eingebettet und befinden sich im HEAD-Bereich. Wenn Sie diese Datei als Inhalt/Bilder eines E-Mails anhängen, werden die CSS-Elemente von den meisten E-Mail-Clients entfernt, was zu einer schlechten Darstellung führt. Version 24.12 von Aspose.Cells führt eine Option ein, mit der Sie CSS optional deaktivieren können, sodass Styles direkt innerhalb der HTML-Elemente angewendet werden können. Wenn Sie HTML als Inhalt/Bilder des E-Mails setzen möchten, verwenden Sie bitte die Property [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) und setzen Sie sie auf **true**.

## **CSS beim Speichern in HTML deaktivieren**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/)-Eigenschaft.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}

---
title: Disable Exporting Frame Scripts and Document Properties with Golang via C++
type: docs
weight: 310
url: /go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Disable exporting frame scripts and document properties using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells exports frame scripts and document properties when converting a workbook into HTML. The 8.6.0 version of Aspose.Cells for C++ introduces an option that allows you to optionally disable exporting frame scripts and document properties. Please use the `HtmlSaveOptions.ExportFrameScriptsAndProperties` property to disable the export.

{{% /alert %}}

## **Disable Exporting Frame Scripts and Document Properties**

The following sample code allows you to disable exporting frame scripts and document properties. Once you convert a workbook into HTML, the output file will not contain any frame scripts or document properties.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
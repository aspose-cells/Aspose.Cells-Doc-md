---
title: Disable Exporting Frame Scripts and Document Properties
type: docs
weight: 310
url: /python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET exports frame scripts and document properties while converting a workbook into HTML. The 8.6.0 version of Aspose.Cells for Python via .NET introduces an option which allows you optionally disable exporting frame scripts and document properties. Please use the HtmlSaveOptions.ExportFrameScriptsAndProperties property to disable the export.

{{% /alert %}}

## **Disable exporting frame scripts and document properties**

The following sample code allows you to disable exporting frame scripts and document properties. Once you convert a workbook into HTML, the output file will not contain any frame scripts and document properties.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
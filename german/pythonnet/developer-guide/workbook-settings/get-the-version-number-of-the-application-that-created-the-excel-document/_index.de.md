---
title: Ermitteln Sie die Versionsnummer der Anwendung, die das Excel Dokument erstellt hat
type: docs
weight: 210
url: /de/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Oft ist es notwendig, die Versionsnummer der Anwendung zu kennen, die ein Microsoft Excel-Dokument erstellt hat. Aspose.Cells für Python via .NET bietet die [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version)-Eigenschaft zu diesem Zweck.

{{% /alert %}}

Der folgende Beispielcode zeigt die Verwendung der [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version)-Eigenschaft. Er lädt Excel-Dateien, die mit Microsoft Excel 2003, 2007, 2010 und 2013 erstellt wurden, und gibt die Versionsnummer der Anwendung aus, die diese Excel-Dokumente erstellt hat.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

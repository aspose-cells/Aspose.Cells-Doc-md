---
title: Получить номер версии приложения, создавшего документ Excel
type: docs
weight: 210
url: /ru/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Часто необходимо знать номер версии приложения, создавшего документ Microsoft Excel. Aspose.Cells для Python via .NET предоставляет свойство [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version) для этой цели.

{{% /alert %}}

Следующий образец кода демонстрирует использование свойства [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version). Он загружает файлы Excel, созданные в Microsoft Excel 2003, 2007, 2010 и 2013, и выводит номер версии приложения, создавшего эти документы Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}

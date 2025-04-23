---
title: Получить номер версии приложения, создавшего документ Excel
type: docs
weight: 210
url: /ru/net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Часто вам нужно знать номер версии приложения, создавшего документ Microsoft Excel. Aspose.Cells предоставляет свойство [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/version) для этой цели.

{{% /alert %}}

Следующий образец кода демонстрирует использование свойства [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/version). Он загружает файлы Excel, созданные в Microsoft Excel 2003, 2007, 2010 и 2013, и выводит номер версии приложения, создавшего эти документы Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-GetApplicationVersion-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: Установить пользовательский источник данных для WorkbookDesigner
type: docs
weight: 60
url: /ru/net/set-custom-datasource-for-workbookdesigner/
---
Aspose.Cells предоставляет возможность установить собственный источник данных для WorkbookDesigner. API предоставляет перегруженный метод[WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5)который принимает имя источника в качестве первого параметра и экземпляр класса, который реализует[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)как второй параметр.

Следующий фрагмент кода демонстрирует использование[WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5)метод для установки пользовательского источника данных.
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-1.cs" >}}

Реализация*источник данных клиента*, *Покупатель*, а также*список клиентов* классы приведены ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}

Исходный и выходной файлы Excel прилагаются для ознакомления.

[Исходный файл](95584319.xlsx)

[Выходной файл](95584320.xlsx)

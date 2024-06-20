---
title: Экспорт DataTable из GridWeb
type: docs
weight: 70
url: /ru/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, экспорт
description: В этой статье рассматривается экспорт DataTable в GridWeb.
---

{{% alert color="primary" %}} 

[Импорт DataView в GridWeb](/cells/ru/net/aspose-cells-gridweb/import-dataview-to-gridweb/) говорит о импорте содержимого DataView в элемент управления Aspose.Cells.GridWeb. В этой статье обсуждается экспорт данных из элемента управления Aspose.Cells.GridWeb в DataTable.

{{% /alert %}} 
## **Экспорт данных листа**
### **В определенную DataTable**
Экспорт данных листа в определенный объект DataTable:

1. Добавьте элемент управления Aspose.Cells.GridWeb на свою веб-форму.
1. Создайте конкретный объект DataTable.
1. Экспортируйте данные выбранных ячеек в указанный объект DataTable.

В приведенном ниже примере создается конкретный объект DataTable с четырьмя столбцами. Данные листа экспортируются, начиная с первой ячейки, все строки и столбцы видимы на листе, в уже созданный объект DataTable.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **В новый DataTable**
Иногда вам не нужно создавать объект DataTable, а просто экспортировать данные листа в новый объект DataTable.

В приведенном ниже примере показывается другой способ использования метода Export. Он берет ссылку на активный лист и экспортирует полные данные этого листа в новый объект DataTable. Объект DataTable теперь может быть использован в любом нужном вам способе. Например, его можно связать с элементом управления GridView для просмотра данных.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

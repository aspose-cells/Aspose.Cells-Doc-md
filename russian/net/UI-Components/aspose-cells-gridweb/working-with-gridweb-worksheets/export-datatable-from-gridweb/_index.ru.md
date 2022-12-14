---
title: Экспорт DataTable из GridWeb
type: docs
weight: 70
url: /ru/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[Импорт DataView в GridWeb](/cells/ru/net/import-dataview-to-gridweb/)говорил об импорте содержимого DataView в элемент управления Aspose.Cells.GridWeb. В этом разделе обсуждается экспорт данных из элемента управления Aspose.Cells.GridWeb в DataTable.

{{% /alert %}} 
## **Экспорт данных рабочего листа**
### **К определенной таблице данных**
Чтобы экспортировать данные рабочего листа в определенный объект DataTable:

1. Добавьте элемент управления Aspose.Cells.GridWeb в свою веб-форму.
1. Создайте определенный объект DataTable.
1. Экспортировать данные выбранных ячеек в указанный объект DataTable.

В приведенном ниже примере создается определенный объект DataTable с четырьмя столбцами. Данные рабочего листа экспортируются, начиная с первой ячейки со всеми строками и столбцами, видимыми на листе, в уже созданный объект DataTable.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **К новой таблице данных**
Иногда вы не хотите создавать объект DataTable, а просто должны экспортировать данные рабочего листа в новый объект DataTable.

В приведенном ниже примере используется другой способ показать использование метода Export. Он берет ссылку на активный рабочий лист и экспортирует полные данные этого рабочего листа в новый объект DataTable. Объект DataTable теперь можно использовать как угодно. Например, можно привязать объект DataTable к GridView для просмотра данных.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}

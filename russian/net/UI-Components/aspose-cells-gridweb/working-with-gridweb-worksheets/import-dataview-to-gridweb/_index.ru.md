---
title: Импорт DataView в GridWeb
type: docs
weight: 60
url: /ru/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, импорт
description: В этой статье рассматривается вопрос импорта данных в GridWeb.
---

{{% alert color="primary" %}} 

С появлением платформы Microsoft .NET Framework появился новый способ хранения данных. Теперь существуют объекты DataSet, DataTable и DataView, которые хранят данные в автономном режиме. Эти объекты очень удобны в качестве репозиториев данных. С помощью Aspose.Cells.GridWeb можно импортировать данные из объектов DataTable или DataView в листы. Aspose.Cells.GridWeb поддерживает только импорт данных из объекта DataView, но объект DataTable также может быть использован косвенно. Давайте рассмотрим эту функцию подробнее.

{{% /alert %}} 
## **Импорт данных из DataView**
Импорт данных из объекта DataView с использованием метода ImportDataView элемента управления GridWeb в коллекции GridWorsheetCollection. Передайте методу ImportDataView объект DataView, из которого вы хотите импортировать данные. Во время импорта можно указать заголовок столбца и стили данных.

{{% alert color="primary" %}} 

При импорте данных из объекта DataView создается новый лист, чтобы хранить импортированные данные. Лист называется так же, как и DataTable.

{{% /alert %}} 

**Результат: Данные импортированы из DataView в новый лист** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Ширины столбцов корректируются для отображения всех данных, которые они содержат. Когда данные импортируются из DataView, ширина столбцов не корректируется автоматически. Пользователь должен самостоятельно корректировать их. Для программной корректировки ширин столбцов обратитесь к [Изменение размеров строк и столбцов](/cells/ru/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Перегруженная версия метода ImportDataView позволяет разработчикам указать имя листа, который содержит импортированные данные, а также определенное количество строк и столбцов для импорта из объекта DataView.

{{% /alert %}}

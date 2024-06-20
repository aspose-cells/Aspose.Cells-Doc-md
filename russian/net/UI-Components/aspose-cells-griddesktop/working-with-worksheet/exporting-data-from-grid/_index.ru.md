---
title: Экспорт данных из сетки
type: docs
weight: 60
url: /ru/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop,экспорт,данные,экспорт данных
description: Эта статья представляет способы экспорта данных в GridDesktop.
---

{{% alert color="primary" %}} 

В предыдущей теме мы говорили о импорте содержимого DataTable в элемент управления Aspose.Cells.GridDesktop, но специально не упомянули, что Aspose.Cells.GridDesktop также поддерживает обратный процесс. Поэтому в этой теме мы обсудим экспорт данных из элемента управления Aspose.Cells.GridDesktop в DataTable.

{{% /alert %}} 
## **Экспорт содержимого сетки**
### **Экспорт в конкретный объект DataTable**
Для экспорта содержимого сетки в конкретный объект DataTable выполните следующие шаги:Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Form**.

- Создайте конкретный объект DataTable в соответствии с вашими потребностями.
- Экспортируйте данные выбранного **Worksheet** в ваш указанный объект DataTable.

В приведенном ниже примере мы создали конкретный объект DataTable с четырьмя столбцами внутри. Наконец, мы экспортировали данные листа (начиная с первой ячейки с 69 строками и 4 столбцами) в ранее созданный нами объект DataTable.

**Пример:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Экспорт в новый объект DataTable**
Иногда разработчики могут не заинтересоваться созданием собственного объекта DataTable и могут просто захотеть экспортировать данные листа в новый объект DataTable. Для разработчиков это был бы самый быстрый способ экспорта данных.

В приведенном ниже примере мы попробовали другой способ объяснить использование метода ExportDataTable. Мы использовали ссылку на лист, который в данный момент активен, а затем экспортировали полные данные этого активного листа в новый объект DataTable. Теперь этот объект DataTable может быть использован любым образом, как разработчик пожелает. Например, разработчик может привязать этот объект DataTable к DataGrid для просмотра данных.

**Пример:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

В данном случае мы используем перегруженную версию метода ExportDataTable, которая просто вернет новый объект DataTable, содержащий данные, экспортированные с листа.

{{% /alert %}}

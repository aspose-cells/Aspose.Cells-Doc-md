---
title: Управление элементами управления ячейками в колонках
type: docs
weight: 100
url: /ru/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, элементы управления, управление
description: В этой статье рассматривается, как установить элемент управления в колонке GridDesktop.
---

{{% alert color="primary" %}} 

В этой теме обсуждаются некоторые важные концепции управления элементами управления ячеек в колонках с использованием API Aspose.Cells.GridDesktop. Мы объясним, как разработчик может получить доступ, модифицировать и удалить элементы управления ячеек из колонок их листов. Давайте посмотрим на это.

{{% /alert %}} 
## **Доступ к элементам управления ячейками**
Для доступа и изменения существующего элемента управления ячейкой в колонке разработчики могут использовать свойство CellControl объекта Aspose.Cells.GridDesktop.Data.GridColumn. Как только элемент управления ячейкой будет доступен, разработчики могут изменять его свойства во время выполнения. Например, в приведенном ниже примере мы получили доступ к существующему элементу CheckBox из определенной колонки Aspose.Cells.GridDesktop.Data.GridColumn и изменили его свойство Checked.

ВАЖНО: Свойство CellControl предоставляет элемент управления ячейкой в форме объекта CellControl. Поэтому, если вам нужно получить доступ к определенному типу элемента управления ячейкой, скажем CheckBox, то вам нужно выполнить приведение типа объекта CellControl к классу CheckBox.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Удаление элементов управления ячейками**
Чтобы удалить существующий элемент управления ячейкой, разработчики могут просто получить доступ к желаемому листу и затем удалить элемент управления из определенной колонки, используя метод RemoveCellControl объекта Aspose.Cells.GridDesktop.Data.GridColumn.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Каждая колонка в коллекции Columns объекта Worksheet представлена экземпляром класса Aspose.Cells.GridDesktop.Data.GridColumn.

{{% /alert %}}

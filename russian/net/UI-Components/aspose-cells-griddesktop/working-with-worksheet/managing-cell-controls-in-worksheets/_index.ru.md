---
title: Управление ячейками в таблицах
type: docs
weight: 130
url: /ru/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop, элемент управления ячейками, элемент управления, элементы управления
description: В этой статье рассматривается работа с элементами управления ячейками в GridDesktop.
---

{{% alert color="primary" %}} 

Эта тема обсуждает некоторые важные концепции управления элементами управления ячеек с использованием API Aspose.Cells.GridDesktop. Мы объясним, как разработчик может получить доступ, изменить и удалить элементы управления ячеек из их таблиц. Давайте посмотрим на это.

{{% /alert %}} 
## **Доступ к элементам управления ячейками**
Чтобы получить доступ к существующему элементу управления ячейкой на листе, разработчики могут получить доступ к конкретному элементу управления ячейками из коллекции Controls рабочего листа, указав ячейку (с использованием имени ячейки или ее местоположения в терминах номеров строки и столбца), в которой отображается элемент управления ячейкой. После доступа к элементу управления ячейкой разработчики могут изменять его свойства во время выполнения. Например, в приведенном ниже примере мы получили доступ к существующему элементу управления CheckBox с листа и изменили его свойство Checked.

**ВАЖНО:** Коллекция Controls содержит все типы элементов управления ячеек в форме объектов CellControl. Таким образом, если вам нужно получить доступ к конкретному типу элемента управления ячейками, например, к CheckBox, вам нужно выполнить приведение объекта CellControl к классу CheckBox.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Удаление элементов управления ячейками**
Для удаления существующего элемента управления ячейкой разработчики могут просто получить доступ к нужному листу, затем удалить элемент управления ячейкой из коллекции Controls рабочего листа, указав ячейку (по имени или номерам строки и столбца), содержащую элемент управления ячейкой.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}

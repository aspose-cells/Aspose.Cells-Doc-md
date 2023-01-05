---
title: Управление элементами управления Cell в столбцах
type: docs
weight: 100
url: /ru/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

В этом разделе обсуждаются некоторые важные концепции управления элементами управления ячейками в столбцах с использованием Aspose.Cells.GridDesktop API. Мы объясним, как разработчик может получить доступ, изменить и удалить элементы управления ячейками из столбцов своих рабочих листов. Давайте посмотрим на это.

{{% /alert %}} 
## **Доступ к элементам управления Cell**
 Чтобы получить доступ к существующему элементу управления ячейкой в столбце и изменить его, разработчики могут использовать свойство CellControl элемента управления.**Aspose.Cells.GridDesktop.Data.GridColumn** . После доступа к ячейке разработчики могут изменять ее свойства во время выполнения. Например, в приведенном ниже примере мы получили доступ к существующему**Флажок** управление ячейкой от определенного**Aspose.Cells.GridDesktop.Data.GridColumn** и изменил его свойство Checked.

**ВАЖНЫЙ:** Свойство CellControl предоставляет элемент управления ячейкой в виде**Сотовый контроль**объект. Итак, если вам нужно получить доступ к определенному типу управления ячейкой, скажем**Флажок** тогда вам придется типизировать**Сотовый контроль** Возражать**Флажок** учебный класс.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Снятие Cell элементов управления**
 Чтобы удалить существующий элемент управления ячейкой, разработчики могут просто получить доступ к нужному рабочему листу, а затем**Удалять** элемент управления ячейкой из определенного столбца с помощью**RemoveCellControl** метод**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Каждый столбец в**Столбцы** коллекция**Рабочий лист** представлен экземпляром**Aspose.Cells.GridDesktop.Data.GridColumn** учебный класс.

{{% /alert %}}

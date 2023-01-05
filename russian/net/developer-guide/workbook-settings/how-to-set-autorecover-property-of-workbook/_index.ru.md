---
title: Как установить свойство автоматического восстановления книги
type: docs
weight: 220
url: /ru/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для установки свойства автоматического восстановления книги. Значение по умолчанию для этого свойства**истинный** . Когда вы установите его**ЛОЖЬ** в книге Microsoft Excel отключает автовосстановление (автосохранение) в этом файле Excel.

 Aspose.Cells предоставляет[**Книга.Настройки.Автовосстановление**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) свойство, чтобы включить или отключить эту опцию.

{{% /alert %}}

 Следующий код объясняет, как использовать[**Книга.Настройки.Автовосстановление**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) свойство трудовой книжки. Код сначала считывает значение по умолчанию этого свойства, которое**истинный** , то он устанавливает его как**ЛОЖЬ** и сохраняет книгу. Затем он снова читает книгу и считывает значение этого свойства, которое**ЛОЖЬ** на данный момент.

## Код C# для установки свойства автоматического восстановления книги

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Вывод**

Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

---
title: Как установить свойство автоматического восстановления книги
type: docs
weight: 160
url: /ru/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Вы можете использовать Aspose.Cells для установки свойства автоматического восстановления книги. Значение по умолчанию для этого свойства**истинный** . Когда вы установите его**ЛОЖЬ**в книге Microsoft Excel отключает автовосстановление (автосохранение) в этом файле Excel.

 Aspose.Cells предоставляет[**Книга.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) свойство, чтобы включить или отключить эту опцию.

{{% /alert %}}

## Код Java для установки свойства автоматического восстановления книги

 Следующий код объясняет, как использовать[**Книга.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) свойство трудовой книжки. Код сначала считывает значение по умолчанию этого свойства, которое**истинный** , то он устанавливает его как**ЛОЖЬ** и сохраняет книгу. Затем он снова читает книгу и считывает значение этого свойства, которое в данный момент является ложным.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Вывод, сгенерированный образцом кода

Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}

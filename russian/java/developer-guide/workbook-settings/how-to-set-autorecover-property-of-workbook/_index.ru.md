---
title: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 160
url: /ru/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells, чтобы установить свойство AutoRecover рабочей книги. Значение по умолчанию этого свойства - **true**. Когда вы устанавливаете его **false** для рабочей книги, Microsoft Excel отключает автоматическое восстановление (автосохранение) для этого файла Excel.

Aspose.Cells предоставляет свойство [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) для включения или отключения этой опции.

{{% /alert %}}

## Код на Java для установки свойства AutoRecover в Рабочей книге

Следующий код объясняет, как использовать свойство [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) рабочей книги. Код сначала считывает значение этого свойства, которое по умолчанию **true**, затем устанавливает его как **false** и сохраняет рабочую книгу. Затем он снова считывает рабочую книгу и значение этого свойства, которое в этот момент равно false.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Результат, сгенерированный образцом кода

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

---
title: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 220
url: /ru/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для Python via .NET для установки свойства AutoRecover рабочего файла. Значение по умолчанию этого свойства — **true**. Когда вы установите его **false** для рабочей книги, Microsoft Excel отключит автоматическое восстановление (автосохранение) этого файла.

Aspose.Cells для Python via .NET предоставляет свойство [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) для включения или отключения этой опции.

{{% /alert %}}

Следующий код объясняет, как использовать свойство [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) рабочей книги. Сначала он читает значение по умолчанию этого свойства, которое — **true**, затем устанавливает его как **false** и сохраняет рабочую книгу. Потом он снова читает рабочую книгу и получает значение этого свойства, которое на данный момент — **false**.

## Код C# для установки свойства AutoRecover книги

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Вывод**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}


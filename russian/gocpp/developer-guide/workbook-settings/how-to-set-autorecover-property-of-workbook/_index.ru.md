---
title: Как установить свойство AutoRecover книги с помощью Golang через C++
linktitle: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 220
url: /ru/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Научитесь включать или отключать свойство AutoRecover рабочей книги с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для установки свойства AutoRecover рабочей книги. Значение по умолчанию — **true**. Когда вы установите его в **false**, Microsoft Excel отключит автоматическое восстановление (Авосохранение) для этого файла Excel.

Aspose.Cells предоставляет свойство [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) для включения или отключения этой опции.

{{% /alert %}}

Следующий код объясняет, как использовать свойство [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) рабочей книги. Сначала он читает значение по умолчанию этого свойства, которое равно **true**, затем устанавливает его в **false** и сохраняет рабочую книгу. Потом он снова читает рабочую книгу и проверяет значение этого свойства, которое в этот момент — **false**.

## C++ код для установки свойства AutoRecover рабочей книги

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Вывод**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

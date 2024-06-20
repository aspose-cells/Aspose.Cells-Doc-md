---
title: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 220
url: /ru/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells, чтобы установить свойство AutoRecover книги. Значение по умолчанию этого свойства **true**. Когда вы устанавливаете его **false** для книги, Microsoft Excel отключает AutoRecover (автосохранение) для этого файла Excel.

Aspose.Cells предоставляет свойство [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) для включения или отключения этой опции.

{{% /alert %}}

Следующий код объясняет, как использовать свойство [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) рабочей книги. Код сначала считывает значение по у умолчанию этого свойства, которое **true**, а затем устанавливает его в **false** и сохраняет книгу. Затем он снова считывает книгу и считывает значение этого свойства, которое в этот момент **false**.

## Код C# для установки свойства AutoRecover книги

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Вывод**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

---
title: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Шаблон утилизации используется только для объектов, которые имеют доступ к неуправляемым ресурсам, таким как файлы и дескрипторы каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективен в извлечении неиспользуемых управляемых объектов, но он не способен извлекать неуправляемые объекты.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) объект теперь реализует интерфейс *System.IDisposable*, который имеет один метод [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). Вы можете либо непосредственно вызывать метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose), либо использовать оператор *Using* для автоматического вызова этого метода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}

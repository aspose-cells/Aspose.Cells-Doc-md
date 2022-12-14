---
title: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**Рабочая книга.Утилизировать()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) способ освобождения неуправляемых ресурсов[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)объект. Шаблон удаления используется только для объектов, которые обращаются к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективно освобождает неиспользуемые управляемые объекты, но не может освобождать неуправляемые объекты.

{{% /alert %}}

[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) объект теперь реализует*System.IDisposable* интерфейс, который имеет единственный метод[**Утилизировать()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Вы можете либо напрямую позвонить в[**Рабочая книга.Утилизировать()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) метод или вы можете использовать*С использованием*оператор для автоматического вызова этого метода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}

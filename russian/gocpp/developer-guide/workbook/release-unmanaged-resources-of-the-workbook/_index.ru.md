---
title: Обеспечьте освобождение неуправляемых ресурсов рабочей книги с помощью Golang через C++
linktitle: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Узнайте, как освобождать неуправляемые ресурсы рабочей книги с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Шаблон утилизации используется только для объектов, которые имеют доступ к неуправляемым ресурсам, таким как файлы и дескрипторы каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективен в извлечении неиспользуемых управляемых объектов, но он не способен извлекать неуправляемые объекты.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) объект теперь реализует интерфейс *IDisposable*, который имеет один метод [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). Вы можете либо напрямую вызвать метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/), либо использовать оператор *Using* для автоматического вызова этого метода.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}

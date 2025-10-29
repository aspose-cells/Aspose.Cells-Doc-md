---
title: Объединяйте файлы с помощью Golang через C++
linktitle: Объединить файлы
type: docs
weight: 20
url: /ru/go-cpp/merge-files/
description: Узнайте, как эффективно объединять файлы Excel, используя Aspose.Cells for C++.
---

## **Введение**

Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) для объединения нескольких книг, а метод [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) — для копирования листов в новую книгу. Эти методы просты в использовании и эффективны, но при большом количестве файлов их использование может потреблять много ресурсов системы. Чтобы этого избежать, используйте статический метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells**

Следующий пример показывает, как объединять большие файлы, используя метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/). Он берет два простых, но больших файла, Book1.xls и Book2.xls. Эти файлы содержат отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, картинки, комментарии или другие объекты, могут не объединяться при использовании этого метода. Более того, используется кешированный файл для временного хранения данных процесса.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}

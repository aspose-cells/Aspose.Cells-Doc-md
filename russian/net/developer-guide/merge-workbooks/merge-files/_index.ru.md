---
title: Объединить файлы
type: docs
weight: 20
url: /ru/net/merge-files/
---

## **Введение**

Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine), чтобы объединить несколько рабочих книг, и метод [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index), чтобы скопировать листы в новую рабочую книгу. Эти методы легко использовать и эффективны, но если у вас много файлов для объединения, то вы можете обнаружить, что они занимают много системных ресурсов. Чтобы избежать этого, используйте статический метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells**

Приведенный ниже образец кода иллюстрирует, как объединить большие файлы с использованием метода [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). Он берет два простых, но больших файла, Book1.xls и Book2.xls. Файлы содержат только отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, картинки, комментарии или другие объекты, возможно, не будут объединены с использованием этого метода. Кроме того, для процесса используется кэшированный файл, в котором хранятся временные данные.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}

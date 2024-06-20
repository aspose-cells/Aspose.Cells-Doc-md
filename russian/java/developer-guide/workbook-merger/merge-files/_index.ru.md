---
title: Объединить файлы
type: docs
weight: 10
url: /ru/java/merge-files/
---

## **Введение**

Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) для объединения нескольких книг, а метод [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) можно использовать для копирования листов в новую книгу. Эти методы легко использовать и эффективны, но если у вас много файлов для объединения, вы можете обнаружить, что они занимают много ресурсов системы. Для избежания этого используйте статический метод CellsHelper.mergeFiles, более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells**

Приведенный ниже образец кода иллюстрирует способ объединения больших файлов с использованием метода CellsHelper.mergeFiles. Он берет два простых, но больших файла, MyBook1.xls и MyBook2.xls. Файлы содержат отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод CellsHelper.mergeFiles поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, изображения, комментарии или другие объекты, возможно, не будут объединены с помощью этого метода. Кроме того, для процесса используется кэшированный файл для временного хранения данных.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}

---
title: Объединить файлы
type: docs
weight: 10
url: /ru/java/merge-files/
---

## **Введение**

Aspose.Cells предоставляет несколько способов объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) для объединения нескольких рабочих книг, а для копирования листов в новую книгу — метод [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-). Эти методы просты в использовании и эффективны, однако при большом количестве файлов для объединения они могут потреблять много системных ресурсов. Чтобы этого избежать, используйте статический метод CellsHelper.mergeFiles — более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells**

Приведенный ниже образец кода иллюстрирует способ объединения больших файлов с использованием метода CellsHelper.mergeFiles. Он берет два простых, но больших файла, MyBook1.xls и MyBook2.xls. Файлы содержат отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод CellsHelper.mergeFiles поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, изображения, комментарии или другие объекты, возможно, не будут объединены с помощью этого метода. Кроме того, для процесса используется кэшированный файл для временного хранения данных.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: Объединить файлы
type: docs
weight: 20
url: /ru/python-net/merge-files/
---

## **Введение**

Aspose.Cells для Python via .NET предоставляет разные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) для объединения нескольких книг, а метод [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) для копирования листов в новую книгу. Эти методы просты в использовании и эффективны, но при большом количестве файлов их производительность может снижаться. Чтобы этого избежать, используйте статический метод [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files), более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells для Python via .NET**

Приведенный ниже образец кода иллюстрирует, как объединить большие файлы с использованием метода [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). Он берет два простых, но больших файла, Book1.xls и Book2.xls. Файлы содержат только отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, картинки, комментарии или другие объекты, возможно, не будут объединены с использованием этого метода. Кроме того, для процесса используется кэшированный файл, в котором хранятся временные данные.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

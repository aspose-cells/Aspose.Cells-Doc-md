---
title: Объединить файлы
type: docs
weight: 20
url: /ru/net/merge-files/
---
## **Введение**

 Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами[**Рабочая книга.Объединить()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) можно использовать для объединения нескольких рабочих книг, а[**Рабочий лист.Копировать()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)Метод можно использовать для копирования листов в новую книгу. Эти методы просты в использовании и эффективны, но если вам нужно объединить много файлов, вы можете обнаружить, что они требуют много системных ресурсов. Чтобы этого избежать, используйте[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)статический метод, более эффективный способ объединения нескольких файлов.

## **Объединить файлы с помощью Aspose.Cells**

 В следующем примере кода показано, как объединить большие файлы с помощью[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)метод. Требуется два простых, но больших файла, Book1.xls и Book2.xls. Файлы содержат только отформатированные данные и формулы.

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) Метод поддерживает только слияние данных, стилей, форматирования и формул. Такие объекты, как диаграммы, изображения, комментарии или другие объекты, нельзя объединять с помощью этого метода. Кроме того, кэшированный файл используется для хранения временных данных процесса.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}

---
title: Преобразование текста в столбцы
type: docs
weight: 10
url: /ru/python-java/convert-text-to-columns/
---

## **Преобразование текста в столбцы**
Вы можете преобразовать свой текст в столбцы, используя Microsoft Excel. Эта функция доступна из *Инструменты данных* вкладки *Данные*. Для разделения содержимого столбца на несколько столбцов данные должны содержать определенный разделитель, такой как запятая (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells также предоставляет эту функцию с помощью метода [TextToColumns](https://reference.aspose.com/cells/python/asposecells.api/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)). В следующем фрагменте кода демонстрируется использование метода [TextToColumns](https://reference.aspose.com/cells/python/asposecells.api/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) для преобразования текста в столбцы с пробелом в качестве разделителя.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "RowsAndColumns-ConvetTextToColumns.py" >}}

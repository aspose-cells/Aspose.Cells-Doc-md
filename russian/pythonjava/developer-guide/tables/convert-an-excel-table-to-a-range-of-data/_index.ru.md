---
title: Преобразовать таблицу Excel в диапазон данных
type: docs
weight: 10
url: /ru/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Конвертировать таблицу Excel в диапазон данных**
Aspose.Cells для Python via Java предоставляет опцию конвертации таблицы Excel в диапазон данных. Для этого API предоставляет метод [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). Нижеприведенный фрагмент кода демонстрирует использование метода [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) для конвертации таблицы Excel в диапазон данных.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Конвертировать таблицу Excel в диапазон данных с опциями**
Вы можете предоставить дополнительные параметры при конвертации таблицы в диапазон данных с помощью класса [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). Можно передать экземпляр класса [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) в метод [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)), чтобы указать дополнительные параметры. Нижеприведенный фрагмент кода демонстрирует использование класса [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) для установки последнего индекса строки таблицы. Оформление таблицы будет сохранено до указанного индекса строки, а остальное оформление будет удалено.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}

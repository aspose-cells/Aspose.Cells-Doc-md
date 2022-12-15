---
title: Преобразование таблицы Excel в диапазон данных
type: docs
weight: 10
url: /ru/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Преобразование таблицы Excel в диапазон данных**
 Aspose.Cells for Python via Java предоставляет возможность конвертировать таблицу Excel в диапазон данных. Для этого API предоставляет[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) метод. Следующий фрагмент кода демонстрирует использование[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)для преобразования таблицы Excel в диапазон данных.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Преобразование таблицы Excel в диапазон с параметрами**
Вы можете указать дополнительные параметры при преобразовании таблицы в диапазон с помощью[Таблетторангеоптионс](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) учебный класс. Вы можете передать экземпляр[Таблетторангеоптионс](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)класс к[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) для указания дополнительных параметров. Следующий фрагмент кода демонстрирует использование[Таблетторангеоптионс](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)class для установки индекса последней строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}

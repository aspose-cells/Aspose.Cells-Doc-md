---
title: Форматирование объекта списка
type: docs
weight: 30
url: /ru/python-java/formatting-list-object/
---
## **Форматирование объекта списка**
Таблица — это последовательность строк и столбцов, которые содержат связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию для каждого столбца в таблице включена фильтрация в строке заголовка, что позволяет быстро фильтровать или сортировать данные объекта списка. Вы можете добавить итоговую строку (специальную строку в списке, которая предоставляет выбор агрегатных функций, полезных для работы с числовыми данными) в объект списка, который предоставляет раскрывающийся список агрегатных функций для каждой ячейки итоговой строки.

Aspose.Cells поддерживает форматирование объектов списка. Для этого API предоставляет[СписокОбъект](https://reference.aspose.com/cells/python/asposecells.api/ListObject) и[TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType) классы.[TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType)содержит константы, представляющие встроенные стили таблиц. Следующий фрагмент кода создает новый объект списка и задает для него тип стиля таблицы[ТАБЛИЦА_СТИЛЬ_MEDIUM_10](https://reference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10)



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}

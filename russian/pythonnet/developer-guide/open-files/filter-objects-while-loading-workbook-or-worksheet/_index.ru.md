---
title: Фильтрование объектов при загрузке книги Excel или листа
type: docs
weight: 330
url: /ru/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) при фильтрации данных из рабочей книги. Но если вы хотите фильтровать данные из отдельных листов, вам потребуется переопределить метод [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). Укажите соответствующее значение из перечисления [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) при создании или работе с [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

Перечисление [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) имеет следующие возможные значения.

- Все
- Настройки книги
- Пустая ячейка
- Булева ячейка
- Данные ячейки
- Ошибка ячейки
- Числовая ячейка
- Строковая ячейка
- Значение ячейки
- Chart
- Условное форматирование
- Проверка данных
- Определенные имена
- Свойства документа
- Формула
- Гиперссылки
- ОбъединеннаяОбласть
- СводнаяТаблица
- Настройки
- Фигура
- ДанныеЛиста
- НастройкиЛиста
- Структура
- Стиль
- Таблица
- VBA
- XmlMap
## **Фильтрование объектов при загрузке книги Excel**
Приведенный ниже образец кода демонстрирует, как фильтровать диаграммы из книги Excel. Пожалуйста, проверьте [образец excel файла](5115258.xlsx), использованный в этом коде, и [выходной PDF](5115257.pdf), сгенерированный им. Как видно из выходного PDF, все диаграммы были отфильтрованы из книги Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}


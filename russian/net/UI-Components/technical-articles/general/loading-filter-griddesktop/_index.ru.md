---
title: Фильтрация объектов при загрузке книги в GridDesktop
type: docs
weight: 1060
url: /ru/net/aspose-cells-griddesktop/loading-filter
description: В этой статье описывается, как использовать фильтр загрузки для библиотеки Aspose.Cells.GridDesktop.
---
## **Возможные сценарии использования**
 Пожалуйста, используйте[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)свойство при фильтрации данных из книги.

[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)перечисление имеет следующие значения.
- Все
- Настройки книги
- Пустая ячейка
- CellBool
- CellData
- CellError
- ЯчейкаЧисловой
- CellString
- CellValue
- Диаграмма
- Условное форматирование
- Проверка данных
- Дефайнеднамес
- Свойства документа
- Формула
- Гиперссылки
- Объединенная область
- сводная таблица
- Настройки
- Форма
- Данные листа
- Параметры листа
- Структура
- Стиль
- Стол
- VBA
- XmlMap
## **Фильтровать данные при загрузке книги**
 В следующем примере кода показано, как отфильтровать рисунок из книги. Пожалуйста, проверьте[образец эксель файла](5472489.xlsx) . Как видите, все диаграммы/фигуры/изображения были отфильтрованы из рабочей книги.
![рабочая тетрадь без изображения](nodrawing.png)
### **Образец кода**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}
 
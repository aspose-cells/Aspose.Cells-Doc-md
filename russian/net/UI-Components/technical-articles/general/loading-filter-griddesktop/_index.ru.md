---
title: Фильтрация объектов при загрузке книги в GridDesktop
type: docs
weight: 1060
url: /ru/net/aspose-cells-griddesktop/loading-filter
description: Эта статья описывает, как использовать фильтр загрузки в GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) при фильтрации данных из книги.

Перечисление [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) имеет следующие значения.
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
## **Фильтрация данных при загрузке книги**
Приведенный ниже образец кода иллюстрирует, как фильтровать чертежи из книги. Пожалуйста, проверьте [образец файла Excel](5472489.xlsx). Как видите, все диаграммы/фигуры/изображения были отфильтрованы из книги.
![книга без изображений](nodrawing.png)
### **Образец кода**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}


---
title: Фильтруйте объекты при загрузке рабочей книги или листа с помощью Golang через C++
linktitle: Фильтрование объектов при загрузке книги Excel или листа
type: docs
weight: 330
url: /ru/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Узнайте, как фильтровать объекты такие как диаграммы, фигуры и условное форматирование при загрузке книг или листов с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) при фильтрации данных из рабочей книги. Но если вы хотите фильтровать данные из отдельных листов, вам нужно переопределить метод [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Укажите соответствующее значение из перечисления [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) при создании или работе с [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

Перечисление [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) содержит следующие возможные значения.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Фильтрование объектов при загрузке Листа**
Приведенный ниже образец кода загружает [исходный файл Excel](5115255.xlsx) и фильтрует следующие данные из его листов, используя пользовательский фильтр.

- Он фильтрует Диаграммы из листа с именем NoCharts.
- Он фильтрует формы из листа с именем NoShapes.
- Он фильтрует Условное форматирование из листа с именем NoConditionalFormatting.

После загрузки [исходного файла Excel](5115255.xlsx) с пользовательским фильтром он берет изображения со всех листов один за другим. Здесь представлены изображения для вашего ознакомления. Как видно, на первом изображении нет диаграмм, на втором - нет фигур, на третьем - нет условного форматирования.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
Вот как использовать класс CustomLoadFilter согласно именам листов.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}

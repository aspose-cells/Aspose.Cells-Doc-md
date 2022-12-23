---
title: Фильтровать объекты при загрузке книги или листа
type: docs
weight: 330
url: /ru/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Возможные сценарии использования**
Пожалуйста, используйте[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)свойство при фильтрации данных из книги. Но если вы хотите отфильтровать данные с отдельных рабочих листов, вам придется переопределить[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)метод. Укажите соответствующее значение из[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)перечисление при создании или работе с[Загрузить фильтр](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)перечисление имеет следующие возможные значения.

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
- Валидация данных
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
- Таблица
- VBA
- XmlMap
## **Фильтровать объекты при загрузке книги**
 В следующем примере кода показано, как фильтровать диаграммы из книги. Пожалуйста, проверьте[образец эксель файла](5115258.xlsx) используется в этом коде и[вывод PDF](5115257.pdf)порожденный им. Как вы можете видеть в выводе PDF, все диаграммы были отфильтрованы из рабочей книги.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Фильтровать объекты при загрузке рабочего листа**
 Следующий пример кода загружает[исходный файл excel](5115255.xlsx) и фильтрует следующие данные из своих рабочих листов, используя настраиваемый фильтр.

- Он фильтрует диаграммы из рабочего листа с именем NoCharts.
- Он фильтрует фигуры из рабочего листа с именем NoShapes.
- Он фильтрует условное форматирование из листа с именем NoConditionalFormatting.

 Один раз он загружает[исходный файл excel](5115255.xlsx) с пользовательским фильтром он берет изображения всех рабочих листов одно за другим. Вот выходные изображения для справки. Как видите, на первом изображении нет диаграмм, на втором изображении нет фигур, а на третьем изображении нет условного форматирования.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Вот как использовать класс CustomLoadFilter в соответствии с именами рабочих листов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}

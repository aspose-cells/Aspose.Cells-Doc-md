---
title: Валидация данных
type: docs
weight: 90
url: /ru/net/data-validation/
description: Узнайте, как добавить проверку данных с помощью Aspose.Cells for .NET API.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft Excel предоставляет несколько полезных функций для автоматической фильтрации или проверки данных рабочего листа. Aspose.Cells полностью поддерживает функции проверки данных Excel и автофильтра. В этой статье объясняется, как использовать функции Microsoft Excel и как их кодировать с помощью Aspose.Cells.

{{% /alert %}}

##  **Типы проверки данных и ее выполнение**

Проверка данных — это возможность устанавливать правила, относящиеся к данным, введенным на листе. Например, используйте проверку, чтобы убедиться, что столбец с надписью ДАТА содержит только даты или что другой столбец содержит только числа. Вы даже можете убедиться, что столбец с надписью ДАТА содержит только даты в определенном диапазоне. Благодаря проверке данных вы можете контролировать, что вводится в ячейки на листе.

Microsoft Excel поддерживает несколько различных типов проверки данных. Каждый тип используется для управления типом данных, вводимых в ячейку или диапазон ячеек. Ниже фрагменты кода иллюстрируют, как это проверить:

- Numbers являются целыми, то есть не имеют десятичной части.
- Десятичные числа имеют правильную структуру. В примере кода определено, что диапазон ячеек должен иметь два десятичных пробела.
- Значения ограничены списком значений. Проверка списка определяет отдельный список значений, которые можно применить к ячейке или диапазону ячеек.
- Даты попадают в определенный диапазон.
- Время находится в определенном диапазоне.
- Текст имеет заданную длину символов.

###  **Проверка данных с помощью Microsoft Excel**

Чтобы создать проверки с помощью Microsoft Excel:

1. На листе выберите ячейки, к которым вы хотите применить проверку.
1.  Из**Данные** меню выберите *Проверка**. Откроется диалоговое окно проверки.
1.  Нажмите кнопку**Настройки** вкладку и введите настройки.

###  **Проверка данных с помощью Aspose.Cells**

Проверка данных — это мощная функция проверки информации, введенной в рабочие листы. Благодаря проверке данных разработчики могут предоставлять пользователям список вариантов выбора, ограничивать ввод данных определенным типом или размером и т. д.
 В Aspose.Cells каждый[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)в классе есть[**Валидации**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) свойство, которое представляет собой совокупность[**Проверка**](https://reference.aspose.com/cells/net/aspose.cells/validation) объекты. Чтобы настроить проверку, установите некоторые из[**Проверка**](https://reference.aspose.com/cells/net/aspose.cells/validation)свойства класса следующим образом:

- Тип – представляет тип проверки, который можно указать с помощью одного из предопределенных значений в[**Тип Валидации**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)перечисление.
-  Оператор – представляет оператор, который будет использоваться при проверке, который может быть указан с помощью одного из предопределенных значений в[**Тип Оператора**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)перечисление.
- Формула1 — представляет значение или выражение, связанное с первой частью проверки данных.
- Формула2 – представляет значение или выражение, связанное со второй частью проверки данных.

 Когда[**Проверка**](https://reference.aspose.com/cells/net/aspose.cells/validation) свойства объекта настроены, разработчики могут использовать[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)структура для хранения информации о диапазоне ячеек, который будет проверен с помощью созданной проверки.

####  **Типы проверки данных**

[**Тип Валидации**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)перечисление имеет следующие члены:

|**Имя участника**|**Описание**|
| :- | :- |
|AnyValue|Обозначает значение любого типа.|
|Целое число|Обозначает тип проверки для целых чисел.|
|Десятичная дробь|Обозначает тип проверки десятичных чисел.|
|Список|Обозначает тип проверки раскрывающегося списка.|
|Дата|Обозначает тип проверки для дат.|
|Время|Обозначает тип проверки для времени.|
|Длина текста|Обозначает тип проверки длины текста.|
|Обычай|Обозначает пользовательский тип проверки.|

#####  **Проверка целочисленных данных**

При этом типе проверки пользователи могут вводить в проверяемые ячейки только целые числа в пределах указанного диапазона. В следующих примерах кода показано, как реализовать тип проверки WholeNumber. В примере создается та же проверка данных с использованием Aspose.Cells, которую мы создали с помощью Microsoft Excel выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **Проверка данных списка**

Этот тип проверки позволяет пользователю вводить значения из раскрывающегося списка. Он предоставляет список: серию строк, содержащих данные. В этом примере добавляется второй лист для хранения источника списка. Пользователи могут выбирать значения только из списка. Областью проверки является диапазон ячеек A1:A5 на первом листе.

 Здесь важно установить[**Валидация.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)свойство в *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **Проверка данных даты**

При этом типе проверки пользователи вводят в проверяемые ячейки значения дат в пределах заданного диапазона или отвечающие определенным критериям. В этом примере пользователю разрешено вводить даты в диапазоне от 1970 до 1999 года. Здесь областью проверки является ячейка B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **Проверка данных времени**

При этом типе проверки пользователи могут вводить в проверенные ячейки время в пределах заданного диапазона или соответствующее некоторым критериям. В этом примере пользователю разрешено вводить время с 09:00 до 11:30. Здесь областью проверки является ячейка B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **Проверка данных длины текста**

При этом типе проверки пользователи могут вводить текстовые значения указанной длины в проверенные ячейки. В этом примере пользователю разрешено вводить строковые значения длиной не более 5 символов. Областью проверки является ячейка B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **Правила проверки данных**

 Когда реализована проверка данных, ее можно проверить, назначив различные значения в ячейках.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) может использоваться для получения результата проверки. В следующем примере эта функция демонстрируется с разными значениями. Образец файла можно скачать по следующей ссылке для тестирования:

[образецDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **Проверьте, является ли проверка в ячейке раскрывающимся списком.**

 Как мы видели, существует множество типов проверок, которые можно реализовать внутри ячейки. Если вы хотите проверить, является ли проверка раскрывающимся списком или нет,[**Валидация.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)свойство можно использовать для проверки этого. В следующем примере кода показано использование этого свойства. Образец файла для тестирования можно скачать по следующей ссылке:

[образецValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **Добавить CellArea к существующей проверке**

 Могут быть случаи, когда вы захотите добавить[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)существующим[**Проверка**](https://reference.aspose.com/cells/net/aspose.cells/validation). Когда вы добавляете[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) с использованием[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells проверяет все существующие области, чтобы определить, существует ли уже новая область. Если файл имеет большое количество проверок, это снижает производительность. Чтобы преодолеть эту проблему, API предоставляет[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) метод.*checkПересечение* Параметр указывает, следует ли проверять пересечение данной области с существующими областями проверки. Установка его на**ЛОЖЬ** отключит проверку других областей.*checkEdge*Параметр указывает, следует ли проверять обработанные области. Если новая область становится верхней левой областью, внутренние настройки перестраиваются. Если вы уверены, что новая область не является верхней левой областью, вы можете установить для этого параметра значение *false**.

Следующий фрагмент кода демонстрирует использование[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) метод добавления новых[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)существующим[**Проверка**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Исходный и выходной файлы Excel прилагаются для справки.

[Исходный файл](96928093.xlsx)

[Выходной файл](96928220.xlsx)


##  **Предварительные темы**
- [Получите подтверждение Cell в файлах ODS.](/cells/ru/net/get-cell-validation-in-ods-files/)
- [Получите подтверждение по телефону Cell](/cells/ru/net/get-validation-applied-on-a-cell/)
- [Убедитесь, что значение Cell удовлетворяет правилам проверки данных.](/cells/ru/net/verify-that-cell-value-satisfies-data-validation-rules/)

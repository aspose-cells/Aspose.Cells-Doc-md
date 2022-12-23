---
title: Валидация данных
type: docs
weight: 70
url: /ru/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel предоставляет несколько полезных функций для автоматической фильтрации или проверки данных рабочего листа.

[Валидация данных](/cells/ru/java/data-validation/) это возможность устанавливать правила, относящиеся к данным, введенным на листе. Например, используйте проверку, чтобы убедиться, что столбец с надписью ДАТА содержит только даты или что другой столбец содержит только числа. Вы даже можете убедиться, что столбец с надписью DATE содержит только даты в определенном диапазоне. С проверкой данных вы можете контролировать, что вводится в ячейки на листе. Aspose.Cells полностью поддерживает функции проверки данных и автофильтра Microsoft Excel. В этой статье объясняется, как использовать функции в Microsoft Excel и как кодировать их с помощью Aspose.Cells.

{{% /alert %}} 
## **Типы проверки данных и выполнение**
Microsoft Excel поддерживает ряд различных типов проверки данных. Каждый тип используется для контроля того, какой тип данных вводится в ячейку или диапазон ячеек. Ниже фрагменты кода иллюстрируют, как это проверить:

- [Numbers целые](/cells/ru/java/data-validation/)то есть, что они не имеют десятичной части.
- [Десятичные числа следуют правильной структуре](/cells/ru/java/data-validation/). В примере кода определяется, что диапазон ячеек должен содержать два десятичных пробела.
- [Значения ограничены списком значений](/cells/ru/java/data-validation/). Проверка списка определяет отдельный список значений, которые можно применить к ячейке или диапазону ячеек.
- [Даты попадают в определенный диапазон](/cells/ru/java/data-validation/).
- [Время находится в определенном диапазоне](/cells/ru/java/data-validation/).
- [Текст находится в пределах заданной длины символа](/cells/ru/java/data-validation/).
### **Проверка данных с помощью Microsoft Excel**
Чтобы создать проверки с помощью Microsoft Excel:

1. На листе выберите ячейки, к которым вы хотите применить проверку.
1. От**Данные**меню, выберите**Проверка**.
 Отображается диалоговое окно проверки.
1. Нажмите на**Настройки**вкладку и введите настройки, как показано ниже.

   **Настройки проверки данных** 

![дело:изображение_альтернативный_текст](data-validation_1.png)
### **Проверка данных с Aspose.Cells**
Проверка данных — мощная функция для проверки информации, введенной в рабочие листы. Благодаря проверке данных разработчики могут предоставить пользователям список вариантов, ограничить ввод данных определенным типом или размером и т. д.
 В Aspose.Cells каждый[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)класс имеет[Валидации](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)объект, который представляет собой набор[Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)объекты. Чтобы настроить проверку, установите некоторые[Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)свойства класса:

- [Тип](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): представляет тип проверки, который может быть указан с использованием одного из предопределенных значений в[Тип Валидации](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)перечисление.
- [Оператор](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): представляет оператор, который будет использоваться при проверке, который можно указать, используя одно из предопределенных значений в[Тип оператора](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)перечисление.
- [Формула 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): представляет значение или выражение, связанное с первой частью проверки данных.
- [Формула2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): представляет значение или выражение, связанное со второй частью проверки данных.

Когда[Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)свойства объекта настроены, разработчики могут использовать[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)структура для хранения информации о диапазоне ячеек, который будет проверяться с помощью созданной проверки.
#### **Типы проверки данных**
Проверка данных позволяет встраивать бизнес-правила в каждую ячейку, чтобы неправильные записи приводили к сообщениям об ошибках. Бизнес-правила — это политики и процедуры, которые регулируют работу бизнеса. Aspose.Cells поддерживает все важные типы проверки данных.

[Тип Валидации](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)перечисление имеет следующие члены:

|**Имя участника**|**Описание**|
|:- |:- |
|[ЛЮБОЕ_ЗНАЧЕНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Обозначает значение любого типа.|
|[ЦЕЛОЕ ЧИСЛО](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Обозначает тип проверки для целых чисел.|
|[ДЕСЯТИЧНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Обозначает тип проверки для десятичных чисел.|
|[СПИСОК](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Обозначает тип проверки для раскрывающегося списка.|
|[ДАТИРОВАТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Обозначает тип проверки для дат.|
|[ВРЕМЯ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Обозначает тип проверки для времени.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Обозначает тип проверки длины текста.|
|[ОБЫЧАЙ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Обозначает настраиваемый тип проверки.|
#### **Пример программирования: проверка данных целого числа**
При этом типе проверки пользователи могут вводить в проверенные ячейки только целые числа из указанного диапазона. В приведенных ниже примерах кода показано, как реализовать[ЦЕЛОЕ ЧИСЛО](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)тип проверки. В примере создается та же проверка данных с использованием Aspose.Cells, которую мы создали с помощью Microsoft Excel выше.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Пример программирования: проверка десятичных данных**
При этом типе проверки пользователь может вводить десятичные числа в проверенные ячейки. В этом примере пользователь может вводить только десятичные значения, а область проверки — A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Пример программирования: проверка данных списка**
Этот тип проверки позволяет пользователю вводить значения из раскрывающегося списка. Он предоставляет список: ряд строк, содержащих данные. Пользователи могут выбирать значения только из списка. Областью проверки является диапазон ячеек A1:A5 на первом листе.

Здесь важно, чтобы вы установили[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) собственность на**истинный**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Пример программирования: проверка данных даты**
При этом типе проверки пользователи вводят значения дат в указанном диапазоне или соответствующие определенным критериям в проверенные ячейки. В этом примере пользователю разрешено вводить даты с 1970 по 1999 год. Здесь областью проверки является ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Примеры программирования: проверка данных времени**
При этом типе проверки пользователи могут вводить время в пределах указанного диапазона или в соответствии с некоторыми критериями в проверенные ячейки. В примере пользователю разрешено вводить время с 09:00 до 11:30. Здесь областью проверки является ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Примеры программирования: проверка данных о длине текста**
При этом типе проверки пользователи могут вводить текстовые значения заданной длины в проверенные ячейки. В примере пользователю разрешено вводить строковые значения, содержащие не более 5 символов. Область проверки — ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Правила проверки данных**
Когда реализованы проверки данных, проверку можно проверить, назначив разные значения в ячейках.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) можно использовать для получения результата проверки. В следующем примере эта функция демонстрируется с разными значениями. Образец файла можно загрузить по следующей ссылке для тестирования:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Проверьте, является ли проверка в ячейке раскрывающимся списком**
 Как мы видели, существует множество типов проверок, которые можно реализовать в ячейке. Если вы хотите проверить, является ли проверка раскрывающимся списком или нет,[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) свойство можно использовать для проверки этого. Следующий пример кода демонстрирует использование этого свойства. Образец файла для тестирования можно скачать по следующей ссылке:

[SampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Добавить CellArea к существующей проверке**
Могут быть случаи, когда вы можете захотеть добавить[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)к существующим[Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Когда вы добавляете[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)с использованием[Validation.AddArea(CellAreacellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells проверяет все существующие области, чтобы убедиться, что новая область уже существует. Если файл имеет большое количество проверок, это снижает производительность. Чтобы преодолеть это, API предоставляет[Validation.AddAreaCellArea (cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) метод.*проверитьПерекресток*Параметр указывает, следует ли проверять пересечение данной области с существующими областями проверки. Установка его на**ЛОЖЬ**отключит проверку других областей.*checkEdge*Параметр указывает, следует ли проверять обрабатываемые области. Если новая область становится верхней левой областью, внутренние настройки перестраиваются. Если вы уверены, что новая область не является верхней левой областью, вы можете установить этот параметр как**ЛОЖЬ**.

Следующий фрагмент кода демонстрирует использование[Validation.AddAreaCellArea (cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) метод добавления нового[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)к существующим[Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Исходный и выходной файлы Excel прилагаются для ознакомления.

[Исходный файл](PivotTableHideAndSortSample.xlsx)

[Выходной файл](ValidationsSample_out.xlsx)


## **Предварительные темы**
- [Получить проверку Cell в файлах ODS](/cells/ru/java/get-cell-validation-in-ods-files/)
- [Применить проверку к номеру Cell](/cells/ru/java/get-validation-applied-on-a-cell/)
- [Убедитесь, что значение Cell удовлетворяет правилам проверки данных.](/cells/ru/java/verify-that-cell-value-satisfies-data-validation-rules/)

---
title: Валидация данных
type: docs
weight: 70
url: /ru/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel предоставляет некоторые хорошие функции для автоматической фильтрации или валидации данных листа.

[Валидация данных](/cells/ru/java/data-validation/) – это возможность установить правила ввода данных на листе. Например, используйте валидацию, чтобы гарантировать, что столбец с меткой DATE содержит только даты, или что другой столбец содержит только числа. Вы можете даже убедиться, что столбец с меткой DATE содержит только даты в определенном диапазоне. С помощью валидации данных вы можете контролировать, что вводится в ячейки на листе. Aspose.Cells полностью поддерживает функции валидации данных и автофильтрации Microsoft Excel. В этой статье объясняется, как использовать функции в Microsoft Excel и как их программир...</cel...

{{% /alert %}} 
## **Типы проверки данных и выполнение**
Microsoft Excel поддерживает ряд различных типов проверки данных. Каждый тип используется для контроля типа данных, вводимого в ячейку или диапазон ячеек. Ниже приведены фрагменты кода, иллюстрирующие проверку, что:

- [Числа являются целыми](/cells/ru/java/data-validation/), то есть они не имеют десятичной части.
- [Десятичные числа соответствуют правильной структуре](/cells/ru/java/data-validation/). В приведенном примере кода определено, что диапазон ячеек должен иметь два десятичных знака.
- [Значения ограничены списком значений](/cells/ru/java/data-validation/). Проверка списка определяет отдельный список значений, которые можно применить к ячейке или диапазону ячеек.
- [Даты находятся в определенном диапазоне](/cells/ru/java/data-validation/)
- [Время находится в определенном диапазоне](/cells/ru/java/data-validation/)
- [Текст находится в заданной длине символов](/cells/ru/java/data-validation/)
### **Проверка данных в Microsoft Excel**
Для создания проверок с помощью Microsoft Excel:

1. В листе выберите ячейки, к которым вы хотите применить проверку.
1. В меню **Данные** выберите **Проверка**.
   Отображается диалоговое окно проверки.
1. Нажмите вкладку **Настройка** и введите настройки, как показано ниже. 

   **Настройки проверки данных** 

![todo:image_alt_text](data-validation_1.png)
### **Проверка данных в Aspose.Cells**
Проверка данных - мощная функция для проверки введенной информации в таблицы. С помощью проверки данных разработчики могут предоставлять пользователям список выбора, ограничивать ввод данных определенного типа или размера и т. д.
В Aspose.Cells каждый [класс Лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) имеет объект [Проверки](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations), который представляет собой коллекцию объектов [Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Чтобы настроить проверку, установите некоторые свойства класса [Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation):

- [Тип](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): представляет тип проверки, который может быть указан с использованием одного из предопределенных значений в перечислении [ТипПроверки](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType).
- [Оператор](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): представляет оператор, который будет использоваться при проверке, который может быть указан с использованием одного из предопределенных значений в перечислении [ТипОператора](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType).
- [Формула1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): представляет значение или выражение, связанное с первой частью проверки данных.
- [Формула2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): представляет значение или выражение, связанное со второй частью проверки данных.

Когда свойства объекта [Проверка](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) настроены, разработчики могут использовать структуру [ДиапазонЯчеек](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) для хранения информации о диапазоне ячеек, которые будут проверяться с использованием созданной проверки.
#### **Типы проверки данных**
Проверка данных позволяет встраивать в каждую ячейку деловые правила, чтобы неправильные записи приводили к сообщениям об ошибках. Деловые правила - это политики и процедуры, которые регулируют деятельность компании. Aspose.Cells поддерживает все важные типы проверки данных.

Перечисление [ТипПроверки](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) имеет следующие элементы:

|**Название элемента**|**Описание**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY-VALUE)|Обозначает значение любого типа.|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER)|Обозначает тип проверки целых чисел.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Обозначение типа проверки для десятичных чисел.|
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Обозначение типа проверки для выпадающего списка.|
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Обозначение типа проверки для дат.|
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Обозначение типа проверки для времени.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT-LENGTH)|Обозначает тип проверки длины текста.|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Обозначение типа проверки.|
#### **Пример программирования: Проверка данных целого числа**
С этим типом проверки пользователи могут вводить только целые числа в определенном диапазоне в проверяемые ячейки. Следующие примеры показывают, как реализовать тип проверки [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER). В примере создается такая же проверка данных с помощью Aspose.Cells, как и в Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Пример программирования: Проверка данных десятичного числа**
С этим типом проверки пользователь может вводить десятичные числа в проверяемые ячейки. В примере пользователю запрещается вводить только десятичные значения, и область проверки – A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Пример программирования: Проверка данных из списка**
Этот тип проверки позволяет пользователю вводить значения из выпадающего списка. Предоставляется список: серия строк, содержащих данные. Пользователи могут выбирать значения только из списка. Область проверки – это диапазон ячеек A1:A5 на первом листе.

Здесь важно установить свойство  [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) в **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Пример программирования: Проверка данных даты**
С этим типом проверки пользователи вводят значения дат в указанном диапазоне или отвечающие определенным критериям в проверяемые ячейки. В примере пользователь ограничен вводом дат с 1970 по 1999 год. Здесь область проверки – ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Пример программирования: Проверка данных времени**
С этим типом проверки пользователи могут вводить время в указанном диапазоне, или соответствующее некоторым критериям, в проверяемые ячейки. В примере пользователь ограничен вводом времени с 09:00 по 11:30 утра. Здесь область проверки – ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Пример программирования: Проверка данных длины текста**
С помощью этого типа проверки пользователи могут вводить текстовые значения заданной длины в проверяемые ячейки. В примере пользователь ограничен вводом строковых значений не более 5 символов. Область проверки - это ячейка B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Правила проверки данных**
Когда реализуются проверки данных, то проверка может быть выполнена путем назначения различных значений в ячейки. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) можно использовать для получения результата проверки. Следующий пример демонстрирует эту функцию с разными значениями. Файл для тестирования можно скачать по следующей ссылке:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Проверьте, является ли проверка в ячейке выпадающим списком**
Как мы видели, существует множество типов проверок, которые могут быть реализованы внутри ячейки. Если вы хотите проверить, является ли проверка выпадающим списком или нет, можно использовать свойство [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown), чтобы проверить это. В следующем примере демонстрируется использование этого свойства. Образец файла для тестирования можно загрузить по следующей ссылке:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Добавить CellArea к существующей Validation**
Могут быть случаи, когда вы захотите добавить [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) к существующей [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). При добавлении [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) через [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-), Aspose.Cells проверяет все существующие области, чтобы убедиться, что новая область уже не существует. Если в файле много проверок, это сказывается на производительности. Чтобы решить проблему, API предоставляет метод [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-). Параметр *checkIntersection* указывает, следует ли проверять пересечение заданной области с существующими областями проверки. Установка его в **false** отключает проверку других областей. Параметр *checkEdge* указывает, следует ли проверять применяемые области. Если новая область соответствует верхнему левому углу, внутренние настройки пересобираются. Если вы уверены, что новая область не является верхним левым углом, этот параметр можно установить в **false**.

Следующий пример демонстрирует использование метода [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-) для добавления новой [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) в существующую [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Исходный и выходной файлы Excel прикреплены для справки.

[Исходный файл](PivotTableHideAndSortSample.xlsx)

[Выходной файл](ValidationsSample_out.xlsx)


## **Продвинутые темы**
- [Получить проверку ячейки в файлах ODS](/cells/ru/java/get-cell-validation-in-ods-files/)
- [Получить примененную проверку данных к ячейке](/cells/ru/java/get-validation-applied-on-a-cell/)
- [Проверьте, что значение ячейки удовлетворяет правилам проверки данных](/cells/ru/java/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="java" >}}

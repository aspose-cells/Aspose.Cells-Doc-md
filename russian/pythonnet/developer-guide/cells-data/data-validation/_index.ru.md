---
title: Валидация данных
type: docs
weight: 90
url: /ru/python-net/data-validation/
description: Узнайте, как добавить проверку данных с помощью Aspose.Cells для Python via .NET API.
keywords: Python Excel библиотека, Добавление проверки данных в Python, Получение значения проверки данных в Python, Добавление проверки на целые числа в Python, Добавление проверки на список данных в Python, Добавление проверки на дату в Python, Добавление проверки на время в Python, Добавление проверки на длину текста в Python, Добавление ячейки в существующую проверку данных в Python, Проверка, если проверка в ячейке выпадающий список, Добавить пользовательскую проверку  
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет некоторые хорошие функции автофильтрации или проверки данных на листе таблицы. Aspose.Cells для Python via .NET полностью поддерживает проверку данных и функции автофильтрации Microsoft Excel. В этой статье объясняется, как использовать эти функции в Microsoft Excel и как написать код для их использования с помощью Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Типы проверки данных и выполнение**

Проверка данных - это возможность устанавливать правила, касающиеся ввода данных на листе таблицы. Например, использовать проверку для обеспечения того, что столбец с подписью DATE содержит только даты, или что другой столбец содержит только числа. Вы даже можете обеспечить, что столбец с подписью DATE содержит только даты в определенном диапазоне. С помощью проверки данных вы можете контролировать то, что вводится в ячейки на листе таблицы.

Microsoft Excel поддерживает ряд различных типов проверки данных. Каждый тип используется для контроля типа данных, вводимого в ячейку или диапазон ячеек. Ниже приведены фрагменты кода, иллюстрирующие проверку, что:

- Числа являются целыми, то есть у них нет десятичной части.
- Десятичные числа соответствуют правильной структуре. Приведенный пример кода определяет, что диапазон ячеек должен иметь два десятичных знака.
- Значения ограничены списком значений. Проверка списка определяет отдельный список значений, которые можно применить к ячейке или диапазону ячеек.
- Даты находятся в определенном диапазоне.
- Время находится в определенном диапазоне.
- Текст имеет определенную длину.

### **Проверка данных в Microsoft Excel**

Для создания проверок с помощью Microsoft Excel:

1. В листе выберите ячейки, к которым вы хотите применить проверку.
1. Из меню **Данные** выберите **Проверку**. Диалоговое окно проверки будет отображено.
1. Нажмите вкладку **Настройки** и введите настройки.

### **Проверка данных с использованием библиотеки Aspose.Cells для Python Excel**

Проверка данных - мощная функция для проверки введенной информации в таблицы. С помощью проверки данных разработчики могут предоставлять пользователям список выбора, ограничивать ввод данных определенного типа или размера и т. д.
В Aspose.Cells для Python via .NET, у каждого объекта [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) есть свойство [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/), которое представляет собой коллекцию объектов [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation). Чтобы настроить проверку, задайте некоторые свойства класса [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) следующим образом:

- type – представляет тип проверки, который можно указать, используя одно из предопределенных значений в перечислении [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype).
- Оператор – представляет оператор, который следует использовать в проверке, который можно указать, используя одно из предопределенных значений в перечислении [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype).
- formula1 – представляет значение или выражение, связанное с первой частью проверки данных.
- formula2 – представляет значение или выражение, связанное со второй частью проверки данных.

Когда свойства объекта [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) были настроены, разработчики могут использовать структуру [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), чтобы хранить информацию о диапазоне ячеек, который будет проверен с использованием созданной проверки.

#### **Типы проверки данных**

Перечисление [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) имеет следующие члены:

|**Название элемента**|**Описание**|
| :- | :- |
|ANY_VALUE|Обозначает значение любого типа.|
|WHOLE_NUMBER|Обозначает тип проверки для целых чисел.|
|DECIMAL|Обозначает тип проверки для десятичных чисел.|
|LIST|Обозначает тип проверки для выпадающего списка.|
|DATE|Обозначает тип проверки для дат.|
|TIME|Обозначает тип проверки для времени.|
|TEXT_LENGTH|Обозначает тип проверки для длины текста.|
|ПОЛЬЗОВАТЕЛЬСКИЙ|Обозначает тип пользовательской проверки.|

##### **Проверка данных на целые числа**

С этим типом проверки пользователи могут вводить только целые числа в указанном диапазоне в проверяемые ячейки. Приведены примеры кода, показывающие, как реализовать тип проверки на целые числа. В примере создается такая же проверка данных, используя Aspose.Cells для Python via .NET, которую мы создали с помощью Microsoft Excel выше.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **Проверка данных на список**

Этот тип проверки позволяет пользователю вводить значения из выпадающего списка. Он предоставляет список: серию строк, содержащих данные. В примере во втором рабочем листе добавляется список источников. Пользователи могут выбирать значения только из списка. Область проверки - это диапазон ячеек A1:A5 на первом рабочем листе.

Здесь важно установить свойство [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) на **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **Проверка данных на дату**

С этим типом проверки пользователи вводят значения дат в указанном диапазоне или отвечающие определенным критериям в проверяемые ячейки. В примере пользователь ограничен вводом дат с 1970 по 1999 год. Здесь область проверки – ячейка B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **Проверка данных на время**

С этим типом проверки пользователи могут вводить время в указанном диапазоне, или соответствующее некоторым критериям, в проверяемые ячейки. В примере пользователь ограничен вводом времени с 09:00 по 11:30 утра. Здесь область проверки – ячейка B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **Проверка данных на длину текста**

С помощью этого типа проверки пользователи могут вводить текстовые значения заданной длины в проверяемые ячейки. В примере пользователь ограничен вводом строковых значений не более 5 символов. Область проверки - это ячейка B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **Правила проверки данных**

При реализации проверки данных можно проверить проверку, присвоив разные значения в ячейки. [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) можно использовать для получения результатов проверки. В следующем примере демонстрируется это функция с разными значениями. Образец файла можно загрузить по следующей ссылке для тестирования:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **Проверить, если проверка в ячейке выпадающая**

Как мы видели, существует множество типов проверок, которые могут быть реализованы в ячейке. Если вы хотите проверить, является ли проверка выпадающей или нет, свойство [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) можно использовать для этого теста. В следующем примере кода демонстрируется использование этого свойства. Образец файла для тестирования можно загрузить по следующей ссылке:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **Добавить CellArea к существующей Validation**

Может возникнуть случаи, когда вы хотите добавить [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) к существующему [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation). Когда вы добавляете [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) при помощи [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea), Aspose.Cells проверяет все существующие области, чтобы увидеть, существует ли новая область уже. Если в файле большое количество проверок, это замедляет работу. Для преодоления этого API предоставляет метод [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool). Параметр *checkIntersection* указывает, следует ли проверять пересечение данной области с существующими областями проверок. Установка его в **false** отключит проверку других областей. Параметр *checkEdge* указывает, следует ли проверять примененные области. Если новая область становится верхним левым углом, внутренние настройки перестраиваются. Если вы уверены, что новая область не является верхним левым углом, вы можете установить этот параметр в **false**.

Следующий фрагмент кода демонстрирует использование метода [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) для добавления нового [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) к существующему [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

Исходный и выходной файлы Excel прикреплены для справки.

[Исходный файл](96928093.xlsx)

[Выходной файл](96928220.xlsx)


## **Продвинутые темы**
- [Получить проверку ячейки в файлах ODS](/cells/ru/python-net/get-cell-validation-in-ods-files/)
- [Получить примененную проверку данных к ячейке](/cells/ru/python-net/get-validation-applied-on-a-cell/)
- [Проверьте, что значение ячейки удовлетворяет правилам проверки данных](/cells/ru/python-net/verify-that-cell-value-satisfies-data-validation-rules/)

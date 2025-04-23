---
title: Валидация данных с помощью C++
linktitle: Валидация данных
type: docs
weight: 90
url: /ru/cpp/data-validation/
description: Узнайте, как добавлять проверку данных через API Aspose.Cells for C++.
keywords: Добавить проверку данных, получить значение проверки, добавить проверку на целое число, добавить список, добавить дату, добавить время, добавить длину текста, добавить CellArea в существующую проверку, проверить, является ли проверка выпадающим списком, добавить пользовательскую проверку  
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет хорошие функции для автоматической фильтрации или проверки данных на листе. Aspose.Cells полностью поддерживает функции проверки данных и автоматической фильтрации Microsoft Excel. В этой статье объясняется, как использовать эти функции в Microsoft Excel и как программировать их с помощью Aspose.Cells.

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

### **Проверка данных в Aspose.Cells**

Проверка данных - мощная функция для проверки введенной информации в таблицы. С помощью проверки данных разработчики могут предоставлять пользователям список выбора, ограничивать ввод данных определенного типа или размера и т. д.
В Aspose.Cells для каждого [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класса есть свойство [**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/), которое представляет коллекцию объектов [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/). Чтобы настроить валидацию, установите некоторые из свойств класса [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) как показано ниже:

- Тип – представляет тип валидации, который может быть указан, используя одно из предопределенных значений в перечислении [**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/).
- Оператор – представляет оператор, который следует использовать в проверке, который можно указать, используя одно из предопределенных значений в перечислении [**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/).
- Формула1 – представляет значение или выражение, связанное с первой частью валидации данных.
- Формула2 – представляет значение или выражение, связанное со второй частью валидации данных.

Когда свойства объекта [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) были настроены, разработчики могут использовать структуру [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), чтобы хранить информацию о диапазоне ячеек, который будет проверен с использованием созданной проверки.

#### **Типы проверки данных**

Перечисление [**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) имеет следующие члены:

|**Название элемента**|**Описание**|
| :- | :- |
|AnyValue|Обозначает значение любого типа.|
|WholeNumber|Обозначает тип проверки для целых чисел.|
|Decimal|Обозначает тип проверки для десятичных чисел.|
|List|Обозначает тип проверки для выпадающего списка.|
|Date|Обозначает тип проверки для дат.|
|Time|Обозначает тип проверки для времени.|
|TextLength|Обозначает тип проверки для длины текста.|
|Custom|Обозначает настраиваемый тип проверки.|

##### **Проверка данных на целые числа**

С этим типом проверки пользователи могут вводить только целые числа в указанном диапазоне в проверяемые ячейки. Приведены примеры кода, показывающие, как реализовать тип проверки на целое число. Пример создает одинаковую проверку данных, используя Aspose.Cells, как мы создали, используя Microsoft Excel выше.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Create a worksheet and get the first worksheet
    Worksheet ExcelWorkSheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Creating a Validation object
    Validation validation = validations.Get(validations.Add(ca));

    // Setting the validation type to whole number
    validation.SetType(ValidationType::WholeNumber);

    // Setting the operator for validation to Between
    validation.SetOperator(OperatorType::Between);

    // Setting the minimum value for the validation
    validation.SetFormula1(u"10");

    // Setting the maximum value for the validation
    validation.SetFormula2(u"1000");

    // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 1;
    area.StartColumn = 0;
    area.EndColumn = 1;

    // Adding the cell area to Validation
    validation.AddArea(area);

    // Save the workbook
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Validation applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Проверка данных на список**

Этот тип проверки позволяет пользователю вводить значения из выпадающего списка. Он предоставляет список: серию строк, содержащих данные. В примере во втором рабочем листе добавляется список источников. Пользователи могут выбирать значения только из списка. Область проверки - это диапазон ячеек A1:A5 на первом рабочем листе.

Здесь важно установить свойство [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) на **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Add a new worksheet and access it
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet2 = workbook.GetWorksheets().Get(i);

    // Create a range in the second worksheet
    Range range = worksheet2.GetCells().CreateRange(u"E1", u"E4");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"Blue");
    range.Get(1, 0).PutValue(u"Red");
    range.Get(2, 0).PutValue(u"Green");
    range.Get(3, 0).PutValue(u"Yellow");

    // Get the validations collection
    ValidationCollection validations = worksheet1.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Create a new validation to the validations list
    Validation validation = validations.Get(validations.Add(ca));

    // Set the validation type
    validation.SetType(ValidationType::List);

    // Set the operator
    validation.SetOperator(OperatorType::None);

    // Set the in cell drop down
    validation.SetInCellDropDown(true);

    // Set the formula1
    validation.SetFormula1(u"=MyRange");

    // Enable it to show error
    validation.SetShowError(true);

    // Set the alert type severity level
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the error title
    validation.SetErrorTitle(u"Error");

    // Set the error message
    validation.SetErrorMessage(u"Please select a color from the list");

    // Specify the validation area
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 4;
    area.StartColumn = 0;
    area.EndColumn = 0;

    // Add the validation area
    validation.AddArea(area);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Проверка данных на дату**

С этим типом проверки пользователи вводят значения дат в указанном диапазоне или отвечающие определенным критериям в проверяемые ячейки. В примере пользователь ограничен вводом дат с 1970 по 1999 год. Здесь область проверки – ячейка B1.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into the A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Date b/w 1/1/1970 and 12/31/1999");

    // Set row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::Date);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"1/1/1970");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"12/31/1999");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Date Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Date");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Date Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Проверка данных на время**

С этим типом проверки пользователи могут вводить время в указанном диапазоне, или соответствующее некоторым критериям, в проверяемые ячейки. В примере пользователь ограничен вводом времени с 09:00 по 11:30 утра. Здесь область проверки – ячейка B1.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Time b/w 09:00 and 11:30 'o Clock");

    // Set the row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    Validation validation = validations.Get(validations.Add(ca));

    // Set the data validation type
    validation.SetType(ValidationType::Time);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"09:00");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"11:30");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Information);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Time Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Time");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Time Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Проверка данных на длину текста**

С помощью этого типа проверки пользователи могут вводить текстовые значения заданной длины в проверяемые ячейки. В примере пользователь ограничен вводом строковых значений не более 5 символов. Область проверки - это ячейка B1.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter a string not more than 5 chars");

    // Set row height and column width for the cell
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::TextLength);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::LessOrEqual);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"5");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Warning);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Text Length Error");

    // Set the data validation error message
    validation.SetErrorMessage(u" Enter a Valid String");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"TextLength Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Правила проверки данных**

Когда проверки данных реализованы, то проверку можно проверить, присваивая различные значения в ячейках. Для извлечения результата проверки можно использовать [**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). Следующий пример демонстрирует это функциональность с различными значениями. Примерный файл можно скачать по следующей ссылке для тестирования:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Проверить, если проверка в ячейке выпадающая**

Как мы видели, существует множество типов проверок, которые могут быть реализованы в ячейке. Если вы хотите проверить, является ли проверка выпадающей или нет, свойство [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) можно использовать для этого теста. В следующем примере кода демонстрируется использование этого свойства. Образец файла для тестирования можно загрузить по следующей ссылке:

[sampleValidation.xlsx](79527947.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleValidation.xlsx";

    // Create workbook
    Workbook book(inputFilePath);

    // Get worksheet
    Worksheet sheet = book.GetWorksheets().Get(u"Sheet1");

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Check validation for cell A2
    Cell a2 = cells.Get(u"A2");
    Validation va2 = a2.GetValidation();
    if (va2.GetInCellDropDown())
    {
        std::cout << "A2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "A2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell B2
    Cell b2 = cells.Get(u"B2");
    Validation vb2 = b2.GetValidation();
    if (vb2.GetInCellDropDown())
    {
        std::cout << "B2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "B2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell C2
    Cell c2 = cells.Get(u"C2");
    Validation vc2 = c2.GetValidation();
    if (vc2.GetInCellDropDown())
    {
        std::cout << "C2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "C2 is NOT a dropdown" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Добавить CellArea к существующей Validation**

Может возникнуть случаи, когда вы хотите добавить [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) к существующему [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/). Когда вы добавляете [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) при помощи [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/), Aspose.Cells проверяет все существующие области, чтобы увидеть, существует ли новая область уже. Если в файле большое количество проверок, это замедляет работу. Для преодоления этого API предоставляет метод [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/). Параметр *checkIntersection* указывает, следует ли проверять пересечение данной области с существующими областями проверок. Установка его в **false** отключит проверку других областей. Параметр *checkEdge* указывает, следует ли проверять примененные области. Если новая область становится верхним левым углом, внутренние настройки перестраиваются. Если вы уверены, что новая область не является верхним левым углом, вы можете установить этот параметр в **false**.

Следующий фрагмент кода демонстрирует использование метода [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) для добавления нового [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) к существующему [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ValidationsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    Validation validation = worksheet.GetValidations().Get(0);

    // Create cell area
    CellArea cellArea = CellArea::CreateCellArea(u"D5", u"E7");

    // Adding the cell area to Validation
    validation.AddArea(cellArea, false, false);

    // Save the output workbook
    workbook.Save(outDir + u"ValidationsSample_out.xlsx");

    std::cout << "Validation added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Исходный и выходной файлы Excel прикреплены для справки.

[Исходный файл](96928093.xlsx)

[Выходной файл](96928220.xlsx)

## **Продвинутые темы**
- [Получить проверку ячейки в файлах ODS](/cells/ru/cpp/get-cell-validation-in-ods-files/)
- [Получить примененную проверку данных к ячейке](/cells/ru/cpp/get-validation-applied-on-a-cell/)
- [Проверьте, что значение ячейки удовлетворяет правилам проверки данных](/cells/ru/cpp/verify-that-cell-value-satisfies-data-validation-rules/)

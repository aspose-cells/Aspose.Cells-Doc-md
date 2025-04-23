---
title: Управление рабочей книгой с помощью C++
linktitle: Книга
type: docs
weight: 60
url: /ru/cpp/managing-workbooks-and-worksheets/
description: Узнайте, как управлять рабочей книгой через API Aspose.Cells for C++.
keywords: Как управлять рабочей книгой в C++, управлять рабочими листами через C++, работать с рабочими книгами и листами в C++.
---

{{% alert color="primary" %}}

API Aspose.Cells for C++ предоставляет мощный и гибкий интерфейс для управления рабочими книгами и листами. В этом разделе объясняется, как создавать, открывать и манипулировать рабочими книгами и листами программно.

{{% /alert %}}

## **Создание новой книги**
Чтобы создать новую рабочую книгу:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
2. Добавьте листы в рабочую книгу с помощью класса [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Сохраните рабочую книгу с помощью метода [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Открытие существующей рабочей книги**
Чтобы открыть существующую рабочую книгу:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) и передайте путь к файлу в конструктор.
2. Получите доступ к листам с помощью класса [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Модифицируйте рабочую книгу по необходимости.
4. Сохраните рабочую книгу с помощью метода [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Управление листами**
API Aspose.Cells for C++ предоставляет широкий набор методов для управления листами, включая добавление, удаление и переименование листов.

### **Добавление рабочего листа**
Чтобы добавить новый рабочий лист:

1. Получите доступ к классу [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) из книги.
2. Используйте метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/), чтобы добавить новый рабочий лист.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Удаление листа**
Для удаления рабочего листа:

1. Получите доступ к классу [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) из книги.
2. Используйте метод [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/), чтобы удалить рабочий лист по индексу.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Переименование листа**
Для переименования рабочего листа:

1. Получите доступ к классу [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) из книги.
2. Используйте метод [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/), чтобы переименовать рабочий лист.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Заключение**
Aspose.Cells for C++ содержит комплексный набор инструментов для управления рабочими книгами и листами. Независимо от того, нужно ли создать новую книгу, открыть существующую или манипулировать листами — Aspose.Cells облегчает работу с файлами Excel программным способом.

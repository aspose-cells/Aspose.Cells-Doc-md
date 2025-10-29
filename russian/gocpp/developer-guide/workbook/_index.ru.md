---
title: Управление рабочей книгой с помощью Golang через C++
linktitle: Книга
type: docs
weight: 60
url: /ru/go-cpp/managing-workbooks-and-worksheets/
description: Узнайте, как управлять рабочей книгой через API Aspose.Cells for C++.
keywords: Как управлять рабочей книгой в C++, управлять рабочими листами через C++, работать с рабочими книгами и листами в C++.
---

{{% alert color="primary" %}}

API Aspose.Cells for C++ предоставляет мощный и гибкий интерфейс для управления рабочими книгами и листами. В этом разделе объясняется, как создавать, открывать и манипулировать рабочими книгами и листами программно.

{{% /alert %}}

## **Создание новой книги**
Чтобы создать новую рабочую книгу:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).
2. Добавьте листы в рабочую книгу, используя класс [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Сохраните рабочую книгу с помощью метода [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Открытие существующей рабочей книги**
Чтобы открыть существующую рабочую книгу:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) и передайте путь к файлу в конструктор.
2. Получите доступ к листам через класс [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Модифицируйте рабочую книгу по необходимости.
4. Сохраните рабочую книгу с помощью метода [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Управление листами**
API Aspose.Cells for C++ предоставляет широкий набор методов для управления листами, включая добавление, удаление и переименование листов.

### **Добавление рабочего листа**
Чтобы добавить новый рабочий лист:

1. Получите доступ к классу [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) из рабочей книги.
2. Используйте метод [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) для добавления нового листа.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Удаление листа**
Для удаления рабочего листа:

1. Получите доступ к классу [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) из рабочей книги.
2. Используйте метод [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) для удаления листа по индексу.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Переименование листа**
Для переименования рабочего листа:

1. Получите доступ к классу [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) из рабочей книги.
2. Используйте метод [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) для переименования листа.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Заключение**
Aspose.Cells for C++ содержит комплексный набор инструментов для управления рабочими книгами и листами. Независимо от того, нужно ли создать новую книгу, открыть существующую или манипулировать листами — Aspose.Cells облегчает работу с файлами Excel программным способом.

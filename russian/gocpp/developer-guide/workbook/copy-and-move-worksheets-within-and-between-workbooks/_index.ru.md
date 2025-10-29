---
title: Копирование и перемещение листов внутри и между рабочими книгами с помощью Golang через C++
linktitle: Копирование и перемещение листов
type: docs
weight: 80
url: /ru/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Узнайте, как копировать и перемещать листы внутри и между рабочими книгами Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам нужны несколько листов с одинаковым форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вы можете создать рабочую книгу с листами, содержащими одинаковые заголовки столбцов, строк и формулы. Есть способ сделать это: создав один лист и затем копируя его несколько раз.

Aspose.Cells поддерживает копирование или перемещение листов внутри или между книгами. Листы включают данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты с наивысшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров:

1. Создайте две рабочие книги с некоторыми данными в Microsoft Excel. Для этого примера мы создали две новые рабочие книги в Excel и ввели некоторые данные в листы:
   - FirstWorkbook.xlsx (3 листа)
   - SecondWorkbook.xlsx (1 лист)

1. Скачайте и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Установите его на ваш компьютер для разработки

1. Создайте проект:
   1. Создайте новый проект C++ в выбранной IDE

1. Добавьте ссылки:
   1. Добавьте библиотеку Aspose.Cells for C++ в проект

1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Копирование листа между книгами Excel**

Выполнение кода копирует лист с именем Copy в SecondWorkbook.xlsx с именем листа Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}

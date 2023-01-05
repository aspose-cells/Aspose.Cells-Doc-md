---
title: Копировать и перемещать рабочие листы внутри и между рабочими книгами
type: docs
weight: 80
url: /ru/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Иногда вам нужно несколько рабочих листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вы можете создать рабочую книгу с листами, содержащими одинаковые заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создать один лист, а затем скопировать его три раза.

Aspose.Cells поддерживает копирование или перемещение рабочих листов внутри или между книгами. Рабочие листы, включая данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты, копируются с высочайшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение рабочих листов**

### **Копирование рабочего листа в рабочую книгу**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые рабочие книги в Microsoft Excel и ввели некоторые данные в рабочие листы.

- FirstWorkbook.xlsx (3 рабочих листа).
- SecondWorkbook.xlsx (1 рабочий лист).

1. Загрузите и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Установите его на свой компьютер для разработки.
 Все[Aspose](http://www.aspose.com/) компоненты при установке работают в ознакомительном режиме. Режим оценки не имеет ограничения по времени и только вставляет водяные знаки в создаваемые документы.
1. Создайте проект:
 1. Запустите Visual Studio.Net.
 1. Создайте новое консольное приложение.
1. Добавьте ссылки:
 1. Добавьте в проект ссылку на Aspose.Cells.
 Например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.
1. Скопируйте рабочий лист в рабочей книге
 В первом примере копируется первый рабочий лист (копия) в файле FirstWorkbook.xlsx.

При выполнении кода рабочий лист с именем Copy копируется в FirstWorkbook.xlsx с именем Last Sheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Перемещение рабочего листа в рабочей книге**

В приведенном ниже коде показано, как переместить лист из одной позиции в книге в другую. Выполнение кода перемещает рабочий лист с именем Move из индекса 1 в индекс 2 в FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Копирование рабочего листа между рабочими книгами**

При выполнении кода рабочий лист с именем Copy is копируется в SecondWorkbook.xlsx с именем Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Перемещение рабочего листа между рабочими книгами**

Выполнение кода перемещает рабочий лист с именем Move из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}

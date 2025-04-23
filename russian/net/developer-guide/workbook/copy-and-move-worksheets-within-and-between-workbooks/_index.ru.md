---
title: Копирование и перемещение листов внутри и между книгами
type: docs
weight: 80
url: /ru/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Иногда вам требуется несколько листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вам может понадобиться создать книгу с листами, содержащими одни и те же заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его три раза.

Aspose.Cells поддерживает копирование или перемещение листов внутри или между книгами. Листы включают данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты с наивысшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые книги в Microsoft Excel и ввели некоторые данные на листах.

- FirstWorkbook.xlsx (3 листа).
- SecondWorkbook.xlsx (1 лист).

1. Скачайте и установите Aspose.Cells:
   1. [Загрузить Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Установите его на вашем компьютере для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект:
   1. Запустите Visual Studio.Net.
   1. Создайте новое консольное приложение.
1. Добавьте ссылки:
   1. Добавьте ссылку на Aspose.Cells в проект.
      Например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Копирование листа между книгами Excel**

При выполнении кода лист с именем Copy копируется в SecondWorkbook.xlsx с именем Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}

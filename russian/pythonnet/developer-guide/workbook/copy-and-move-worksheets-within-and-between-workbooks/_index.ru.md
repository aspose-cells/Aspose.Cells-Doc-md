---
title: Копирование и перемещение листов внутри и между книгами
type: docs
weight: 80
url: /ru/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Иногда вам требуется несколько листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вам может понадобиться создать книгу с листами, содержащими одни и те же заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его три раза.

Aspose.Cells для Python via .NET поддерживает копирование или перемещение листов within или между рабочими книгами. Листы, включая данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты, копируются с максимальной точностью.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые книги в Microsoft Excel и ввели некоторые данные на листах.

- FirstWorkbook.xlsx (3 листа).
- SecondWorkbook.xlsx (1 лист).

1. Скачайте и установите Aspose.Cells для Python via .NET:
   1. [Скачать Aspose.Cells для Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Установите его на вашем компьютере для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект и добавьте ссылки:   
1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Копирование листа между книгами Excel**

При выполнении кода лист с именем Copy копируется в SecondWorkbook.xlsx с именем Sheet2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}

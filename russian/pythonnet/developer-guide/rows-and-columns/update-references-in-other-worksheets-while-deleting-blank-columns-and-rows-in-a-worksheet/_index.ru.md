---
title: Обновление ссылок в других листах при удалении пустых столбцов и строк на листе
type: docs
weight: 5000
url: /ru/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: В этой статье показано, как обновить ссылки в других рабочих листах при удалении пустых столбцов и строк в рабочем листе с помощью Aspose.Cells for Python via .NET API.
keywords: Библиотека Python Excel, Обновление ссылок в других рабочих листах при удалении пустых столбцов и строк в рабочем листе Python, Обновление ссылок при удалении пустых столбцов и строк в рабочем листе в Python.
---

{{% alert color="primary" %}}

Когда вы удаляете пустые столбцы и строки в листе, их ссылки в других листах становятся недействительными. Если вы хотите избежать этого поведения и хотите, чтобы эти ссылки текущего листа в других листах также обновлялись, то, пожалуйста, используйте свойство [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) и установите его в **true**.

{{% /alert %}}

## **Обновление ссылок в других листах при удалении пустых столбцов и строк на листе**

Пожалуйста, посмотрите следующий образец кода и его консольный вывод. Ячейка E3 второго листа имеет формулу =Sheet1!C3, которая ссылается на ячейку C3 первого листа. Если вы установите свойство [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) в **true**, эта формула будет обновлена и станет =Sheet1!A1 при удалении пустых столбцов и строк в первом листе. Однако, если вы установите свойство [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) в **false**, формула в ячейке E3 второго листа останется =Sheet1!C3 и станет недействительной.

### **Пример программирования**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **Вывод в консоль**

Это консольный вывод вышеуказанного образца кода, когда свойство [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) было установлено в **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Это консольный вывод вышеуказанного образца кода, когда свойство [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) было установлено в **false**. Как видите, формула в ячейке E3 второго листа не обновлена, и ее значение ячейки теперь 0 вместо 4, что является недействительным.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}

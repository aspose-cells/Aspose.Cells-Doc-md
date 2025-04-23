---
title: Обновление ссылок в других листах при удалении пустых столбцов и строк на листе
type: docs
weight: 5000
url: /ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Когда вы удаляете пустые столбцы и строки в листе, их ссылки в других листах становятся недействительными. Если вы хотите избежать этого поведения и хотите, чтобы эти ссылки текущего листа в других листах также обновлялись, то, пожалуйста, используйте свойство [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) и установите его в **true**.

{{% /alert %}}

## **Обновление ссылок в других листах при удалении пустых столбцов и строк на листе**

Пожалуйста, посмотрите следующий образец кода и его консольный вывод. Ячейка E3 второго листа имеет формулу =Sheet1!C3, которая ссылается на ячейку C3 первого листа. Если вы установите свойство [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) в **true**, эта формула будет обновлена и станет =Sheet1!A1 при удалении пустых столбцов и строк в первом листе. Однако, если вы установите свойство [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) в **false**, формула в ячейке E3 второго листа останется =Sheet1!C3 и станет недействительной.

### **Пример программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Вывод в консоль**

Это консольный вывод вышеуказанного образца кода, когда свойство [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) было установлено в **true**.

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

Это консольный вывод вышеуказанного образца кода, когда свойство [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) было установлено в **false**. Как видите, формула в ячейке E3 второго листа не обновлена, и ее значение ячейки теперь 0 вместо 4, что является недействительным.

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
{{< app/cells/assistant language="csharp" >}}

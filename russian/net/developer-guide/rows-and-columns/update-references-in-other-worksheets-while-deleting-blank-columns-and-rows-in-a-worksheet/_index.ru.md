---
title: Обновлять ссылки на других листах при удалении пустых столбцов и строк на листе
type: docs
weight: 5000
url: /ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

Когда вы удаляете пустые столбцы и строки на листе, его ссылки на других листах становятся недействительными. Если вы хотите избежать такого поведения и хотите, чтобы ссылки на текущий рабочий лист на других рабочих листах также обновлялись, используйте[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) свойство и установите его в**истинный**.

{{% /alert %}}

## **Обновлять ссылки на других листах при удалении пустых столбцов и строк на листе**

 См. следующий пример кода и его вывод на консоль. Ячейка E3 на втором рабочем листе имеет формулу = Sheet1!C3, которая ссылается на ячейку C3 на первом рабочем листе. Если вы установите[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) собственность как**истинный** , эта формула будет обновлена и станет =Лист1!А1 при удалении пустых столбцов и строк на первом листе. Однако, если вы установите[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) собственность как**ЛОЖЬ**, формула в ячейке E3 второго листа останется =Sheet1!C3 и станет недействительной.

### **Образец программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Консольный вывод**

 Это консольный вывод приведенного выше примера кода, когда[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) свойство установлено как**истинный**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

 Это консольный вывод приведенного выше примера кода, когда[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) свойство установлено как**ЛОЖЬ**. Как видите, формула в ячейке E3 второго рабочего листа не обновляется, и значение ее ячейки теперь равно 0 вместо 4, что недопустимо.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}

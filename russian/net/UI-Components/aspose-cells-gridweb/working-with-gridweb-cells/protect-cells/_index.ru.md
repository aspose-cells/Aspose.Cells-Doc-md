---
title: Защитить Cells
type: docs
weight: 50
url: /ru/net/protect-cells/
---
{{% alert color="primary" %}} 

В этом разделе описывается несколько методов защиты ячеек. Использование этих методов позволяет разработчикам запретить пользователям редактировать все или выбранный диапазон ячеек на листе.

{{% /alert %}} 
## **Защита Cells**
 Aspose.Cells.GridWeb предоставляет несколько различных методов управления уровнем защиты ячеек, когда[Режим редактирования](/cells/ru/net/enable-different-gridweb-modes/#edit-mode) (режим по умолчанию). Это защищает ячейки от изменения конечными пользователями.
### **Сделать все Cells только для чтения**
Чтобы настроить все ячейки на листе только для чтения, вызовите метод SetAllCellsReadonly рабочего листа.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Сделать все Cells редактируемым**
Чтобы снять защиту со всех ячеек, вызовите метод SetAllCellsEditable рабочего листа. Этот метод имеет эффект, противоположный методу SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Создание выбранного Cells Только для чтения**
Чтобы защитить только диапазон ячеек:

1. Сначала сделайте все ячейки редактируемыми, вызвав метод SetAllCellsEditable.
1. Укажите диапазон ячеек, которые нужно защитить, вызвав метод SetReadonlyRange рабочего листа. Этот метод принимает количество строк и столбцов, чтобы указать диапазон ячеек.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Делаем выбранное Cells редактируемым**
Чтобы снять защиту с диапазона ячеек:

1. Сделайте все ячейки доступными только для чтения, вызвав метод SetAllCellsReadonly.
1. Укажите диапазон ячеек, которые будут доступны для редактирования, вызвав метод SetEditableRange рабочего листа. Этот метод принимает количество строк и столбцов, чтобы указать диапазон ячеек.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}

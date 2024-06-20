---
title: Защита ячеек
type: docs
weight: 50
url: /ru/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, защита, только чтение, редактирование
description: Эта статья рассказывает о том, как защищать ячейки в GridWeb.
---

{{% alert color="primary" %}} 

В этой теме описано несколько техник защиты ячеек. Использование этих техник позволяет разработчикам ограничить пользователей от редактирования всех или выбранного диапазона ячеек на листе.

{{% /alert %}} 
## **Защита ячеек**
Aspose.Cells.GridWeb предоставляет несколько различных техник для контроля уровня защиты ячеек, когда управление находится в [режиме редактирования](/cells/ru/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (режим по умолчанию). Это защищает ячейки от изменения конечными пользователями.
### **Установка всех ячеек только для чтения**
Чтобы установить все ячейки на листе только для чтения, вызовите метод SetAllCellsReadonly листа.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Установка всех ячеек для редактирования**
Чтобы удалить защиту со всех ячеек, вызовите метод SetAllCellsEditable листа. Этот метод имеет противоположный эффект по сравнению с методом SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Установка выбранных ячеек только для чтения**
Чтобы защитить только диапазон ячеек:

1. Сначала сделайте все ячейки доступными для редактирования, вызвав метод SetAllCellsEditable.
1. Укажите диапазон ячеек для защиты, вызвав метод SetReadonlyRange таблицы. Этот метод принимает количество строк и столбцов для определения диапазона ячеек.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Сделать выбранные ячейки доступными для редактирования**
Чтобы снять защиту с диапазона ячеек:

1. Сделайте все ячейки только для чтения, вызвав метод SetAllCellsReadonly.
1. Укажите диапазон ячеек, которые будут доступны для редактирования, вызвав метод SetEditableRange таблицы. Этот метод принимает количество строк и столбцов для указания диапазона ячеек.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}

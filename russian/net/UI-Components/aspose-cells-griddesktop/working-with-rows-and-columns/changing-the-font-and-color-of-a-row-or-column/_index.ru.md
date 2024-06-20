---
title: Изменение шрифта и цвета строки или столбца
type: docs
weight: 110
url: /ru/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop,шрифт,цвет
description: Эта статья рассказывает о том, как изменить шрифт и цвет в строке или столбце в GridDesktop.
---

{{% alert color="primary" %}} 

В этой статье мы обсудим изменение шрифта и цвета шрифта строк и столбцов листа. Это базовый уровень функции форматирования, предлагаемой Aspose.Cells.GridDesktop, которая позволяет разработчикам настраивать отображение своих листов, делая их более презентабельными.

{{% /alert %}} 
## **Изменение шрифта и цвета столбца**
Чтобы изменить шрифт и цвет столбца с использованием Aspose.Cells.GridDesktop, выполните следующие шаги:

- Получить доступ к любому желаемому **Рабочему листу**
- Получите доступ к **Столбцу**, шрифт и цвет которого нужно изменить
- Создайте настроенный **Шрифт**
- Задайте **Шрифт** **Столбца** созданному
- Наконец, задайте **Цвет Шрифта** **Столбца** любым желаемым **Цветом**



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Изменение шрифта и цвета строки**
- Получить доступ к любому желаемому **Рабочему листу**
- Получите доступ к **Строке**, шрифт и цвет которой нужно изменить
- Создайте настроенный **Шрифт**
- Задайте **Шрифт** **Строки** созданному
- Наконец, задайте **Цвет Шрифта** **Строки** любым желаемым **Цветом**



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}

---
title: Изменение шрифта и цвета строки или столбца
type: docs
weight: 110
url: /ru/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

В этом разделе мы обсудим изменение шрифта и цвета шрифта строк и столбцов рабочего листа. Это базовый уровень функции форматирования, предлагаемый Aspose.Cells.GridDesktop, который позволяет разработчикам настраивать представление своих рабочих листов, чтобы сделать их более презентабельными.

{{% /alert %}} 
## **Изменение шрифта и цвета столбца**
Чтобы изменить шрифт и цвет столбца с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

-  Доступ к любому желаемому**Рабочий лист**
-  Доступ к**Столбец** чей шрифт и цвет должны быть изменены
-  Создайте индивидуальный**Шрифт**
-  Установить**Шрифт** принадлежащий**Столбец** к индивидуальному
-  Наконец, установите**Цвет шрифта** принадлежащий**Столбец** на любой желаемый**Цвет**



{{< highlight "csharp" >}}

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
-  Доступ к любому желаемому**Рабочий лист**
-  Доступ к**Строка** чей шрифт и цвет должны быть изменены
-  Создайте индивидуальный**Шрифт**
-  Установить**Шрифт** принадлежащий**Строка** к индивидуальному
-  Наконец, установите**Цвет шрифта** принадлежащий**Строка** на любой желаемый**Цвет**



{{< highlight "csharp" >}}

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

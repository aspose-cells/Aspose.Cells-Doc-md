---
title: Применение стиля к строке или столбцу
type: docs
weight: 50
url: /ru/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

В этом разделе мы обсудим изменение шрифта и цвета шрифта строк и столбцов рабочего листа. Это базовый уровень функции форматирования, предлагаемый Aspose.Cells.GridDesktop, который позволяет разработчикам настраивать представление своих рабочих листов, чтобы сделать их более презентабельными.

{{% /alert %}} 
## **Применение стиля к столбцу**
Чтобы применить пользовательский стиль к столбцу с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

-  Доступ к любому желаемому**Рабочий лист**
-  Доступ к**Столбец** к которому мы хотим применить**Стиль**
-  Получать**Стиль** принадлежащий**Столбец**
-  Установлен**Стиль** свойства в соответствии с вашими индивидуальными потребностями
-  Наконец, установите**Стиль** принадлежащий**Столбец** с обновленным

 Существует множество полезных свойств и методов, предлагаемых**Стиль** объект, который разработчики могут использовать для настройки стиля в соответствии со своими требованиями.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Применение стиля к строке**
Чтобы применить пользовательский стиль к строке с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

-  Доступ к любому желаемому**Рабочий лист**
-  Доступ к**Строка** к которому мы хотим применить**Стиль**
-  Получать**Стиль** принадлежащий**Строка**
-  Установлен**Стиль** свойства в соответствии с вашими индивидуальными потребностями
-  Наконец, установите**Стиль** принадлежащий**Строка** с обновленным

 Существует множество полезных свойств и методов, предлагаемых**Стиль** объект, который разработчики могут использовать для настройки стиля в соответствии со своими требованиями.



{{< highlight "csharp" >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}

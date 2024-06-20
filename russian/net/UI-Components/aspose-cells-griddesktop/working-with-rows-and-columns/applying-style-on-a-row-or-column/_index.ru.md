---
title: Применение стиля к строке или столбцу
type: docs
weight: 50
url: /ru/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, стиль, строка, столбец
description: Эта статья знакомит с применением стиля к строке или столбцу в GridDesktop.
---

{{% alert color="primary" %}} 

В этой статье мы обсудим изменение шрифта и цвета шрифта строк и столбцов листа. Это базовый уровень функции форматирования, предлагаемой Aspose.Cells.GridDesktop, которая позволяет разработчикам настраивать отображение своих листов, делая их более презентабельными.

{{% /alert %}} 
## **Применение стиля к столбцу**
Чтобы применить настраиваемый стиль к столбцу с использованием Aspose.Cells.GridDesktop, выполните следующие шаги:

- Получить доступ к любому желаемому **Рабочему листу**
- Получите доступ к **столбцу**, на котором мы хотим применить **стиль**
- Получите **стиль** **столбца**
- Установите свойства **стиля** в соответствии с вашими индивидуальными потребностями
- Наконец, установите **стиль** **столбца** с обновленным

Существует множество полезных свойств и методов, предлагаемых объектом **Style**, которые могут быть использованы разработчиками для настройки стиля в соответствии с их требованиями.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Применение стиля к строке**
Чтобы применить настраиваемый стиль к строке с использованием Aspose.Cells.GridDesktop, выполните следующие шаги:

- Получить доступ к любому желаемому **Рабочему листу**
- Получите доступ к **строке**, на которой мы хотим применить **стиль**
- Получите **стиль** **строки**
- Установите свойства **стиля** в соответствии с вашими индивидуальными потребностями
- Наконец, установите **стиль** **строки** с обновленным

Существует множество полезных свойств и методов, предлагаемых объектом **Style**, которые могут быть использованы разработчиками для настройки стиля в соответствии с их требованиями.



{{< highlight csharp >}}

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

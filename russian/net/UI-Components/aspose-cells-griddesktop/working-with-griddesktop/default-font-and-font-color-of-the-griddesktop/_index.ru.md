---
title: Шрифт по умолчанию и цвет шрифта GridDesktop
type: docs
weight: 70
url: /ru/net/default-font-and-font-color-of-the-griddesktop/
---
## **Возможные сценарии использования**
Иногда вам нужно изменить шрифт по умолчанию и цвет шрифта GridDesktop. Пожалуйста, используйте следующие два свойства для этой цели. Вы можете получить доступ к этим свойствам во время разработки или во время выполнения в зависимости от ваших потребностей.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Изменение шрифта по умолчанию и цвета шрифта во время разработки**
На следующем снимке экрана показано, как изменить шрифт по умолчанию и цвет шрифта GridDesktop во время разработки.

![дело:изображение_альтернативный_текст](default-font-and-font-color-of-the-griddesktop_1.png)
## **Изменить шрифт по умолчанию и цвет шрифта во время выполнения**
В следующем примере кода объясняется, как изменить шрифт по умолчанию и цвет шрифта GridDesktop во время выполнения.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

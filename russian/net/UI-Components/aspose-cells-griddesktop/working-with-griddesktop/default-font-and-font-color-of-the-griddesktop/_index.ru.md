---
title: Шрифт и цвет шрифта по умолчанию в GridDesktop
type: docs
weight: 70
url: /ru/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop,шрифт,цвет
description: В этой статье представлены шрифт и цвет шрифта по умолчанию в GridDesktop.
---

## **Возможные сценарии использования**
Иногда вам нужно изменить шрифт и цвет шрифта по умолчанию в GridDesktop. Используйте следующие два свойства для этой цели. Вы можете получить доступ к этим свойствам на этапе проектирования или во время выполнения, в зависимости от ваших потребностей.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Изменение шрифта и цвета шрифта по умолчанию на этапе проектирования**
Ниже приведено изображение экрана, показывающее, как изменить шрифт и цвет шрифта по умолчанию в GridDesktop на этапе проектирования.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Изменение шрифта и цвета шрифта по умолчанию во время выполнения**
В приведенном ниже образце кода объясняется, как изменить шрифт и цвет шрифта по умолчанию в GridDesktop во время выполнения.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

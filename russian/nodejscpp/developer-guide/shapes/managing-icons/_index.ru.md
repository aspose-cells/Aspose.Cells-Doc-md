---  
title: Добавление значков на лист с помощью Node.js через C++  
linktitle: Управление значками  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/insert-svg-to-excel/  
---  

## Добавление значков на лист в Aspose.Cells for Node.js via C++

Если вам нужно использовать [Aspose.Cells](https://products.aspose.com/cells/) для добавления 'значков' в файл Excel, то этот документ может предоставить вам некоторую помощь.

Интерфейс Excel, соответствующий операции вставки значка, выглядит следующим образом:

![](1.png)

- Выберите позицию для вставки значка на лист
- Левый щелчок *Вставка*->*Значки*
- В открывшемся окне выберите значок в красном прямоугольнике на рисунке выше
- Левый щелчок *Вставить*, он вставится в файл Excel.

Эффект будет следующий:

![](2.png)

Здесь мы подготовили *пример кода*, чтобы помочь вставить иконки с помощью [Aspose.Cells](https://products.aspose.com/cells/). Также есть необходимый [пример файла](sample.xlsx) и [ресурсный файл иконок](icon.zip). Мы использовали интерфейс Excel для вставки иконки с таким же визуальным эффектом, как у [ресурсного файла](icon.zip) в [примерном файле](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Когда вы выполните вышеуказанный код в своем проекте, вы получите следующие результаты:

![](3.png)  


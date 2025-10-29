---
title: Конвертация Smart Art в сгруппированную форму с помощью Node.js через C++
linktitle: Преобразовать умное изображение в групповую форму
type: docs
weight: 200
url: /ru/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Возможные сценарии использования**

Вы можете преобразовать форму Smart Art в группу форм, используя метод [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Это позволит вам работать с формой smart art как с группой. Следовательно, у вас будет доступ к отдельным частям или фигурам группы.

## **Преобразование SmartArt в форму группы**

Следующий пример кода загружает [пример файла Excel](55541793.xlsx), содержащий фигуру Smart Art, как показано на этом скриншоте. Далее он преобразует фигуру Smart Art в группу и выводит свойство Shape.isGroup. Пожалуйста, смотрите вывод в консоли ниже.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Вывод в консоль**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

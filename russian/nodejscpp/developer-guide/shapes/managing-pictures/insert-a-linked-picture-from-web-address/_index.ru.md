---  
title: Вставка связанного изображения из веб адреса с помощью Node.js via C++  
linktitle: Вставить связанное изображение из веб адреса  
type: docs  
weight: 450  
url: /ru/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Узнайте, как вставить связанное изображение из веб адреса в лист с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Иногда необходимо вставить изображение из интернета (http://) в лист. Для этого укажите URL изображения, и изображение будет загружено каждый раз при открытии файла в Excel. Изображение не встроено физически в документ Excel, а указывает на веб-ресурс.  
{{% /alert %}}  

## **Использование Microsoft Excel**  

В Microsoft Excel (например, 2007 год):  

1. Нажмите меню **Вставка** и выберите **Изображение**.  
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.  

## **Использование Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ поддерживает добавление связанного изображения с помощью [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).  

Следующий пример показывает, как добавить связанное изображение из веб-адреса в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  


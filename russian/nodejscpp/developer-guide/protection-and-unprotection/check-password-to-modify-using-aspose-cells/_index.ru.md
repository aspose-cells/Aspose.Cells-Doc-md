---  
title: Проверка пароля для изменений с помощью Aspose.Cells for Node.js via C++  
linktitle: Проверка пароля для изменений  
type: docs  
weight: 2400  
url: /ru/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Узнайте, как проверить, совпадает ли пароль для внесения изменений, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 Иногда необходимо программно проверить, совпадает ли данный пароль с «Паролем для внесения изменений». Aspose.Cells предоставляет метод `WorkbookSettings.writeProtection.validatePassword()`, который можно использовать для проверки правильности введенного пароля.  
{{% /alert %}}  

## **Проверка пароля на доступ на изменение в Microsoft Excel**  

Вы можете указать **Пароль на открытие** и **Пароль на доступ на изменение** при создании ваших книг в Microsoft Excel. Пожалуйста, посмотрите этот скриншот, который показывает интерфейс, предоставляемый Microsoft Excel для указания этих паролей.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Проверка пароля для изменений с помощью Aspose.Cells for Node.js via C++**  

 Следующий код загружает файл [исходного Excel](5112232.xlsx). В нем установлен пароль для открытия 1234 и пароль для внесения изменений 5678. Код сначала проверяет, правильен ли пароль для изменений 567, и возвращает false, затем проверяет, правильен ли пароль 5678, и возвращает true.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Вывод в консоль**  

Вот консольный вывод вышеуказанного образца кода после загрузки файла [исходного Excel](5112232.xlsx).  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  

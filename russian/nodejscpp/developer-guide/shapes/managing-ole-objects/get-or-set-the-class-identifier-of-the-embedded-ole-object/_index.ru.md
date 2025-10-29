---  
title: Получить или установить идентификатор класса встроенного объекта OLE с помощью Node.js через C++  
linktitle: Получение или установка идентификатора класса встроенного объекта OLE  
type: docs  
weight: 200  
url: /ru/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Узнайте, как получать или устанавливать идентификатор класса встроенных объектов OLE в Node.js с помощью Aspose.Cells через C++.  
---  

## **Возможные сценарии использования**  
Aspose.Cells предоставляет свойство [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--), которое можно использовать для получения или установки идентификатора класса встроенного объекта OLE. Идентификаторы класса объектов OLE — это фактически GUIDs, т.е. Глобальные уникальные идентификаторы. GUID всегда имеет длину 16 байт; поэтому идентификаторы класса также длиной 16 байт. Они часто встречаются в реестре Windows и предоставляют информацию хост-приложению о том, как открыть встроенные объекты OLE, содержащие различные встроенные ресурсы внутри клиентского приложения.

## **Получение или установка идентификатора класса встроенного объекта OLE**  
Следующий скриншот показывает идентификатор класса объекта OLE, т.е. GUID, который был считан из [пример файла Excel](5115190.xls), содержащего встроенный PowerPoint OLE-объект.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Образец кода**  
Пожалуйста, смотрите следующий пример кода, выполненный с [примером файла Excel](5115190.xls), и его выводом в консоль, который печатает идентификатор класса OLE-объекта, т.е. GUID. Выведенный GUID точно такой же, как отображается на скриншоте.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Вывод в консоль**  
Это вывод консоли указанного выше примера кода при выполнении с [примером файла Excel](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

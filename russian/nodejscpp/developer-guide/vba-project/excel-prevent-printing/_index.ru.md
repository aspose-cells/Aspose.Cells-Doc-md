---  
title: Как запретить пользователям печатать файл Excel с помощью Node.js через C++  
linktitle: Как предотвратить пользователей от печати файлов Excel  
type: docs  
weight: 600  
url: /ru/nodejs-cpp/how-to-prevent-printing-excel/  
description: Узнайте, как запретить пользователям печать файлов Excel с помощью Aspose.Cells for Node.js via C++.  
keywords: печать excel, предотвращение печати excel, как предотвратить пользователей от печати excel, excel предотвращение печати, предотвращение печати рабочей книги, Предотвращение печати всей книги с помощью VBA.  
---  

## **Возможные сценарии использования**  
В нашей ежедневной работе в файле Excel может содержаться важная информация; чтобы защитить внутренние данные от распространения, компания не разрешит их печать. Этот документ расскажет, как предотвратить печать файлов Excel другими.  

## **Как предотвратить пользователей от печати файла в MS-Excel**  
Вы можете применить следующий VBA-код для защиты вашего конкретного файла от печати.  
1. Откройте свою книгу, которую вы не разрешаете печатать.  
1. Выберите вкладку "Developer" на ленте Excel и нажмите кнопку "View Code" в разделе "Controls". Или удерживайте клавиши ALT + F11 для открытия окна Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. Затем в левом окне Обозревателя проекта дважды щелкните ЭтотРабочийКнига, чтобы открыть модуль, и добавьте некоторые VBA-коды.  
<br>  
<img src="2.png" width=70% />  
1. Затем сохраните и закройте этот код, вернитесь в рабочую книгу, и теперь при попытке распечатать файл образца выводится предупреждение:  
<br>  
<img src="3.png" width=70% />  

## **Как запретить пользователям печатать файл Excel с помощью Aspose.Cells for Node.js via C++**  

Следующий пример кода показывает, как предотвратить печать файла Excel:  

1. Загрузите [образец файла](sample.xlsx).  
1. Получите объект VbaModuleCollection из свойства VbaProject рабочей книги.  
1. Получите объект VbaModule через имя "ThisWorkbook".  
1. Установите свойство codes объекта VbaModule.  
1. Сохраните образец файла в формате [xlsm](out.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

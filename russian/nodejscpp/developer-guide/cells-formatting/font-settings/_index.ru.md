---  
title: Настройки шрифта с Node.js через C++  
linktitle: Настройки шрифта  
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц. Она поддерживает установку настроек шрифта для ячеек, позволяя пользователям настраивать стиль шрифта и свойства ячеек. В этой статье рассказывается о том, как использовать библиотеку Aspose.Cells для установки настроек шрифта ячеек.  
keywords: Aspose.Cells, ячейки, настройки шрифта, стили, свойства, Node.js через C++  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
Внешний вид и ощущение текста могут быть управляемыми путем изменения настроек шрифта. Настройки шрифта могут включать имя, стиль, размер, цвет и другие эффекты шрифтов. Как и Microsoft Excel, Aspose.Cells также поддерживает настройку шрифта ячеек.  
{{% /alert %}}  

## **Настройка настроек шрифта**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получать доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) — это объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells предоставляет методы класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) и [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-), которые используются для получения и установки стиля форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) предоставляет свойства для настройки настроек шрифта.  

### **Установка названия шрифта**  

Разработчики могут применить любой шрифт к тексту внутри ячейки, используя метод [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Установка стиля шрифта на жирный**  

Разработчики могут сделать текст полужирным, установив метод [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) в значение **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Установка размера шрифта**  

Установите размер шрифта с помощью метода [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Установка цвета шрифта**  

Используйте метод [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) для установки цвета шрифта. Выберите любой цвет из перечисления Color (часть Node.js) и присвойте его методу [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-).   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Установка типа подчеркивания шрифта**  

Используйте метод [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) для подчеркивания текста. Aspose.Cells предлагает различные предопределенные типы подчеркивания шрифта в перечислении [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype).  

|**Типы подчеркивания шрифта**|**Описание**|  
| :- | :- |  
|Accounting| Одиночная линия подчеркивания для учета  
|Double| Двойное подчеркивание  
|DoubleAccounting| Двойная линия подчеркивания для учета  
|None| Без подчеркивания  
|Single| Одиночная линия подчеркивания  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Установка эффекта зачеркивания**  

Примените зачеркивание, установив метод [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) в значение **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Установка эффекта нижнего индекса**  

Примените индекс нижнего регистра, установив метод [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) в значение **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Установка верхнего индекса на шрифт**  

Разработчики могут применить эффект надстрочного текста, установив метод [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) объекта [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) в значение **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Продвинутые темы**  
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  



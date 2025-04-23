---  
title: Проверка, содержит ли книга скрытые внешние ссылки, с помощью Node.js через C++  
linktitle: Проверка, содержит ли рабочая книга скрытые внешние ссылки  
type: docs  
weight: 230  
url: /ru/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Узнайте, как проверить, содержит ли книга скрытые внешние ссылки, с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  
Иногда книга содержит внешние ссылки, которые скрыты и не могут быть отображены в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, независимо от их видимости. Вы можете проверить свойство [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--), чтобы определить, видима ли внешняя ссылка или нет.

## **Проверка, содержит ли рабочая книга скрытые внешние ссылки**  
Следующий пример загружает [исходный файл Excel](5115413.xlsx), содержащий скрытые внешние ссылки. Эти ссылки не видны в Microsoft Excel, но присутствуют в книге. После вывода свойств [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) и [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--), выводится свойство [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--). В консольном выводе ниже видно, что все внешние ссылки скрыты.

### **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **Вывод в консоль**  
Вот вывод консоли вышеприведенного образца кода при выполнении с заданным [образцовым файлом Excel](5115413.xlsx).

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  

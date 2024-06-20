---
title: Веб расширения  дополнения для офиса
type: docs
weight: 120
url: /ru/java/web-extensions-office-add-ins/
---

Веб-расширения расширяют возможности приложений Office и взаимодействуют с контентом в документах Office. Веб-расширения добавляют дополнительную функциональность в клиент Office для улучшения опыта пользователя и продуктивности.

Aspose.Cells также предоставляет возможность работать с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить веб-расширения (дополнения Office) в Excel, щелкнув вкладку **Вставка**, а затем щелкнув ссылку **Склад**/**Получить дополнения**. В поле дополнений найдите и добавьте необходимое дополнение.

Aspose.Cells также предоставляет функцию добавления веб-расширений с использованием классов WebExtension и WebExtensionTaskPane. Нижеприведенный образец кода демонстрирует использование классов WebExtension и WebExtensionTaskPane для добавления веб-расширения в файл Excel. Пожалуйста, ознакомьтесь с [выходным файлом Excel](AddWebExtension_Out.xlsx), сгенерированным кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Доступ к информации веб-расширения**

Aspose.Cells предоставляет возможность доступа к информации о веб-расширениях в файле Excel. Нижеприведенный образец кода демонстрирует, как получить доступ к информации о веб-расширении, загружая [образец файла Excel](WebExtensionsSample.xlsx). Пожалуйста, ознакомьтесь с выходными данными в консоли, сгенерированными кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **Вывод в консоль**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}

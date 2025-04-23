---
title: Веб расширения  дополнения для офиса
type: docs
weight: 130
url: /ru/net/web-extensions-office-add-ins/
---

Веб-расширения расширяют возможности приложений Office и взаимодействуют с контентом в документах Office. Веб-расширения добавляют дополнительную функциональность в клиент Office для улучшения опыта пользователя и продуктивности.

Aspose.Cells также предоставляет возможность работать с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить Веб-расширения (надстройки для Office) в Excel, нажав вкладку **Вставка**, а затем щелкнув ссылку **Магазин**/**Получить надстройки**. В поле надстроек найдите нужную надстройку и добавьте ее.

Aspose.Cells также предоставляет возможность добавления Веб-расширений с помощью классов [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane). Следующий образец кода демонстрирует использование классов [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) для добавления веб-расширения в файл Excel. Пожалуйста, обратитесь к [выходному файлу Excel](89849869.xlsx), сгенерированному кодом для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Доступ к информации веб-расширения**

Aspose.Cells предоставляет возможность доступа к информации о Веб-расширениях в файле Excel. Следующий образец кода демонстрирует, как получить информацию о веб-расширении, загрузив [образец файла Excel](89849870.xlsx). Пожалуйста, обратитесь к сгенерированному коду консоли для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}

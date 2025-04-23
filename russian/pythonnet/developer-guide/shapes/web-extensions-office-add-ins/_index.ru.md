---
title: Веб расширения  дополнения для офиса
type: docs
weight: 130
url: /ru/python-net/web-extensions-office-add-ins/
---

Веб-расширения расширяют возможности приложений Office и взаимодействуют с контентом в документах Office. Веб-расширения добавляют дополнительную функциональность в клиент Office для улучшения опыта пользователя и продуктивности.

Aspose.Cells for Python via .NET также предоставляет возможность работы с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить Веб-расширения (надстройки для Office) в Excel, нажав вкладку **Вставка**, а затем щелкнув ссылку **Магазин**/**Получить надстройки**. В поле надстроек найдите нужную надстройку и добавьте ее.

Aspose.Cells for Python via .NET также включает возможность добавления веб-расширений с помощью классов [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). Следующий пример кода демонстрирует использование классов [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) для добавления веб-расширения в файл Excel. Пожалуйста, ознакомьтесь с [выходным файлом Excel](89849869.xlsx), сгенерированным этим кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Доступ к информации веб-расширения**

Aspose.Cells for Python via .NET предоставляет возможность доступа к информации о веб-расширениях в файле Excel. Следующий пример показывает, как получить информацию о веб-расширениях, загрузив [пример файла Excel](89849870.xlsx). Пожалуйста, ознакомьтесь с выводом в консоль, сгенерированным кодом, для справки.

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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

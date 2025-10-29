---
title: Веб расширения  дополнения Office с Golang через C++
linktitle: Веб расширения  дополнения для офиса
type: docs
weight: 130
url: /ru/go-cpp/web-extensions-office-add-ins/
description: Узнайте, как добавлять и получать доступ к веб расширениям (дополнениям Office) в файлах Excel с Aspose.Cells с Golang через C++.
---

Расширения веб расширяют возможности приложений Office и взаимодействуют с содержимым документов Office. Они добавляют дополнительную функциональность клиентским приложениям Office для улучшения пользовательского опыта и повышения производительности.

Aspose.Cells также предоставляет возможность работать с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить расширения веб (надстройки Office) в Excel, кликнув на вкладку **Вставка**, а затем на ссылку **Магазин**/**Получить надстройки**. В окне надстроек найдите нужную надстроку и добавьте её.

Aspose.Cells также предоставляет возможность добавлять расширения веб, используя классы [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). Следующий пример демонстрирует использование классов [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) для добавления веб-расширения в файл Excel. Пожалуйста, посмотрите на [выходной файл Excel](89849869.xlsx), созданный этим кодом.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Доступ к информации веб-расширения**

Aspose.Cells предоставляет возможность получать информацию о расширениях веб в файле Excel. Следующий пример показывает, как получить информацию о веб-расширениях, загрузив [пример файла Excel](89849870.xlsx). Обратите внимание на вывод в консоль, сгенерированный кодом.

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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

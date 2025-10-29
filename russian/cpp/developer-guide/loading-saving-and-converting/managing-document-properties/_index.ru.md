---
title: Управление свойствами документа
type: docs
weight: 30
url: /ru/cpp/managing-document-properties/
---

## **Возможные сценарии использования**
Aspose.Cells позволяет работать с встроенными и настраиваемыми свойствами документа. Здесь представлен интерфейс Microsoft Excel для открытия этих *свойств документа*. Просто щелкните *Дополнительные свойства*, как показано на этом скриншоте, и просмотрите их.

![todo:image_alt_text](managing-document-properties_1.png)
## **Управление свойствами документа**
В следующем примере кода загружается [образец файла Excel](23166989.xlsx) и считываются встроенные свойства документа, например, *Название, Тема*, а затем они изменяются. Затем также считывается настраиваемое свойство документа, т.е. *MyCustom1*, и затем добавляется новое настраиваемое свойство документа, т. е. *MyCustom5*, и записывается [выходной файл Excel](23166986.xlsx). На следующем скриншоте показан эффект примера кода на образец файла Excel.

![todo:image_alt_text](managing-document-properties_2.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Вывод в консоль**
Это вывод в консоль вышеуказанного примера кода при выполнении с предоставленным [образцом файла Excel](23166989.xlsx).

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}

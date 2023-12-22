---
title: Управление свойствами документа
type: docs
weight: 30
url: /ru/cpp/managing-document-properties/
---
##  **Возможный сценарий использования**
 Aspose.Cells позволяет работать со встроенными и пользовательскими свойствами документа. Вот интерфейс Excel Microsoft для открытия этих*Свойства документа*. Просто нажмите *Дополнительные свойства.*как показано на этом снимке экрана, и просмотрите их.

![задача: image_alt_text](managing-document-properties_1.png)
##  **Управление свойствами документа**
 Следующий пример кода загружается[образец файла Excel](23166989.xlsx) и читает встроенные свойства документа, например*Название, Тема* а затем меняет их. Затем он также считывает свойство пользовательского документа, т.е.*МойCustom1* а затем добавляет новое свойство пользовательского документа, т.е.*МойCustom5* и пишет[выходной файл Excel](23166986.xlsx)На следующем снимке экрана показано влияние примера кода на образец файла Excel.

![задача: image_alt_text](managing-document-properties_2.png)
##  **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


##  **Консольный вывод**
 Это вывод консоли приведенного выше примера кода при выполнении с предоставленным[образец файла Excel](23166989.xlsx).

{{< highlight "java" >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}

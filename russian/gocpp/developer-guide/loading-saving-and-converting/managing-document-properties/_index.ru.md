---
title: Управление свойствами документа
type: docs
weight: 30
url: /ru/go-cpp/managing-document-properties/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет работать с встроенными и настраиваемыми свойствами документа. Здесь представлен интерфейс Microsoft Excel для открытия этих *свойств документа*. Просто щелкните *Дополнительные свойства*, как показано на этом скриншоте, и просмотрите их.

![todo:image_alt_text](managing-document-properties_1.png)

## **Управление свойствами документа**

Следующий пример кода загружает [пример файла Excel](23166989.xlsx) и читает встроенные свойства документа, например, *Title* и *Subject*, затем изменяет их. Также он читает пользовательское свойство документа, i.e., *MyCustom1*, и добавляет новое пользовательское свойство, i.e., *MyCustom5*, а затем сохраняет [выходной файл Excel](23166986.xlsx). Следующий скриншот показывает эффект этого кода на пример файла Excel.

![todo:image_alt_text](managing-document-properties_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **Вывод в консоль**

Это вывод из консоли приведённого выше примера кода при выполнении с предоставленным [примером файла Excel](23166989.xlsx).

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}

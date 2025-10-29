---
title: Установка свойств ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Golang через C++
linktitle: Настройка свойств ScaleCrop и LinksUpToDate
type: docs
weight: 320
url: /ru/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Узнайте, как установить свойства ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) и [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) — два расширенных встроенных свойства документа, определённых внутри формата OpenXml. Назначение этих свойств:

## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Следующий пример кода устанавливает расширенные встроенные свойства документа [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) и [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) для книги Excel. Проверьте созданный с помощью этого кода файл Excel, измените его расширение на .zip, извлеките содержимое и откройте app.xml, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}

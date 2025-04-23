---
title: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 320
url: /ru/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Возможные сценарии использования**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) и [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) - это два расширенных встроенных свойства документа, определенных в формате OpenXml. Цель этих свойств следующая
## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
В следующем образце кода устанавливаются [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) и [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) расширенные встроенные свойства документа книги. Пожалуйстa, проверьте [выходной файл Excel](5115500.xlsx), сгенерированный с помощью этого кода, измените его расширение на .zip, извлеките его содержимое и просмотрите файл app.xml как показано на снимке экрана выше.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 320
url: /ru/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Возможные сценарии использования**
[МасштабОбрезка](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) а также[СсылкиUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)— это два расширенных встроенных свойства документа, определенные в формате OpenXml. Назначение этих свойств следующее
## **1) Масштабирование**
 Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в**ПРАВДА**чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в**ЛОЖНЫЙ** чтобы включить обрезку миниатюры документа, чтобы отображались только те разделы, которые подходят для дисплея.

Возможные значения для этого элемента определяются логическим типом данных W3C XML Schema.
## **2) LinksUpToDate**
 Этот элемент указывает, являются ли гиперссылки в документе актуальными. Установите этот элемент в**ПРАВДА** чтобы указать, что гиперссылки обновлены. Установите этот элемент в**ЛОЖНЫЙ** чтобы указать, что гиперссылки устарели.

Возможные значения для этого элемента определяются логическим типом данных W3C XML Schema.
## **Снимок экрана, показывающий эти свойства в файле app.xml**
![дело:изображение_альтернативный_текст](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
 В следующем примере кода задается[МасштабОбрезка](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) а также[СсылкиUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) расширенные встроенные свойства документа книги. Пожалуйста, проверьте[выходной файл excel](5115500.xlsx)созданный с помощью этого кода, измените его расширение на .zip, извлеките его содержимое и просмотрите app.xml, как показано на снимке экрана выше.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}

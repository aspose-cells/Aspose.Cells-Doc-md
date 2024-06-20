---
title: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 1050
url: /ru/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Возможные сценарии использования**
[МасштабОбрезка](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) и [СсылкиАктуальны](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) - это два дополнительных встроенных свойства документа, определенные в формате OpenXml. Цель этих свойств следующая:
## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **true**, чтобы разрешить масштабирование миниатюры документа для отображения. Установите этот элемент в **false**, чтобы обрезать миниатюру документа и показать только секции, подходящие для отображения.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **true**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **false**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Приведенный ниже образец кода устанавливает [свойства ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) и [свойства LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) расширенных встроенных свойств документа рабочей книги. Пожалуйста, проверьте [файл Excel с выводом](5472494.xlsx), сгенерированный этим кодом, измените его расширение на .zip, извлеките его содержимое и посмотрите файл aap.xml, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}

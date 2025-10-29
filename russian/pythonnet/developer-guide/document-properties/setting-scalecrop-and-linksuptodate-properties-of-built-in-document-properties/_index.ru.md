---
title: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 320
url: /ru/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Возможные сценарии использования**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) и [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) — два расширенных встроенных свойства документа, определенных внутри формата OpenXml. Их назначение —
## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.
## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Следующий пример кода устанавливает расширенные встроенные свойства документа [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) и [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) для рабочей книги. Проверьте сгенерированный файл Excel (5115500.xlsx), измените его расширение на .zip, распакуйте содержимое и просмотрите app.xml, как показано на скриншоте выше.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}

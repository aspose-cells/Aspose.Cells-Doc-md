---
title: Используйте пользовательские XML части в Aspose.Cells с Golang через C++
linktitle: Используйте пользовательские XML части
type: docs
weight: 390
url: /ru/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Узнайте, как программно использовать пользовательские XML части в файлах Excel с помощью Aspose.Cells и Golang через C++.
---

## Использование пользовательских XML-частей в Aspose.Cells

Пользовательские XML-части — это XML-данные, сохраняемые различными приложениями, такими как SharePoint, внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому интерфейс для их добавления отсутствует. Вы можете просмотреть эти данные, изменив расширение файла с **.xlsx** на **.zip**, а затем открыв его через **WinZip**. Также ZIP-файл можно открыть с помощью сторонней программы для работы с ZIP-архивами, например WinRAR или WinZip. Данные хранятся внутри папки **customXml**.

Вы можете добавлять пользовательские XML-части, используя Aspose.Cells через метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/).

Следующий пример использует метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) для добавления **Book Catalog XML** с именем **BookStore**. На изображении показан результат этого кода. Как видно, XML-каталог книг добавлен внутри узла BookStore, который является названием этого свойства.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++ код для использования пользовательских XML-частей

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Связанная статья

- [Добавление пользовательских свойств, видимых в панели информации документа](/cells/ru/cpp/adding-custom-properties-visible-inside-document-information-panel/)

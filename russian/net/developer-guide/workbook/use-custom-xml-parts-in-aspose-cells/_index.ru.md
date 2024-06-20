---
title: Использование пользовательских XML частей в Aspose.Cells
type: docs
weight: 390
url: /ru/net/use-custom-xml-parts-in-aspose-cells/
---

## Использование пользовательских XML-частей в Aspose.Cells

Пользовательские XML-части - это XML-данные, хранящиеся различными приложениями, такими как SharePoint и т. д., внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому в нем нет графического интерфейса для их добавления. Вы можете просмотреть эти данные, изменив расширение **.xlsx** на **.zip** и затем открыв файл с помощью **WinZip**. Вы также можете открыть ZIP-файл с помощью любой сторонней утилиты для архивации под Windows, такой как WinRAR или WinZip. Данные находятся внутри папки **customXml**.

Вы можете добавлять пользовательские XML-части с помощью Aspose.Cells через метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index).

Приведенный ниже образец кода использует метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) и добавляет **Book Catalog XML**, его имя **BookStore**. На следующем изображении показан результат этого кода. Как видите, Book Catalog XML добавлен в узел BookStore, который является названием этого свойства.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Пример кода на C# для использования пользовательских XML-частей

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Связанная статья

- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/net/adding-custom-properties-visible-inside-document-information-panel/)

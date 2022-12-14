---
title: Используйте пользовательские части XML в Aspose.Cells
type: docs
weight: 390
url: /ru/net/use-custom-xml-parts-in-aspose-cells/
---
## Использование пользовательских частей XML в Aspose.Cells

Пользовательские XML-части — это XML-данные, которые хранятся различными приложениями, такими как SharePoint и т. д., внутри файла Excel. Эти данные потребляются различными приложениями, которым они нужны. Microsoft Excel не использует эти данные, поэтому графический интерфейс для их добавления отсутствует. Вы можете просмотреть эти данные, изменив расширение**.xlsx** в**.zip** а затем, открыв его с помощью**WinZip** . Вы также можете открыть ZIP-файл с помощью любой zip-утилиты третьей части Windows, такой как WinRAR или WinZip и т. д. Данные находятся внутри**customXml** папка.

 Вы можете добавить пользовательские части XML, используя Aspose.Cells через[**Рабочая книга.ContentTypeProperties.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)метод.

 В следующем примере кода используется[**Рабочая книга.ContentTypeProperties.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) метод и добавляет**XML-каталог книг** и его имя**Книжный магазин**. На следующем изображении показан результат этого кода. Как видите, XML каталога книг добавляется внутрь узла BookStore, который является именем этого свойства.

![дело:изображение_альтернативный_текст](use-custom-xml-parts-in-aspose-cells_1.png)

![дело:изображение_альтернативный_текст](use-custom-xml-parts-in-aspose-cells_2.png)

## C# код для использования пользовательских частей XML

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Связанная статья

- [Добавление настраиваемых свойств, видимых на панели сведений о документе](/cells/ru/net/adding-custom-properties-visible-inside-document-information-panel/)

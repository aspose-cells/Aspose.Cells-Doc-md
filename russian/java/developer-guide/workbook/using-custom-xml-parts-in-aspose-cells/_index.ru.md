---
title: Использование пользовательских частей XML в Aspose.Cells
type: docs
weight: 570
url: /ru/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Пользовательские XML-части — это XML-данные, которые хранятся различными приложениями, такими как SharePoint и т. д., внутри файла Excel. Эти данные потребляются различными приложениями, которым они нужны. Microsoft Excel не использует эти данные, поэтому графический интерфейс для их добавления отсутствует. Вы можете просмотреть эти данные, изменив расширение**.xlsx** в**.zip** а затем, открыв его с помощью**WinRAR** . Данные находятся внутри**customXml** папку, как показано на этом изображении.

![дело:изображение_альтернативный_текст](using-custom-xml-parts-in-aspose-cells_1.png)

 Вы можете добавить пользовательские части XML, используя Aspose.Cells через[Рабочая книга.getContentTypeProperties().добавить()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) метод.

{{% /alert %}} 
## **Использование пользовательских частей Xml в Aspose.Cells**
 В следующем примере кода используется[Рабочая книга.getContentTypeProperties().добавить()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) метод и добавляет**Каталог книг Xml** и его имя**Книжный магазин**На следующем изображении показан результат этого кода. Как видите, Xml каталога книг добавляется внутрь узла BookStore, который является именем этого свойства.

![дело:изображение_альтернативный_текст](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Связанная статья**
{{% alert color="primary" %}} 

- [Добавление настраиваемых свойств, видимых на панели сведений о документе](/cells/ru/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

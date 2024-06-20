---
title: Использование пользовательских XML частей в Aspose.Cells
type: docs
weight: 570
url: /ru/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Пользовательские XML-части - это XML-данные, которые хранятся различными приложениями, такими как SharePoint и др., внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому нет графического интерфейса для их добавления. Вы можете просмотреть эти данные, изменив расширение **.xlsx** на **.zip** и открыв их с помощью **WinRAR**. Данные находятся внутри папки **customXml**, как показано на этом изображении.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Вы можете добавить пользовательские XML-части с помощью Aspose.Cells через метод [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)).

{{% /alert %}} 
## **Использование пользовательских XML-частей в Aspose.Cells**
Приведенный ниже образец кода использует метод [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) и добавляет **Book Catalog Xml** с именем **BookStore**. На этом изображении показан результат этого кода. Как видно, Book Catalog Xml добавлен внутри узла BookStore, который является именем этого свойства.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Связанная статья**
{{% alert color="primary" %}} 

- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

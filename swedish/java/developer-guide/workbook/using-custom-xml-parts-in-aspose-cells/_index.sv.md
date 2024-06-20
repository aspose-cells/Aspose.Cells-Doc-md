---
title: Användning av anpassade XML delar i Aspose.Cells
type: docs
weight: 570
url: /sv/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Anpassade XML-delar är XML-data som lagras av olika program som SharePoint etc. inuti excel-filen. Denna data konsumeras av olika applikationer som behöver den. Microsoft Excel använder inte denna data så det finns ingen GUI att lägga till den. Du kan se denna data genom att ändra förlängningen av **.xlsx** till **.zip** och sedan genom att öppna den med **WinRAR**. Datan finns inne i mappen **customXml** som visas på bilden.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Du kan lägga till anpassade XML-delar med Aspose.Cells via metoden [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)).

{{% /alert %}} 
## **Använda anpassade Xml Delar i Aspose.Cells**
Följande provkod använder metoden [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) och lägger till **Book Catalog Xml** och dess namn är **BookStore**. Den följande bilden visar resultatet av denna kod. Som ni kan se har Book Catalog Xml lagts till inne i BookStore-noden som är namnet på egenskapen.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Relaterad artikel**
{{% alert color="primary" %}} 

- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

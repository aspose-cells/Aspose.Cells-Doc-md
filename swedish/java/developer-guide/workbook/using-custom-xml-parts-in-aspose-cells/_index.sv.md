---
title: Använda anpassade XML-delar i Aspose.Cells
type: docs
weight: 570
url: /sv/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint etc inuti excel-filen. Denna data konsumeras av olika applikationer som behöver den. Microsoft Excel använder inte denna data så det finns inget GUI att lägga till det. Du kan se denna data genom att ändra tillägget av**.xlsx** in i**.blixtlås** och sedan genom att öppna den med hjälp av**WinRAR** . Uppgifterna finns inuti**customXml** mapp som visas i denna bild.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

 Du kan lägga till anpassade XML-delar med Aspose.Cells via[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) metod.

{{% /alert %}} 
## **Använder anpassade XML-delar i Aspose.Cells**
 Följande exempelkod använder sig av[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) )-metoden och lägger till**Bokkatalog Xml** och dess namn är**Bokhandel**Följande bild visar resultatet av denna kod. Som du kan se läggs Book Catalog Xml till i BookStore-noden som är namnet på den här egenskapen.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Relaterad artikel**
{{% alert color="primary" %}} 

- [Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen](/cells/sv/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

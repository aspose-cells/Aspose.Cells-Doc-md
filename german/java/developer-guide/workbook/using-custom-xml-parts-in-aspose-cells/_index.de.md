---
title: Verwenden von benutzerdefinierten XML Teilen in Aspose.Cells
type: docs
weight: 570
url: /de/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Benutzerdefinierte XML-Teile sind die XML-Daten, die von verschiedenen Anwendungen wie SharePoint usw. in der Excel-Datei gespeichert werden. Diese Daten werden von verschiedenen Anwendungen verbraucht, die sie benötigen. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung von **.xlsx** in **.zip** ändern und sie dann mit **WinRAR** öffnen. Die Daten sind im **customXml**-Ordner vorhanden, wie in diesem Bild gezeigt.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Sie können benutzerdefinierte XML-Teile mittels der Methode [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) von Aspose.Cells hinzufügen.

{{% /alert %}} 
## **Verwenden von benutzerdefinierten XML-Teilen in Aspose.Cells**
Der folgende Beispielcode verwendet die Methode [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) und fügt das **Buchkatalog-XML** hinzu. Es wird als **Buchladen** benannt. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie man sehen kann, wird das Buchkatalog-XML innerhalb des Knotens Buchladen hinzugefügt, was der Name dieser Eigenschaft ist.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

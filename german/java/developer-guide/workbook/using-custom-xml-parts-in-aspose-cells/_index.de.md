---
title: Verwenden von benutzerdefinierten XML-Teilen in Aspose.Cells
type: docs
weight: 570
url: /de/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Benutzerdefinierte XML-Teile sind die XML-Daten, die von verschiedenen Anwendungen wie SharePoint usw. in der Excel-Datei gespeichert werden. Diese Daten werden von verschiedenen Anwendungen verbraucht, die sie benötigen. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI zum Hinzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung von ändern**.xlsx** hinein**.Postleitzahl** und dann durch Öffnen mit**WinRAR** . Die Daten sind in der vorhanden**benutzerdefiniertes XML** Ordner wie in diesem Bild gezeigt.

![todo: Bild_alt_Text](using-custom-xml-parts-in-aspose-cells_1.png)

 Sie können benutzerdefinierte XML-Teile mit Aspose.Cells über die hinzufügen[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) Methode.

{{% /alert %}} 
## **Verwenden von benutzerdefinierten XML-Teilen in Aspose.Cells**
 Der folgende Beispielcode verwendet[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) )-Methode und fügt die hinzu**Buchkatalog Xml** und sein Name ist**Buchhandlung**Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, wird Book Catalog Xml innerhalb des BookStore-Knotens hinzugefügt, der der Name dieser Eigenschaft ist.

![todo: Bild_alt_Text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Verwandter Artikel**
{{% alert color="primary" %}} 

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}

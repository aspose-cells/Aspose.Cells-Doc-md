---
title: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 500
url: /de/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells kann verwendet werden, um benutzerdefinierte Eigenschaften im Arbeitsmappenobjekt hinzuzufügen, die im Dokumentinformationsfeld sichtbar sind. Sie können das Dokumentinformationsfeld in Microsoft Excel über die Befehle Datei > Informationen > Eigenschaften > Dokumentinformationsfeld anzeigen öffnen.

Bitte verwenden Sie die Methode [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-), um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsfeld sichtbar ist.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielscode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ und die zweite Eigenschaft hat den Typ DateTime. Wenn Sie die durch diesen Code generierte Ausgabedatei in Excel öffnen, sehen Sie diese beiden Eigenschaften im Dokumentinformationsfeld.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwenden von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 300
url: /de/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind**

Aspose.Cells für Python via .NET kann verwendet werden, um benutzerdefinierte Eigenschaften im Arbeitsbuch-Objekt hinzuzufügen, die im Dokumentinformationen-Panel sichtbar sind. Das Dokumentinformationen-Panel kann in Microsoft Excel über Datei > Infos > Eigenschaften > Dokumenten-Panel anzeigen geöffnet werden.

Bitte verwenden Sie die Methode [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add), um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsfeld sichtbar sein wird.

Der folgende Beispielscode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ und die zweite Eigenschaft hat den Typ DateTime. Wenn Sie die durch diesen Code generierte Ausgabedatei in Excel öffnen, sehen Sie diese beiden Eigenschaften im Dokumentinformationsfeld.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

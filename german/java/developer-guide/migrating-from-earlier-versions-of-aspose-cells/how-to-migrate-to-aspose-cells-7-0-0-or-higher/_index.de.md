---
title: So migrieren Sie auf Aspose.Cells 7.0.0 oder höher
type: docs
weight: 10
url: /de/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

In diesem Artikel haben wir die bemerkenswerten Änderungen in API geteilt, die in Aspose.Cells for Java 7.0.0 und höheren Versionen im Vergleich zu den Vorgängerversionen von Aspose.Cells for Java enthalten waren. Dieser Artikel hilft den Benutzern, schnell von Old API zu New zu migrieren API, indem sie die vorgenommenen Änderungen verstehen und in ihren Anwendungen umsetzen.

{{% /alert %}}

## **Bemerkenswerte Änderungen für die bestehenden Benutzer**

Seit der Veröffentlichung von Aspose.Cells for Java v7.0.0 haben wir einige größere Änderungen an API vorgenommen und alle Funktionen hinzugefügt, die bis heute in Aspose.Cells for .NET vorhanden sind. Sowohl Aspose.Cells for Java als auch .NET sind jetzt in Bezug auf Funktionen und sogar in Bezug auf Methoden und Eigenschaftsnamen vergleichbar.

Ähnlich wie beim älteren Ansatz können Sie einfach nur eine Importanweisung in Ihre Anwendung importieren, um alle Klassen, Schnittstellen usw. abzurufen.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Wir haben bestimmte API-Sets umbenannt, um die API-Struktur zu bereinigen, damit sie mit Aspose.Cells for .NET übereinstimmen. Wir haben jetzt einige Sammlungsklassen hinzugefügt und sie durch vorhandene Sammlungsklassen ersetzt. Die Klasse Like Worksheets wurde durch ersetzt**Arbeitsblattsammlung** . Ebenso wurde die Shapes-Klasse durch ersetzt**ShapeCollection**. Die Funktionalität der Klassen wurde jedoch nicht beeinträchtigt, sondern erweitert.

Wenn Sie auf die neue API migrieren möchten, müssen Sie möglicherweise die folgenden Änderungen in Ihrer Anwendung vornehmen, damit die Dinge auf Ihrer Seite funktionieren. Die folgende Liste enthält auch die Änderungen, die in Klassen und ihren jeweiligen Methoden vorgenommen wurden.

## **Zusammenfassung der Änderungen in der API**

1) Sammlungen in v2.5.4 oder früher, deren Namen mit „s“ enden, werden umbenannt. In v7.0.0 oder höher werden die Sammlungen wie folgt benannt:
zB Shapes (Alt) -> ShapeCollection (Neu), Worksheets (Alt) -> WorksheetCollection (Neu), ... usw.

2) Das Abrufen des Elements aus der Sammlung wird geändert. Zum Beispiel haben wir es in v2.5.4 oder früher als getXXX(int) gemacht, in v7.0.0 oder höher machen wir es jetzt als get(int):
zB Worksheets.getSheet(int) (Alt) -> WorksheetCollection.get(int) (Neu), ...etc.

3) Das Abrufen der Größe (Elementanzahl) einer Sammlung wird geändert. In v2.5.4 oder früher haben wir es mit size() gemacht, in v7.0.0 oder höher machen wir es jetzt mit getCount():
Worksheets.size() (Alt) -> WorksheetCollection.getCount() (Neu), ... usw.

4) Getter-Methoden für boolesche Eigenschaften in v2.5.4 oder früher, deren Namen, die mit „is“ beginnen, geändert wurden. In v7.0.0 werden diese mit "get" gestartet:
zB PageSetup.isBlackAndWhite() (Alt) -> PageSetup.getBlackAndWhite() (Neu), ... usw.

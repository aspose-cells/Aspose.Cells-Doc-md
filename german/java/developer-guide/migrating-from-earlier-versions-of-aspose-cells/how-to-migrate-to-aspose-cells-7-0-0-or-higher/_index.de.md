---
title: Wie man zu Aspose.Cells 7.0.0 oder höher migriert
type: docs
weight: 10
url: /de/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

In diesem Artikel haben wir die bemerkenswerten Änderungen in der API geteilt, die in den Versionen ab 7.0.0 und weiter im Vergleich zu den Vorgängerversionen von Aspose.Cells for Java durchgeführt wurden. Dieser Artikel wird den Benutzern helfen, schnell von der alten API zur neuen API zu migrieren, indem sie die vorgenommenen Änderungen verstehen und in ihren Anwendungen umsetzen.

{{% /alert %}}

## **Bemerkenswerte Änderungen für die bestehenden Benutzer**

Seit der Veröffentlichung von Aspose.Cells for Java v7.0.0 haben wir einige wichtige Änderungen an der API vorgenommen und alle Funktionen hinzugefügt, die bis heute in Aspose.Cells for .NET vorhanden sind. Daher werden sowohl Aspose.Cells for Java als auch .NET jetzt in Bezug auf Funktionen und sogar in Bezug auf Methoden- und Eigenschaftsnamen vergleichbar sein.

Ähnlich wie bei dem früheren Ansatz können Sie in Ihrer Anwendung nur einen Importbefehl importieren, um alle Klassen, Schnittstellen usw. abzurufen.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Wir haben bestimmte API's umbenannt, um die Struktur der API zu bereinigen und mit Aspose.Cells for .NET abzugleichen. Wir haben jetzt einige Sammlungsklassen hinzugefügt und sie mit vorhandenen Sammlungsklassen ersetzt. Beispielsweise wurde die Klasse Worksheets jetzt durch **WorksheetCollection** ersetzt. Gleichzeitig wurde die Klasse Shapes durch **ShapeCollection** ersetzt. Die Funktionalität der Klassen wurde jedoch nicht beeinträchtigt, sondern verbessert.

Wenn Sie zur neuen API migrieren möchten, müssen Sie die folgenden Änderungen in Ihrer Anwendung vornehmen, um die Dinge auf Ihrer Seite zum Laufen zu bringen. Die folgende Liste enthält die Änderungen in Klassen und deren entsprechenden Methoden.

## **Zusammenfassung der Änderungen in der API**

1) Sammlungen in v2.5.4 oder früher, deren Namen mit 's' enden, werden umbenannt. In v7.0.0 oder höher sind die Sammlungen benannt als:
z. B. Shapes (Alt) -> ShapeCollection (Neu), Worksheets (Alt) -> WorksheetCollection (Neu), ..., usw.

2) Das Abrufen eines Elements aus der Sammlung wurde geändert. Zum Beispiel haben wir in v2.5.4 oder früher dies mit getXXX(int) gemacht, in v7.0.0 oder höher machen wir es jetzt mit get(int):
z. B. Worksheets.getSheet(int) (Alt) -> WorksheetCollection.get(int) (Neu), ...usw.

3) Das Abrufen der Größe (Elementanzahl) einer Sammlung wurde geändert. In v2.5.4 oder früher haben wir dies mit size() gemacht, in v7.0.0 oder höher machen wir es jetzt mit getCount():
Worksheets.size() (Alt) -> WorksheetCollection.getCount() (Neu), ...usw.

4) Die Getter-Methoden für boolesche Eigenschaften in v2.5.4 oder früher, deren Namen mit 'is' beginnen, wurden geändert. In v7.0.0 beginnen diese mit "get":
z. B. PageSetup.isBlackAndWhite() (Alt) -> PageSetup.getBlackAndWhite() (Neu), ...usw.
{{< app/cells/assistant language="java" >}}

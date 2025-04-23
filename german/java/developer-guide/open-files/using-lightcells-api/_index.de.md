---
title: Verwendung der LightCells API
type: docs
weight: 80
url: /de/java/using-lightcells-api/
---

{{% alert color="primary" %}}

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Liste von Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells-API ist nützlich, um riesige Excel-Tabellenkalkulationen zu erstellen: Damit benötigen Sie weniger Speicher und erzielen bessere Leistung und Effizienz.

{{% /alert %}}

## **Eventgesteuerte Architektur**

Aspose.Cells bietet die LightCells API, die hauptsächlich darauf ausgelegt ist, Zellendaten einzeln zu manipulieren, ohne ein vollständiges Datenmodell (Verwendung der Zellensammlung usw.) in den Speicher zu laden. Es funktioniert im ereignisgesteuerten Modus.

Um Arbeitsmappen zu speichern, geben Sie den Zellinhalt einzeln an, wenn Sie speichern, und das Komponente speichert ihn direkt in die Ausgabedatei.

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und gibt deren Wert einzeln an.

In beiden Verfahren wird ein Cell-Objekt verarbeitet und dann verworfen, das Workbook-Objekt hält die Sammlung nicht. In diesem Modus wird daher Speicher gespart, wenn Microsoft Excel-Dateien importiert und exportiert werden, die einen großen Datensatz haben, der ansonsten viel Speicher verwenden würde.

Obwohl die LightCells API die Zellen für XLSX- und XLS-Dateien auf dieselbe Weise verarbeitet (sie lädt nicht alle Zellen tatsächlich in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart sie für XLSX-Dateien effektiver Speicher als für XLS-Dateien aufgrund der unterschiedlichen Datenmodelle und Strukturen der beiden Formate.

Für XLS-Dateien können Entwickler jedoch spezifisch einen temporären Speicherort angeben, um während des Speichervorgangs generierte temporäre Daten zu speichern. **Die Verwendung der LightCells API zum Speichern von XLSX-Dateien kann in der Regel etwa 50 % oder mehr Speicher sparen** als die herkömmliche Methode, **das Speichern von XLS-Dateien kann etwa 20-40 % Speicher sparen**.

### **Schreiben großer Excel-Dateien**

Aspose.Cells bietet eine Schnittstelle, LightCellsDataProvider, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenspeicher für das Speichern großer Tabellendateien im leichten Modus dar.

Beim Speichern eines Arbeitsmappen im diesem Modus wird bei jedem Arbeitsblatt in der Arbeitsmappe startSheet(int) überprüft. Für ein Blatt, wenn startSheet(int) true ist, werden alle Daten und Eigenschaften von Zeilen und Zellen dieses Blatts, die gespeichert werden sollen, von dieser Implementierung bereitgestellt. Zuerst wird nextRow() aufgerufen, um den nächsten zu speichernden Zeilenindex zu erhalten. Wenn ein gültiger Zeilenindex zurückgegeben wird (der Zeilenindex muss in aufsteigender Reihenfolge für die zu speichernden Zeilen sein), wird ein Zeilenobjekt, das diese Zeile darstellt, von der Implementierung bereitgestellt, um seine Eigenschaften durch startRow(Row) zu setzen.

Für eine Zeile wird zuerst nextCell() überprüft. Wenn ein gültiger Spaltenindex (der Spaltenindex muss in aufsteigender Reihenfolge für alle Zellen einer Zeile sein) zurückgegeben wird, wird ein Zellenobjekt, das diese Zelle darstellt, bereitgestellt, um die Daten und Eigenschaften durch startCell(Cell) zu setzen. Nachdem die Daten dieser Zelle festgelegt sind, wird diese Zelle direkt in die generierte Tabellendatei gespeichert und die nächste Zelle wird überprüft und verarbeitet.

Das folgende Beispiel zeigt, wie die LightCells API funktioniert.

Das folgende Programm erstellt eine große Datei mit 100.000 Datensätzen in einem Arbeitsblatt, die mit Daten gefüllt sind. Wir haben einige Hyperlinks, Zeichenfolgenwerte, numerische Werte und auch Formeln zu bestimmten Zellen im Arbeitsblatt hinzugefügt. Darüber hinaus haben wir auch einen Bereich von Zellen formatiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lesen großer Excel-Dateien**

Aspose.Cells bietet eine Schnittstelle, LightCellsDataHandler, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenspeicher für das Lesen großer Tabellendateien im leichten Modus dar.

Beim Lesen eines Arbeitsmappen in diesem Modus wird bei jedem Arbeitsblatt in der Arbeitsmappe startSheet() überprüft. Für ein Blatt, wenn startSheet() true zurückgibt, werden alle Daten und Eigenschaften der Zellen in den Zeilen und Spalten des Blatts überprüft und verarbeitet. Für jede Zeile wird startRow() aufgerufen, um zu prüfen, ob sie verarbeitet werden muss. Wenn eine Zeile verarbeitet werden muss, werden zuerst die Eigenschaften der Zeile gelesen und Entwickler können auf ihre Eigenschaften mit processRow() zugreifen.

Wenn auch die Zellen der Zeile verarbeitet werden müssen, gibt processRow() true zurück und startCell() wird für jede vorhandene Zelle in der Zeile aufgerufen, um zu prüfen, ob sie verarbeitet werden muss. Wenn ja, wird processCell() aufgerufen.

Der folgende Beispielcode veranschaulicht diesen Prozess. Das Programm liest eine große Datei mit Millionen von Datensätzen ein. Es dauert etwas Zeit, um jedes Blatt in der Arbeitsmappe zu lesen. Der Beispielcode liest die Datei und ruft die Gesamtzahl der Zellen, Zeichenfolgen und Formeln für jedes Arbeitsblatt ab.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Eine Klasse, die die LightCellsDataHandler-Schnittstelle implementiert

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: Verwendung von LightCells API
type: docs
weight: 80
url: /de/java/using-lightcells-api/
---
{{% alert color="primary" %}}

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Liste von Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells API ist nützlich, um riesige Excel-Tabellen zu erstellen: Sie benötigen Speicherplatz und erhalten eine bessere Leistung und Effizienz.

{{% /alert %}}

## **Ereignisgesteuerte Architektur**

Aspose.Cells stellt die LightCells API bereit, die hauptsächlich dafür ausgelegt sind, Zelldaten einzeln zu manipulieren, ohne einen vollständigen Datenmodellblock (unter Verwendung der Cell-Sammlung usw.) im Speicher zu erstellen. Es arbeitet in einem ereignisgesteuerten Modus.

Um Arbeitsmappen zu speichern, geben Sie beim Speichern den Zelleninhalt Zelle für Zelle an, und die Komponente speichert ihn direkt in der Ausgabedatei.

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und stellt deren Wert nacheinander bereit.

In beiden Verfahren wird ein Cell-Objekt verarbeitet und dann verworfen, das Workbook-Objekt enthält die Sammlung nicht. In diesem Modus wird also beim Importieren und Exportieren von Microsoft Excel-Dateien mit einem großen Datensatz, der sonst viel Speicher verbrauchen würde, Speicherplatz gespart.

Obwohl LightCells API die Zellen für XLSX- und XLS-Dateien auf die gleiche Weise verarbeitet (es lädt nicht alle Zellen in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart es aufgrund von XLSX-Dateien effektiver Speicher als XLS-Dateien die unterschiedlichen Datenmodelle und Strukturen der beiden Formate.

 Jedoch,**für XLS Dateien** , um mehr Speicher zu sparen, können Entwickler einen temporären Speicherort zum Speichern temporärer Daten angeben, die während des Speichervorgangs generiert werden. Häufig,**Die Verwendung von LightCells API zum Speichern der Datei XLSX kann 50 % oder mehr Speicherplatz sparen** als den üblichen Weg zu gehen,**Durch das Speichern von XLS können etwa 20-40 % Speicher eingespart werden**.

### **Schreiben großer Excel-Dateien**

Aspose.Cells bietet eine Schnittstelle, LightCellsDataProvider, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt einen Datenanbieter zum Speichern großer Tabellenkalkulationsdateien im Lightweight-Modus dar.

Beim Speichern einer Arbeitsmappe in diesem Modus wird startSheet(int) überprüft, wenn jedes Arbeitsblatt in der Arbeitsmappe gespeichert wird. Wenn für ein Blatt startSheet(int) wahr ist, dann werden alle Daten und Eigenschaften von Zeilen und Zellen dieses zu speichernden Blatts von dieser Implementierung bereitgestellt. Zunächst wird nextRow() aufgerufen, um den nächsten zu speichernden Zeilenindex zu erhalten. Wenn ein gültiger Zeilenindex zurückgegeben wird (der Zeilenindex muss in aufsteigender Reihenfolge vorliegen, damit die Zeilen gespeichert werden können), wird ein Row-Objekt, das diese Zeile darstellt, für die Implementierung bereitgestellt, um seine Eigenschaften durch startRow(Row) festzulegen.

Für eine Zeile wird zuerst nextCell() geprüft. Wenn ein gültiger Spaltenindex zurückgegeben wird (der Spaltenindex muss in aufsteigender Reihenfolge sein, damit alle Zellen einer Zeile gespeichert werden), wird ein Cell-Objekt bereitgestellt, das diese Zelle darstellt, um die Daten und Eigenschaften von startCell(Cell) festzulegen. Nachdem die Daten dieser Zelle festgelegt wurden, wird diese Zelle direkt in der generierten Tabellendatei gespeichert und die nächste Zelle wird überprüft und verarbeitet.

Das folgende Beispiel zeigt, wie die LightCells API funktioniert.

Das folgende Programm erstellt eine riesige Datei mit 100.000 Datensätzen in einem Arbeitsblatt, gefüllt mit Daten. Wir haben einigen Zellen im Arbeitsblatt einige Hyperlinks, Zeichenfolgenwerte, numerische Werte und auch Formeln hinzugefügt. Darüber hinaus haben wir auch eine Reihe von Zellen formatiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Große Excel-Dateien lesen**

Aspose.Cells bieten eine Schnittstelle, LightCellsDataHandler, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenanbieter zum Lesen großer Tabellenkalkulationsdateien in einem leichtgewichtigen Modus dar.

Beim Lesen einer Arbeitsmappe in diesem Modus wird startSheet() überprüft, wenn jedes Arbeitsblatt in der Arbeitsmappe gelesen wird. Wenn für ein Blatt startSheet() true zurückgibt, werden alle Daten und Eigenschaften der Zellen in den Zeilen und Spalten des Blatts geprüft und verarbeitet. Für jede Zeile wird startRow() aufgerufen, um zu prüfen, ob sie verarbeitet werden muss. Wenn eine Zeile verarbeitet werden muss, werden die Eigenschaften der Zeile zuerst gelesen und Entwickler können mit processRow() auf ihre Eigenschaften zugreifen.

Wenn auch die Zellen der Zeile verarbeitet werden müssen, gibt processRow() true zurück und startCell() wird für jede vorhandene Zelle in der Zeile aufgerufen, um zu prüfen, ob sie verarbeitet werden muss. Wenn dies der Fall ist, wird processCell() aufgerufen.

Der folgende Beispielcode veranschaulicht diesen Vorgang. Das Programm liest eine große Datei mit Millionen von Datensätzen. Es braucht ein wenig Zeit, um jedes Blatt in der Arbeitsmappe zu lesen. Der Beispielcode liest die Datei und ruft die Gesamtzahl der Zellen, die Anzahl der Zeichenfolgen und die Anzahl der Formeln für jedes Arbeitsblatt ab.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Eine Klasse, die die LightCellsDataHandler-Schnittstelle implementiert

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}

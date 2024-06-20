---
title: Verwendung der LightCells API
type: docs
weight: 160
url: /de/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Menge an Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells API ist nützlich, um große Excel-Tabellenkalkulationen zu erstellen: Sie benötigen weniger Speicher und erhalten eine bessere Leistung und Effizienz.

{{% /alert %}} 
# Ereignisgesteuerte Architektur
Aspose.Cells bietet die LightCells API, die hauptsächlich darauf ausgelegt ist, Zellendaten einzeln zu manipulieren, ohne ein vollständiges Datenmodell (Verwendung der Zellensammlung usw.) in den Speicher zu laden. Es funktioniert im ereignisgesteuerten Modus.

Um Arbeitsmappen zu speichern, geben Sie den Zellinhalt einzeln an, wenn Sie speichern, und das Komponente speichert ihn direkt in die Ausgabedatei.

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und gibt deren Wert einzeln an.

In beiden Verfahren wird ein Cell-Objekt verarbeitet und dann verworfen, das Workbook-Objekt hält die Sammlung nicht. In diesem Modus wird daher Speicher gespart, wenn Microsoft Excel-Dateien importiert und exportiert werden, die einen großen Datensatz haben, der ansonsten viel Speicher verwenden würde.

Obwohl die LightCells API die Zellen für XLSX- und XLS-Dateien auf dieselbe Weise verarbeitet (sie lädt nicht alle Zellen tatsächlich in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart sie für XLSX-Dateien effektiver Speicher als für XLS-Dateien aufgrund der unterschiedlichen Datenmodelle und Strukturen der beiden Formate.

Für XLS-Dateien können Entwickler jedoch spezifisch einen temporären Speicherort angeben, um während des Speichervorgangs generierte temporäre Daten zu speichern. **Die Verwendung der LightCells API zum Speichern von XLSX-Dateien kann in der Regel etwa 50 % oder mehr Speicher sparen** als die herkömmliche Methode, **das Speichern von XLS-Dateien kann etwa 20-40 % Speicher sparen**.
## Schreiben einer großen Excel-Datei
Aspose.Cells bietet eine Schnittstelle, LightCellsDataProvider, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenaustauschanbieter für das Speichern großer Tabellendateien im Leichtgewichtsmodus dar.

Beim Speichern eines Arbeitsblatts in diesem Modus wird bei jedem Arbeitsblatt im Arbeitsbuch StartSheet(int) überprüft. Für ein Blatt, wenn StartSheet(int) true zurückgibt, werden alle Daten und Eigenschaften von Zeilen und Zellen dieses Blatts, die gespeichert werden sollen, von dieser Implementierung bereitgestellt. Zunächst wird NextRow() aufgerufen, um den nächsten Zeilenindex zu erhalten, der gespeichert werden soll. Wenn ein gültiger Zeilenindex zurückgegeben wird (der Zeilenindex muss in aufsteigender Reihenfolge für die zu speichernden Zeilen sein), wird ein Row-Objekt, das diese Zeile darstellt, bereitgestellt, um seine Eigenschaften durch StartRow(Row) festzulegen.

Für eine Zeile wird zuerst NextCell() überprüft. Wenn ein gültiger Spaltenindex zurückgegeben wird (der Spaltenindex muss in aufsteigender Reihenfolge für alle Zellen einer Zeile sein, die gespeichert werden sollen), wird ein Cell-Objekt, das diese Zelle darstellt, bereitgestellt, um ihre Daten und Eigenschaften durch StartCell(Cell) festzulegen. Nachdem die Daten der Zelle festgelegt sind, wird die Zelle direkt in der generierten Tabellendatei gespeichert und die nächste Zelle wird überprüft und verarbeitet.
### Schreiben einer großen Excel-Datei: Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.

Das Programm erstellt eine riesige Datei mit **10.000 (10000x30 Matrix) Datensätzen** in einem Arbeitsblatt und füllt sie mit Dummy-Daten. Sie können Ihre eigene Matrix angeben, indem Sie die Variablen rowsCount und colsCount in der Main()-Methode ändern.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Lesen großer Excel-Dateien
Aspose.Cells bietet eine Schnittstelle, LightCellsDataHandler, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenanbieter für das Lesen großer Tabellendateien im Leichtgewichtsmodus dar.

Beim Lesen eines Arbeitsblatts in diesem Modus wird bei jedem Arbeitsblatt im Arbeitsbuch StartSheet überprüft. Für ein Blatt, wenn StartSheet true zurückgibt, werden alle Daten und Eigenschaften der Zellen in Zeilen und Spalten des Blatts von der Implementierung dieser Schnittstelle überprüft und verarbeitet. Für jede Zeile wird StartRow aufgerufen, um zu überprüfen, ob diese verarbeitet werden muss. Wenn eine Zeile verarbeitet werden muss, werden zuerst ihre Eigenschaften gelesen und der Entwickler kann auf ihre Eigenschaften mit ProcessRow zugreifen. Wenn die Zellen der Zeile ebenfalls verarbeitet werden müssen, sollte ProcessRow true zurückgeben, und dann wird für jede vorhandene Zelle in der Zeile StartCell aufgerufen, um zu überprüfen, ob eine Zelle verarbeitet werden muss. Wenn eine Zelle verarbeitet werden muss, wird ProcessCell aufgerufen, um die Zelle durch die Implementierung dieser Schnittstelle zu verarbeiten.
### Lesen großer Excel-Dateien: Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.

Das Programm liest eine riesige Datei mit Millionen von Datensätzen in einem Arbeitsblatt. Es dauert etwas Zeit, um jede Tabelle im Arbeitsbuch zu lesen. Der Beispielcode liest die Datei und ruft die Gesamtanzahl der Zellen, die Zeichenfolgenanzahl und die Formelanzahl in jedem Arbeitsblatt ab.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}

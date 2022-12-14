---
title: Verwendung von LightCells API
type: docs
weight: 160
url: /de/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Liste von Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells API ist nützlich, um riesige Excel-Tabellen zu erstellen: Sie benötigen weniger Speicher und erhalten eine bessere Leistung und Effizienz.

{{% /alert %}} 
# Ereignisgesteuerte Architektur
Aspose.Cells stellt die LightCells API bereit, die hauptsächlich dafür ausgelegt sind, Zelldaten einzeln zu manipulieren, ohne einen vollständigen Datenmodellblock (unter Verwendung der Cell-Sammlung usw.) im Speicher zu erstellen. Es arbeitet in einem ereignisgesteuerten Modus.

Um Arbeitsmappen zu speichern, geben Sie beim Speichern den Zelleninhalt Zelle für Zelle an, und die Komponente speichert ihn direkt in der Ausgabedatei.

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und stellt deren Wert nacheinander bereit.

In beiden Verfahren wird ein Cell-Objekt verarbeitet und dann verworfen, das Workbook-Objekt enthält die Sammlung nicht. In diesem Modus wird also beim Importieren und Exportieren von Microsoft Excel-Dateien mit einem großen Datensatz, der sonst viel Speicher verbrauchen würde, Speicherplatz gespart.

Obwohl LightCells API die Zellen für XLSX- und XLS-Dateien auf die gleiche Weise verarbeitet (es lädt nicht alle Zellen in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart es aufgrund von für XLSX-Dateien effektiver Speicher als für XLS-Dateien die unterschiedlichen Datenmodelle und Strukturen der beiden Formate.

 Jedoch,**für XLS-Dateien** , um mehr Speicher zu sparen, können Entwickler einen temporären Speicherort zum Speichern temporärer Daten angeben, die während des Speichervorgangs generiert werden. Häufig,**Die Verwendung von LightCells API zum Speichern einer XLSX-Datei kann 50 % oder mehr Speicherplatz einsparen** als den üblichen Weg zu gehen,**Durch das Speichern von XLS können etwa 20-40 % Speicher eingespart werden**.
## Schreiben einer großen Excel-Datei
Aspose.Cells bieten eine Schnittstelle, LightCellsDataProvider, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt den Datenlieferanten dar, um große Tabellenkalkulationsdateien im Lightweight-Modus zu speichern.

Beim Speichern einer Arbeitsmappe in diesem Modus wird StartSheet(int) überprüft, wenn jedes Arbeitsblatt in der Arbeitsmappe gespeichert wird. Wenn für ein Blatt StartSheet(int) wahr ist, werden alle zu speichernden Daten und Eigenschaften von Zeilen und Zellen dieses Blatts von dieser Implementierung bereitgestellt. Zunächst wird NextRow() aufgerufen, um den nächsten zu speichernden Zeilenindex zu erhalten. Wenn ein gültiger Zeilenindex zurückgegeben wird (der Zeilenindex muss in aufsteigender Reihenfolge vorliegen, damit die Zeilen gespeichert werden können), wird ein Zeilenobjekt, das diese Zeile darstellt, für die Implementierung bereitgestellt, um seine Eigenschaften durch StartRow(Row) festzulegen.

Für eine Zeile wird zuerst NextCell() geprüft. Wenn ein gültiger Spaltenindex zurückgegeben wird (der Spaltenindex muss in aufsteigender Reihenfolge sein, damit alle Zellen einer Zeile gespeichert werden), wird ein Cell-Objekt, das diese Zelle darstellt, für die Implementierung bereitgestellt, um seine Daten und Eigenschaften durch StartCell(Cell) festzulegen. Nachdem die Daten der Zelle eingestellt sind, wird die Zelle direkt in der generierten Tabellenkalkulationsdatei gespeichert und die nächste Zelle wird geprüft und verarbeitet.
### Schreiben einer großen Excel-Datei:Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codesegmente nach Bedarf hinzu, entfernen oder aktualisieren Sie sie.

 Das Programm erstellt eine riesige Datei mit**10.000 (10.000 x 30 Matrix) Datensätze** in ein Arbeitsblatt und füllt sie mit Dummy-Daten. Sie können Ihre eigene Matrix angeben, indem Sie die Variablen rowsCount und colsCount in der Methode Main() ändern.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Große Excel-Dateien lesen
Aspose.Cells bietet eine Schnittstelle, LightCellsDataHandler, die in Ihrem Programm implementiert werden muss. Die Schnittstelle stellt einen Datenanbieter zum Lesen großer Tabellenkalkulationsdateien im Lightweight-Modus dar.

Beim Lesen einer Arbeitsmappe in diesem Modus wird StartSheet überprüft, wenn jedes Arbeitsblatt in der Arbeitsmappe gelesen wird. Wenn StartSheet für ein Blatt „true“ zurückgibt, werden alle Daten und Eigenschaften der Zellen in Zeilen und Spalten des Blatts von der Implementierung dieser Schnittstelle geprüft und verarbeitet. Für jede Zeile wird StartRow aufgerufen, um zu prüfen, ob sie verarbeitet werden muss. Wenn eine Zeile verarbeitet werden muss, werden ihre Eigenschaften zuerst gelesen und der Entwickler kann mit ProcessRow auf ihre Eigenschaften zugreifen. Wenn auch die Zellen der Zeile verarbeitet werden müssen, sollte ProcessRow true zurückgeben, und dann wird StartCell für jede vorhandene Zelle in der Zeile aufgerufen, um zu prüfen, ob eine Zelle verarbeitet werden muss. Wenn eine Zelle verarbeitet werden muss, wird ProcessCell aufgerufen, um die Zelle durch die Implementierung dieser Schnittstelle zu verarbeiten.
### Große Excel-Dateien lesen:Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codesegmente nach Bedarf hinzu, entfernen oder aktualisieren Sie sie.

Das Programm liest eine riesige Datei mit Millionen von Datensätzen in einem Arbeitsblatt. Es braucht ein wenig Zeit, um jedes Blatt in der Arbeitsmappe zu lesen. Der Beispielcode liest die Datei und ruft die Gesamtzahl der Zellen, die Zeichenfolgenanzahl und die Formelanzahl in jedem Arbeitsblatt ab.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}

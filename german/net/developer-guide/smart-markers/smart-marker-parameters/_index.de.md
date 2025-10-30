---
title: Smart Marker Parameter
type: docs
weight: 30
url: /de/net/smart-marker-parameters/
---

## **Designer-Tabelle & Intelligente Marker**
Designer-Tabellen sind Standard-Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Marker enthalten. Sie können intelligente Marker enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu relevanten Kontakten. Intelligente Marker werden in die Zellen geschrieben, in denen Sie die Informationen platzieren möchten.

Alle intelligenten Marker beginnen mit &=. Ein Beispiel für einen Datenmarker ist &=Party.FullName. Wenn der Datenmarker zu mehr als einem Element führt, beispielsweise einer vollständigen Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Somit können Zwischensummen und Summen in die Zeile unmittelbar nach dem Datenmarker platziert werden, um Berechnungen auf Basis der eingefügten Daten durchzuführen. Um Berechnungen auf den eingefügten Zeilen durchzuführen, verwenden Sie **dynamische Formeln**.

Intelligente Marker bestehen aus den Teilen **Datenquelle** und **Feldname** für die meisten Informationen. Spezielle Informationen können auch mit Variablen und Variablenarrays übergeben werden. Variablen füllen immer nur eine Zelle aus, während Variablenarrays mehrere Zellen ausfüllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete intelligente Marker werden entfernt.

Intelligente Marker können auch Parameter enthalten. Parameter ermöglichen es Ihnen, zu ändern, wie die Informationen dargestellt werden. Sie werden am Ende des intelligenten Markers in Klammern als durch Kommas getrennte Liste angehängt.

## **Intelligente Marker-Optionen**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Smart Marker Parameter**
Folgende Parameter sind erlaubt:

- **noadd** - Füge keine zusätzlichen Zeilen hinzu, um Daten anzupassen.
- **skip:n** - Überspringe n Zeilen für jede Datensatzzeile.
- **ascending:n** oder **descending:n** - Sortiere Daten in Smart-Markern. Wenn n 1 ist, ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach der Verarbeitung der Datenquelle sortiert. Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreibe Daten von links nach rechts anstatt von oben nach unten.
- **numeric** - Konvertiere Text in eine Zahl, wenn möglich.
- **shift** - Verschiebt nach unten oder rechts und erstellt zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert auf die gleiche Weise wie in Microsoft Excel. Zum Beispiel, wenn Sie in Microsoft Excel einen Bereich von Zellen auswählen, mit der rechten Maustaste darauf klicken und **Einfügen** auswählen und **Zellen nach unten verschieben** oder **Zellen nach rechts verschieben** oder andere Optionen angeben. Kurz gesagt, der **shift**-Parameter erfüllt die gleiche Funktion für vertikale/übliche (von oben nach unten) oder horizontale (von links nach rechts) intelligente Markierungen.
- **copystyle** - Kopiere den Zellstil der Basiszelle in alle Zellen dieser Spalte.

Die Parameter noadd und skip können kombiniert werden, um Daten in alternierende Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie noadd in der ersten Zeile hinzufügen, um zu verhindern, dass zusätzliche Zeilen vor der alternierenden Zeile eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie diese mit Kommas, aber ohne Leerzeichen: parameterA,parameterB,parameterC.

Die folgenden Screenshots zeigen, wie Daten in jeder zweiten Zeile eingefügt werden.

|**Vorlagendatei**|**Ausgabedatei**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **Dynamische Formeln**
Dynamische Formeln ermöglichen es Ihnen, Excel-Formeln in Zellen einzufügen, auch wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können für jede eingefügte Zeile wiederholt werden oder nur die Zelle verwenden, in der der Datenmarker platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r - Aktuelle Zeilennummer.
- 2, -1 - Versatz zur aktuellen Zeilennummer.

Zum Beispiel:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Im dynamischen Formelmarker steht "-1" für den Versatz zur aktuellen Zeile in den Spalten B und C, die für die Divisionsoperation festgelegt werden, der Überspringparameter beträgt eine Zeile. Darüber hinaus sollten wir das folgende Zeichen angeben:

{{< highlight java >}}

 "~"

{{< /highlight >}}

als Trennzeichen, um weitere Parameter in dynamischen Formeln anzuwenden.

Die folgenden Screenshots veranschaulichen eine wiederholende dynamische Formel und das resultierende Excel-Arbeitsblatt.

|**Vorlagendatei**|**Ausgabedatei**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Die Zelle "C1" enthält die Formel **= A1*B1**, die Zelle "C2" enthält **= A2*B2** und die Zelle "C3" enthält **= A3*B3**.

Es ist sehr einfach, die Smart Marker zu verarbeiten. Im folgenden Beispielcode wird gezeigt, wie dynamische Formeln in Smart Markers verwendet werden. Wir laden die [Template-Datei](templateDynamicFormulas.xlsx) und erstellen Testdaten, um die Marker zu verarbeiten, um Daten in die Zellen gegen den Marker einzufügen. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Wie man dynamische Formeln und Variablen in SmartMarkers verwendet**
Manchmal ist es notwendig, dynamische Formeln und Variablen in SmartMarkers zu verwenden. Für dynamische Formeln fügen Sie bitte das Sonderzeichen (~) als Trennzeichen hinzu. Aspose.Cells ermöglicht die Nutzung von dynamischen Formeln und Variablen in SmartMarkers. Bitte prüfen Sie [Vorlage](template.xlsx), [JSON-Datei](employees-data.json) und den Screenshot der generierten Excel-Ausgabe mit folgendem Code.

|**Das erste Arbeitsblatt der Vorlage.xlsx zeigt Variablen.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**Das zweite Arbeitsblatt der Vorlage.xlsx zeigt Smart Markers.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Die JSON-Daten sind wie folgt:
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}

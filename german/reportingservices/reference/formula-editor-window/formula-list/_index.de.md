---
title: Formelliste
type: docs
weight: 10
url: /de/reportingservices/formula-list/
---

**Berichtsfelder**

|**Set Name** |**Formelname**|**Beschreibung**|
| :- | :- | :- |
|Globale Felder |ExecutionTime |Das Datum und die Uhrzeit, zu denen der Bericht begonnen hat, ausgeführt zu werden. |
| |ReportServerUrl |Die URL des Berichtsservers, auf dem der Bericht ausgeführt wird. |
| |ReportName |Der Name des Berichts, wie er in der Datenbank des Berichtsservers gespeichert ist. |
| |ReportFolder |Der vollständige Pfad zum Ordner, der den Bericht enthält. Dies beinhaltet nicht die URL des Berichtsservers. |
|Benutzer |UserID |Die ID des Benutzers, der den Bericht ausführt. |
| |Sprache |Die Sprach-ID des Benutzers, der den Bericht ausführt. |
**Berichtsfelder**

|**Set Name**|**Beschreibung**|
| :- | :- |
|Parameters |Die Parametersammlung enthält die Berichtsparameter innerhalb des Berichts. Parameter können an Abfragen übergeben, in Filtern verwendet oder in anderen Funktionen verwendet werden, die das Berichtsaussehen basierend auf dem Parameter ändern. |
|Felder |Die Feldsammlung enthält die Felder im aktuellen Datensatz. |
|Datensatz ||
**Operatoren**
Arithmetische Operatoren werden verwendet, um Zahlen, numerische Variablen, numerische Felder und numerische Funktionen zu kombinieren, um eine andere Zahl zu erhalten. Vergleichsoperatoren werden normalerweise verwendet, um Operanden für eine Bedingung in einer Steuerstruktur wie einer If-Anweisung zu vergleichen. Boolesche Operatoren werden typischerweise mit Vergleichsoperatoren verwendet, um Bedingungen für Steuerstrukturen zu generieren.

|**Set Name**|**Formelname**|**Beschreibung**|
| :- | :- | :- |
|Arithmetik |^ |Potenzierung, zum Beispiel 2^3. |
| |* |Multiplikation, zum Beispiel 2*3. |
| |/ |Division, zum Beispiel 2/3. |
| |\\\ |Ganzzahlige Division, zum Beispiel 2\\\3. |
| |Mod |Modulo, zum Beispiel 4 Mod 3. |
| |+ |Addition, zum Beispiel 4 + 3. |
| |- |Subtraktion, zum Beispiel 4 - 3. |
|Vergleich |< |Kleiner als, zum Beispiel 4 < 3 falsch. |
| |<= |Kleiner als oder gleich, zum Beispiel 4 <= 3 falsch. |
| |> |Größer als, zum Beispiel 4 > 3 wahr. |
| |>= |Größer als oder gleich, zum Beispiel 4 >= 3 wahr. |
| |= |Gleich, zum Beispiel 4 = 3 falsch. |
| |<> |Ungleich, zum Beispiel 4 <> 3 wahr. |
| |Wie |Vergleicht einen String mit einem Muster. Zum Beispiel resultat = string Wie muster. |
| |Ist |Vergleicht zwei Objektreferenzvariablen, zum Beispiel asp Ist aspose. |
|Verkettung |& |Erzeugt eine Zeichenkettenverkettung von zwei Ausdrücken. |
| |+ |Addiert zwei Zahlen oder gibt den positiven Wert eines numerischen Ausdrucks zurück. Kann auch verwendet werden, um zwei Zeichenkettenausdrücke zu verkettet. |
|Logisch/Bitweise |Und |Führt eine logische Konjunktion auf zwei booleschen Ausdrücken oder eine bitweise Konjunktion auf zwei numerischen Ausdrücken durch. |
| |Nicht |Führt eine logische Negation auf einen booleschen Ausdruck oder eine bitweise Negation auf einen numerischen Ausdruck durch. |
| |Oder |Führt eine logische Disjunktion auf zwei booleschen Ausdrücken oder eine bitweise Disjunktion auf zwei numerischen Ausdrücken durch. |
| |Xor |Führt eine logische Ausschluss auf zwei booleschen Ausdrücken oder eine bitweise Ausschluss auf zwei numerischen Ausdrücken durch. |
| |UndAuch |Führt eine Kurzschlusslogik auf zwei Ausdrücken durch. |
| |OderAuch |Führt eine Kurzschluss inkulsive logische Disjunktion auf zwei Ausdrücken durch. |
|Bitverschiebung |>> |Führt eine arithmetische Linksverschiebung auf ein Bitmuster durch. |
| |<< |Führt eine arithmetische Rechtsverschiebung auf ein Bitmuster durch. |


---
title: Formelliste
type: docs
weight: 10
url: /de/reportingservices/formula-list/
---
**Berichtsfelder**

|**Name einsetzen** |**Formelname**|**Beschreibung**|
|:- |:- |:- |
| Globale Felder| Ausführungszeit|Datum und Uhrzeit des Beginns der Berichtsausführung.|
|| ReportServerUrl| Die URL des Berichtsservers, auf dem der Bericht ausgeführt wird.|
|| Berichtsname| Der Name des Berichts, wie er in der Berichtsserver-Datenbank gespeichert ist.|
|| Berichtsordner| Der vollständige Pfad zu dem Ordner, der den Bericht enthält. Dies beinhaltet nicht die Berichtsserver-URL.|
| Benutzer| Benutzeridentifikation| Die ID des Benutzers, der den Bericht ausführt.|
|| Sprache| Die Sprach-ID des Benutzers, der den Bericht ausführt.|
**Berichtsfelder**

|**Name einsetzen**|**Beschreibung**|
|:- |:- |
| Parameter| Die Parameters-Auflistung enthält die Berichtsparameter innerhalb des Berichts. Parameter können an Abfragen übergeben, in Filtern oder in anderen Funktionen verwendet werden, die das Erscheinungsbild des Berichts basierend auf dem Parameter ändern.|
| Felder| Die Fields-Auflistung enthält die Felder im aktuellen Dataset.|
| Datensatz||
**Betreiber**
Arithmetische Operatoren werden verwendet, um Zahlen, numerische Variablen, numerische Felder und numerische Funktionen zu kombinieren, um eine andere Zahl zu erhalten. Vergleichsoperatoren werden normalerweise verwendet, um Operanden für eine Bedingung in einer Kontrollstruktur wie einer If-Anweisung zu vergleichen. Boolesche Operatoren werden typischerweise mit Vergleichsoperatoren verwendet, um Bedingungen für Kontrollstrukturen zu generieren.

|**Name einsetzen**|**Formelname**|**Beschreibung**|
|:- |:- |:- |
| Arithmetik|^ | Potenzierung, zum Beispiel 2^3.|
||* | Multiplikation, zum Beispiel 2*3.|
||/ | Division, zum Beispiel 2/3.|
||\\\ | Ganzzahlige Division, zum Beispiel 2\\\3.|
|| Mod| Modul, zum Beispiel 4 Mod 3.|
||+ | Addition, zum Beispiel 4 + 3.|
||- | Subtraktion, zum Beispiel 4 – 3.|
| Vergleich|< | Weniger als zum Beispiel 4< 3 false. |
||<= | Kleiner oder gleich, zum Beispiel 4<= 3 false. |
||> | Größer als zum Beispiel 4 > 3 wahr.|
||>= | Größer oder gleich, zum Beispiel 4 >= 3 wahr.|
||= | Gleich, zum Beispiel 4 = 3 falsch.|
||<> | Ungleich, zum Beispiel 4<> 3 wahr.|
|| Wie|Vergleicht eine Zeichenfolge mit einem Muster. Zum Beispiel result = string Wie Muster.|
|| Ist| Vergleicht zwei Objektreferenzvariablen, zum Beispiel asp Is aspose.|
| Verkettung|& | Erzeugt eine Zeichenfolgenverkettung von zwei Ausdrücken.|
||+ | Addiert zwei Zahlen oder gibt den positiven Wert eines numerischen Ausdrucks zurück. Kann auch verwendet werden, um zwei Zeichenfolgenausdrücke zu verketten.|
| Logisch/bitweise| Und| Führt eine logische Konjunktion für zwei boolesche Ausdrücke oder eine bitweise Konjunktion für zwei numerische Ausdrücke aus.|
|| Nicht| Führt eine logische Negation für einen booleschen Ausdruck oder eine bitweise Negation für einen numerischen Ausdruck durch.|
|| Oder| Führt eine logische Trennung von zwei booleschen Ausdrücken oder eine bitweise Trennung von zwei numerischen Ausdrücken durch.|
|| Xor| Führt einen logischen Ausschluss für zwei boolesche Ausdrücke oder einen bitweisen Ausschluss für zwei numerische Ausdrücke durch.|
|| Und auch| Führt eine kurzschließende logische Konjunktion an zwei Ausdrücken aus.|
|| Sonst|Führt einen Kurzschluss inklusive logischer Disjunktion an zwei Ausdrücken durch.|
| Bitverschiebung|>> | Führt eine arithmetische Linksverschiebung an einem Bitmuster durch.|
||<< | Führt eine arithmetische Rechtsverschiebung an einem Bitmuster durch.|


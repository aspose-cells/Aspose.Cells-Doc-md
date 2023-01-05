---
title: Parametrisierter Bericht
type: docs
weight: 60
url: /de/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 EIN*parametrisierter Bericht* ist ein Bericht, der Eingabewerte akzeptiert, die bei der Verarbeitung des Berichts verwendet werden.

 Mit einem parametrisierten Bericht können Sie die Ausgabe eines Berichts basierend auf den zur Laufzeit festgelegten Werten variieren. Reporting Services unterstützt zwei Arten von Parametern: Abfrageparameter und Berichtsparameter.

- **Parameter abfragen** werden verwendet, um Daten während der Datenverarbeitung auszuwählen oder zu filtern. Wenn ein Abfrageparameter angegeben ist, muss ein Wert entweder vom Benutzer oder von Standardeigenschaften bereitgestellt werden, um die SELECT-Anweisung oder gespeicherte Prozedur abzuschließen, die Daten für einen Bericht abruft.
- **Berichtsparameter**werden während der Berichtsverarbeitung verwendet, um einen anderen Aspekt der Daten anzuzeigen. Ein Berichtsparameter wird normalerweise verwendet, um eine große Menge an Datensätzen zu filtern, aber er kann abhängig von den Abfragen und Ausdrücken im Bericht auch andere Verwendungszwecke haben.

 Berichtsparameter unterscheiden sich von Abfrageparametern dadurch, dass sie in einem Bericht definiert und vom Berichtsserver verarbeitet werden, während Abfrageparameter als Teil der Datensatzabfrage definiert und auf dem Datenbankserver verarbeitet werden. In Aspose.Cells.Report.Designer werden Abfrageparameter zum Zeitpunkt der Abfrageerstellung in Microsoft Abfrage angegeben.

Sie können Berichtsparameter erstellen und Abfrageparameter den entsprechenden Berichtsparametern in Aspose.Cells.Report.Designer zuordnen. Auf diese Weise ist es möglich, Werte für Berichtsparameter auszuwählen und sie in der Abfrage zu übergeben, um die aus der Datenquelle abgerufenen Daten einzuschränken.

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:**
- [Erstellen von Berichtsparametern](/cells/de/reportingservices/creating-report-parameters/)
- [Ändern von Berichtsparametern](/cells/de/reportingservices/modifying-report-parameters/)
- [Zuordnung von Abfrageparametern zu Berichtsparametern](/cells/de/reportingservices/mapping-query-parameters-to-report-parameters/)

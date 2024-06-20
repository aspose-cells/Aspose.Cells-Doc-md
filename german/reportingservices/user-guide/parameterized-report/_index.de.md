---
title: Parametrisierter Bericht
type: docs
weight: 60
url: /de/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Ein *parametrisierter Bericht* ist ein Bericht, der Eingabewerte akzeptiert, die verwendet werden, wenn der Bericht verarbeitet wird. 

Bei einem parametrisierten Bericht können Sie die Ausgabe eines Berichts basierend auf den Werten variieren, die zur Laufzeit festgelegt sind. Reporting Services unterstützt zwei Arten von Parametern: Abfrageparameter und Berichtsparameter. 

- **Abfrageparameter** werden verwendet, um Daten während der Datenverarbeitung auszuwählen oder zu filtern. Wenn ein Abfrageparameter angegeben ist, muss entweder vom Benutzer oder von den Standardwerten ein Wert bereitgestellt werden, um die SELECT-Anweisung oder gespeicherte Prozedur abzuschließen, die Daten für einen Bericht abruft.
- **Berichtsparameter** werden während der Berichtsverarbeitung verwendet, um einen anderen Aspekt der Daten darzustellen. Ein Berichtsparameter wird normalerweise verwendet, um eine große Menge von Datensätzen zu filtern, kann aber je nach Abfragen und Ausdrücken im Bericht auch andere Verwendungen haben.

Berichtsparameter unterscheiden sich von Abfrageparametern darin, dass sie in einem Bericht definiert und vom Berichtsserver verarbeitet werden, während Abfrageparameter als Teil der DataSet-Abfrage definiert und auf dem Datenbankserver verarbeitet werden. In Aspose.Cells.Report.Designer werden Abfrageparameter zum Zeitpunkt der Abfrageerstellung in Microsoft Query festgelegt. 

Sie können Berichtsparameter erstellen und Abfrageparameter auf den entsprechenden Berichtsparameter in Aspose.Cells.Report.Designer abbilden. Auf diese Weise ist es möglich, Werte für Berichtsparameter auszuwählen und sie in der Abfrage weiterzugeben, um die aus der Datenquelle abgerufenen Daten zu begrenzen.

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:** 
- [Erstellen von Berichtsparametern](/cells/de/reportingservices/creating-report-parameters/)
- [Ändern von Berichtsparametern](/cells/de/reportingservices/modifying-report-parameters/)
- [Abbildung von Abfrageparametern auf Berichtsparameter](/cells/de/reportingservices/mapping-query-parameters-to-report-parameters/)

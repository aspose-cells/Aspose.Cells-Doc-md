---
title: Tabellenbericht erstellen
type: docs
weight: 70
url: /de/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Eine Tabelle in einer Aspose.Cells-Berichtsvorlage besteht aus einer Kopfzeile, Tabellendatenzeilen, Zeilengruppen und Fußzeilen. Eine Beispieltabelle ist unten gezeigt.

**Eine Beispieltabelle** 

![todo: Bild_alt_Text](creating-tabular-report_1.png)
#### **Tabellenkopf**
Der Tabellenkopf enthält normalerweise den Titel für jede Tabellenspalte und andere Textelemente wie statischen Text, Berichtsparameter, globale Berichtsvariablen und so weiter. Der Tabellenkopf ist optional. Wenn Sie eine Kopfzeile verwenden, sollte das Kopfzeilen-Tag links von der ersten Spalte der Tabellendaten platziert werden, um anzuzeigen, dass es sich bei der Zeile um eine Kopfzeile handelt.
#### **Tabellendatenzeile**
Eine Tabellendatenzeile ist eine Zeile von Zellen, die intelligente Markierungen enthalten. Eine Tabelle kann nur eine einzige Datenzeile enthalten.
#### **Zeilengruppe**
Die Zeilengruppe folgt dicht auf die Tabellendatenzeile und besteht aus zwei Teilen: Gruppen-Tag und Gruppendatenzeile.

Das Gruppen-Tag sollte links von der ersten Tabellendatenspalte platziert werden, um anzugeben, dass die Zeile die Datenzeile der Zeilengruppe ist. Das Format des Gruppen-Tags ist ##group{GroupColumn}, zum Beispiel ##group{SalesOrderNumber}, wobei SalesOrderNumber einer der Spaltennamen des Datensatzes ist. Eine Tabelle kann nur eine Zeilengruppe enthalten, aber eine Zeilengruppe kann mehr als eine Gruppendatenzeile enthalten. Das Gruppen-Tag darf nur in der ersten Datenzeile platziert werden, wie im Beispiel oben gezeigt.

Das Gruppen-Tag wird zum Zeitpunkt des Renderns aus der Excel-Ausgabedatei Microsoft entfernt. Zeilengruppen sind optional.
#### **Fußzeilen**
 Fußzeilen kommen nach der Zeilengruppe und bestehen aus drei Teilen: Fußzeilen-Tag, Fußzeilen-Datenzeile und Fußzeilen-Textbereich.

Das Fußzeilen-Tag sollte links von der ersten Spalte der Tabellendatenspalte platziert werden, die angibt, dass die Zeile die Fußzeile der Tabelle ist. Eine Tabelle kann mehr als eine Fußzeile enthalten und jede Fußzeile muss durch ein Fußzeilen-Tag gekennzeichnet sein.

Der Fußzeilentextbereich kann statischen Text, Berichtsparameter und globale Berichtsvariablen enthalten, wie im Beispiel oben gezeigt.

Das Fußzeilen-Tag wird zum Zeitpunkt des Renderns aus der Excel-Ausgabedatei Microsoft entfernt. Fußzeilen sind optional.

Die Ausgabe der Beispielvorlage ist unten dargestellt.

**Mustervorlage** 

![todo: Bild_alt_Text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:**
- [Vorbereitung zum Erstellen eines Tabellenberichts](/cells/de/reportingservices/preparing-for-creating-table-report/)
- [Hinzufügen von Basisinformationen für die Tabelle](/cells/de/reportingservices/adding-base-information-for-table/)
- [Hinzufügen von Reporting Services-Formeln](/cells/de/reportingservices/adding-reporting-services-formulas/)
- [Tabellengruppe hinzufügen](/cells/de/reportingservices/adding-table-group/)
- [Tabellenfußzeilen hinzufügen](/cells/de/reportingservices/adding-table-footers/)
- [Hinzufügen von Berichtsparametern zum Bericht](/cells/de/reportingservices/adding-report-parameters-to-report/)
- [Hinzufügen globaler Reporting Services-Variablen zum Bericht](/cells/de/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Berichtsattribute festlegen](/cells/de/reportingservices/setting-report-attributes/)
- [Ändern von Berichtsattributen](/cells/de/reportingservices/modifying-report-attributes/)

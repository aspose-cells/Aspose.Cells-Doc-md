---
title: Tabellarischen Bericht erstellen
type: docs
weight: 70
url: /de/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

In einem Aspose.Cells-Berichtsvorlage besteht eine Tabelle aus einem Header, Tabellendatenzeilen, Zeilengruppen und Fußzeilen. Eine Beispieltabelle wird unten angezeigt.

**Ein Beispiel für eine Tabelle** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Tabellenheader**
Der Tabellenheader enthält normalerweise den Titel für jede Tabellenspalte und andere Textelemente wie statischen Text, Berichtsparameter, globale Berichtsvariablen usw. Der Tabellenheader ist optional. Wenn ein Header verwendet wird, sollte das Header-Tag links von der ersten Tabellenspalte platziert werden, um anzuzeigen, dass die Zeile ein Header ist.
#### **Tabellendatenzeile**
Eine Tabellendatenzeile ist eine Zeile von Zellen, die Smart-Marker enthalten. Eine Tabelle kann nur eine einzige Datenzeile enthalten.
#### **Zeilengruppe**
Die Zeilengruppe folgt unmittelbar nach der Tabellendatenzeile und besteht aus zwei Teilen: Gruppen-Tag und Gruppendatenzeile. 

Der Gruppen-Tag sollte links von der ersten Tabellendatenzeile platziert werden, um anzuzeigen, dass die Zeile die Datenzeile der Zeilengruppe ist. Das Format des Gruppen-Tags lautet ##group{GruppenSpalte}, beispielsweise ##group{SalesOrderNumber}, wobei SalesOrderNumber einer der Spaltennamen des Datensatzes ist. Eine Tabelle kann nur eine Zeilengruppe enthalten, aber eine Zeilengruppe kann mehr als eine Gruppendatenzeile enthalten. Der Gruppen-Tag darf nur in der ersten Datenzeile platziert werden, wie im obigen Beispiel gezeigt.

Der Gruppen-Tag wird zur Renderzeit aus der Ausgabedatei von Microsoft Excel entfernt. Zeilengruppen sind optional.
#### **Fußzeilen**
Fußzeilen folgen nach der Zeilengruppe und bestehen aus drei Teilen: Fußzeichen, Fußdatenzeile und Fußtextbereich. 

Das Fußzeichen sollte links von der ersten Spalte der Tabellendatenzeile platziert werden, um anzuzeigen, dass die Zeile die Tabellenfußzeile ist. Eine Tabelle kann mehrere Fußdatenzeilen enthalten, und jede Fußzeile muss mit einem Fußzeichen markiert sein. 

Der Fußtextbereich kann statischen Text, Berichtsparameter und globale Berichtsvariablen enthalten, wie im obigen Beispiel gezeigt.

Das Fußzeichen wird zur Renderzeit aus der Ausgabedatei von Microsoft Excel entfernt. Fußzeilen sind optional.

Die Ausgabe der Beispielvorlage wird unten angezeigt.

**Beispielvorlage** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:** 
- [Vorbereitung zur Erstellung eines Tabellenberichts](/cells/de/reportingservices/preparing-for-creating-table-report/)
- [Hinzufügen von Basisinformationen für Tabelle](/cells/de/reportingservices/adding-base-information-for-table/)
- [Hinzufügen von Reporting Services-Formeln](/cells/de/reportingservices/adding-reporting-services-formulas/)
- [Hinzufügen von Tabellengruppe](/cells/de/reportingservices/adding-table-group/)
- [Hinzufügen von Tabellenfußzeilen](/cells/de/reportingservices/adding-table-footers/)
- [Hinzufügen von Berichtsparametern zum Bericht](/cells/de/reportingservices/adding-report-parameters-to-report/)
- [Hinzufügen von Reporting Services-Globalvariablen zum Bericht](/cells/de/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Festlegen von Berichtsattributen](/cells/de/reportingservices/setting-report-attributes/)
- [Ändern von Berichtsattributen](/cells/de/reportingservices/modifying-report-attributes/)

---
title: Vorwort
type: docs
weight: 20
url: /de/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells für Reporting Services enthält hauptsächlich zwei Komponenten: Aspose.Cells.Report.Designer und Aspose.Cells.Renderer für Reporting Services. Ersteres wird verwendet, um Berichte direkt in Microsoft Excel zu entwerfen, und letzteres ist für das Rendern eines RDL-Berichts in Microsoft Excel verantwortlich.

{{% /alert %}} 
### **Entwerfen eines Berichts mit dem Berichtsdesigner**
Die wichtigsten Schritte zum Entwerfen eines Berichts mit Aspose.Cells.Report.Designer sind:

1. **Erstellen Sie Datenquellen und Abfragen**.
 Microsoft Query ist in Aspose.Cells.Report.Designer integriert und wird als grafisches Tool zum Erstellen von Datenquellen und Abfragen verwendet. Benutzer können auch auf eine vorhandene RDL-Datei zurückgreifen, in der Datenquellen und Abfragen für Operationen verfügbar sind.
1. **Kartenparameter**.
 Wenn die SQL-Anweisungen einer Abfrage Parameter enthalten, müssen Benutzer Berichtsparameter erstellen und SQL-Parameter den Berichtsparametern zuordnen. Sie können gültige Werte für einen Berichtsparameter in Aspose.Cells.Report.Designer festlegen.
1. **Design Microsoft Inhalte, Stile und Formate von Excel-Berichtsvorlagen**.
Eine Aspose.Cells-Berichtsvorlage kann eine beliebige Anzahl der folgenden Arten von Berichtselementen enthalten:
 1. Tabelle
 1. Pivot-Tabelle
 1. Diagramm
 1. Textfeld
 1. Matrix
 Normalerweise wird eine Abfrage (d. h. DataSet) als Datenquelle für Berichtselemente verwendet. Sie können auch Reporting Services-Parameter, Formeln und globale Variablen als Datenquelle für einige Arten von Berichtselementen verwenden. Die Stile und Formate von Berichtselementen werden einfach durch Festlegen der Stile und Formate der Zellen angegeben, aus denen die Berichtselemente bestehen.
1. **Bericht veröffentlichen**.
 Nach den obigen Schritten kann der Bericht veröffentlicht werden. Benutzer können festlegen, in welchem Ordner der Bericht veröffentlicht wird. Bei Bedarf können Sie eine freigegebene Datenquelle auf dem Berichtsserver als Datenquelle für den Bericht zuweisen.
1. **Vorschaubericht**.
Wenn Sie einen Bericht für die Vorschau auf dem Berichtsserver auswählen, werden Sie aufgefordert, anzugeben, in welches Dateiformat er exportiert werden soll (z. B. Microsoft Excel 97-2003 binäres XLS-Format, SpreadsheetML oder Microsoft Excel 2007 XLSX-Format) und alle erstellten Eingabeberichtsparameter anzugeben während der Berichtsgestaltung. Danach wird der Bericht mit Daten gefüllt, die von Reporting Services bereitgestellt werden.

---
title: Vorwort
type: docs
weight: 20
url: /de/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services enthält hauptsächlich zwei Komponenten: Aspose.Cells.Report.Designer und Aspose.Cells.Renderer für Reporting Services. Ersteres wird verwendet, um Berichte direkt in Microsoft Excel zu entwerfen, und letzteres ist für das Rendern eines RDL-Berichts in Microsoft Excel verantwortlich. 

{{% /alert %}} 
### **Entwerfen eines Berichts mit dem Berichtsdesigner**
Die Haupt-Schritte zum Entwerfen eines Berichts mit Aspose.Cells.Report.Designer sind:

1. **Datenquellen und Abfragen erstellen**.
   Microsoft Query ist in Aspose.Cells.Report.Designer integriert und wird als grafisches Werkzeug zum Erstellen von Datenquellen und Abfragen verwendet. Benutzer können auch eine vorhandene RDL-Datei verwenden, in der Datenquellen und Abfragen für Operationen verfügbar sind.
1. **Parameter abbilden**.
   Wenn die SQL-Anweisungen einer Abfrage Parameter enthalten, müssen Benutzer Berichtsparameter erstellen und SQL-Parameter auf Berichtsparameter abbilden. Sie können gültige Werte für einen Berichtsparameter in Aspose.Cells.Report.Designer festlegen.
1. **Inhalte, Stile und Formate des Microsoft Excel-Berichtsvorlagenentwurfs gestalten**.
   Eine Aspose.Cells-Berichtsvorlage kann beliebig viele der folgenden Arten von Berichtselementen enthalten: 
   1. Tabelle
   1. Pivot-Tabelle
   1. Diagramm
   1. Textfeld
   1. Matrix
      Normalerweise wird eine Abfrage (d. h. DataSet) als Datenquelle für das Berichtselement verwendet. Sie können auch Reporting Services-Parameter, Formeln und globale Variablen als Datenquelle für einige Arten von Berichtselementen verwenden. Die Styles und Formate der Berichtselemente werden einfach durch Festlegen der Styles und Formate der Zellen festgelegt, die die Berichtselemente zusammensetzen.
1. **Bericht veröffentlichen**.
   Nach den obigen Schritten ist der Bericht bereit, veröffentlicht zu werden. Benutzer können angeben, in welchen Ordner der Bericht veröffentlicht werden soll. Bei Bedarf können Sie einen freigegebenen Datenquell auf dem Berichtsserver als Datenquelle für den Bericht zuweisen.
1. **Berichtsvorschau**.
   Wenn Sie einen Bericht zur Vorschau auf dem Berichtsserver auswählen, werden Sie aufgefordert, das Exportformat anzugeben (z. B. Microsoft Excel 97-2003 binäres XLS-Format, SpreadsheetML oder Microsoft Excel 2007 XLSX-Format) und alle erstellten Eingabeparameter des Berichtsdesigns. Danach wird der Bericht mit von Reporting Services bereitgestellten Daten befüllt.

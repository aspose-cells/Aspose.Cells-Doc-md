---
title: Umbraco Datenbankdatenexporteur nach Excel
type: docs
weight: 20
url: /de/net/umbraco-database-data-exporter-to-excel/
---

## **Einführung**
Aspose .NET-Datenbankdatenexporteur nach Excel für das Umbraco-Modul ermöglicht es Benutzern, Daten direkt aus lokalen oder entfernten Datenbanktabellen, Ansichten und durch benutzerdefinierte Abfragen in Microsoft Excel oder OpenOffice Spreadsheet zu exportieren. Dieses Modul demonstriert die leistungsfähige Tabellenkalkulationserstellungsfunktion, die Aspose.Cells bereitstellt. Diese erste Version des Moduls ist mit den folgenden coolen Funktionen angereichert, um den Exportprozess einfach und benutzerfreundlich zu gestalten
### **Modulfunktionen**
Diese erste Version des Add-ons enthält folgende Funktionen:

- Erlauben Sie den Anschluss an die lokale MS SQL Server-Datenbank
- Erlauben Sie den Anschluss an die entfernte MS SQL Server-Datenbank
- Füllen Sie alle Tabellen aus der verbundenen Datenbank auf
- Füllen Sie alle Ansichten aus der verbundenen Datenbank auf
- Erlauben Sie die Erstellung einer benutzerdefinierten Abfrage
- Automatische Anpassung von Spalten an die Länge des Inhalts.
- Zulassen, dass Zeichenfolgen mit mehr als 32k in Excel-Zellen übersprungen werden (LoadOptions)
- Anwendung der Header-Spaltenformatierung als fettgedruckter Text
- Verwendung als Datenquelle zulassen (Tabelle, Ansichten, benutzerdefinierte Abfrage)
- Export von Daten in Microsoft Excel-Dokumente (.xls, .xlsx und .xlsb)
- Export von Daten in ein Tabstopp-Textdokument (*.txt)
- Export von Daten in CSV (durch Komma getrennt) (*.csv)
- Export von Daten in OpenDocument-Tabellenkalkulation (*.ods)
- Option zur Auswahl des gewünschten Ausgabeformats vor dem Export
- Das exportierte Dokument wird automatisch zum Herunterladen an den Browser gesendet 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **Systemanforderungen und unterstützte Plattformen**
### **Systemanforderungen**
Um den Aspose .NET Database Data Exporter to Excel für das Umbraco-Modul einzurichten, müssen folgende Anforderungen erfüllt sein:

- Umbraco 6.2.5 & Umbraco 6-Versionen
- Umbraco mit MS SQL Server
- Microsoft .Net Framework 4.0

**Hinweis:** Umbraco 7 und höher werden in dieser Version nicht unterstützt. Wir freuen uns auf Ihr Feedback und werden Unterstützung für Umbraco 7 in der nächsten Version hinzufügen.
### **Unterstützte Plattformen**
Das Modul wird auf allen Versionen von

- Umbraco 6.0 mit ASP.NET 4.0
## **Herunterladen**
Sie können das Aspose .NET Cells Database Data Exporter to Excel für Umbraco-Modul von einem der folgenden Orte herunterladen

- [Umbraco-Projekte](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **Installation**
Nach dem Download folgen Sie bitte diesen Schritten, um das Paket in Ihre Umbraco-Website zu installieren:

1. Melden Sie sich im Entwicklerbereich von Umbraco an, z.B. `http://www.myblog.com/umbraco`
1. Öffnen Sie im Baum die **Pakete**-Ordner.
1. Von hier aus gibt es zwei Möglichkeiten, ein Paket zu installieren: wählen Sie **Lokales Paket installieren** oder durchsuchen Sie das **Umbraco-Paketrespository.**
1. Wenn Sie ein **lokales Paket** installieren, entpacken Sie das Paket nicht, sondern laden Sie die ZIP-Datei in Umbraco hoch.
1. Befolgen Sie die Anweisungen auf dem Bildschirm.

**Hinweis:** Beim Installieren kann ein Fehler 'Maximale Anforderungslänge überschritten' auftreten. Sie können dieses Problem leicht beheben, indem Sie den Wert 'maxRequestLength' in Ihrer Umbraco-Web.config-Datei aktualisieren.
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **Verwendung**
Nachdem Sie den Aspose .NET Database Data Exporter to Excel für Umbraco-Modul installiert haben, ist es wirklich einfach, es auf Ihrer Website zu verwenden. Befolgen Sie bitte diese einfachen Schritte, um zu beginnen

1. Stellen Sie sicher, dass Sie im Entwicklerbereich von Umbraco angemeldet sind, z.B. `http://www.myblog.com/umbraco/`
1. Klicken Sie auf **Einstellungen** in der Liste der Abschnitte unten links auf dem Bildschirm.
1. Erweitern Sie den Knoten **Vorlagen** und wählen Sie die Vorlage, zu der Sie hinzufügen möchten, z.B. Textseite.
1. Wählen Sie die Position in der ausgewählten Vorlage aus, an der Sie die Exportschaltfläche hinzufügen möchten. Sie möchten sie in der Regel oben rechts auf der Seite oder am Ende der Seite hinzufügen.
1. Klicken Sie auf **Makro einfügen** im oberen Menüband.
1. Wählen Sie unter **Makro auswählen** (Aspose .NET Database Data Exporter to Excel für Umbraco) das kürzlich installierte Aspose .NET Database Data Exporter to Excel für Umbraco-Makro aus und klicken Sie auf **OK**.

Bitte überprüfen Sie den Screenshot unten für Details. 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

Sie haben das Aspose .NET Database Data Exporter to Excel-Modul erfolgreich zu Ihrer Seite hinzugefügt.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. Geben Sie ein oder verwenden Sie den vorab ausgefüllten MS SQL Server-Verbindungszeichenfolge
1. Wählen Sie den Datentyp aus (Tabelle, Ansicht, benutzerdefinierte Abfrage)
1. Wählen Sie den Datenquelle aus (Tabelle, Ansicht, benutzerdefinierte Abfrage) oder geben Sie diese ein
1. Wählen Sie den Exporttyp aus
1. Klicken Sie auf Daten exportieren
1. Die gewünschte Datei wird automatisch heruntergeladen.
## **Video-Demo**
Bitte überprüfen Sie [das Video](https://www.youtube.com/watch?v=MkfKyeLTauE) unten, um das Modul in Aktion zu sehen.
## **Unterstützung, Erweitern und Beitrag leisten**
### **Unterstützung**
Von den allerersten Tagen von Aspose an wussten wir, dass es nicht ausreichen würde, unseren Kunden einfach gute Produkte anzubieten. Wir mussten auch guten Service liefern. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Eigenart der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht sie zu schaffen.

Deshalb bieten wir kostenlosen Support an. Jeder, der unsere Produkte verwendet, egal ob sie sie gekauft haben oder eine Evaluierung durchführen, verdient unsere volle Aufmerksamkeit und Respekt.

Sie können Probleme oder Vorschläge im Zusammenhang mit den Aspose.Words .NET for Umbraco-Modulen in einem der folgenden Foren protokollieren

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Ausweiten und Beitrag leisten**
Exportieren Sie Mitglieder in Excel ist ein Open-Source-Add-On und der Quellcode ist auf den unten aufgeführten führenden sozialen Codierungs-Websites verfügbar. Entwickler sind dazu ermutigt, den Quellcode herunterzuladen und die Funktionalität entsprechend ihren eigenen Anforderungen zu erweitern.
#### **Quellcode**
Sie können den neuesten Quellcode von einem der folgenden Standorte erhalten

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **So konfigurieren Sie den Quellcode**
Sie müssen Folgendes installiert haben, um den Quellcode öffnen und erweitern zu können

- Visual Studio 2010 oder höher

Befolgen Sie bitte diese einfachen Schritte, um loszulegen

1. Den Quellcode herunterladen/klonen.
1. Öffnen Sie Visual Studio 2010 und wählen Sie **Datei** > **Projekt öffnen**
1. Suchen Sie den neuesten heruntergeladenen Quellcode und öffnen Sie **z.B. Aspose.DatabaseDataExportertoExcel.sln**

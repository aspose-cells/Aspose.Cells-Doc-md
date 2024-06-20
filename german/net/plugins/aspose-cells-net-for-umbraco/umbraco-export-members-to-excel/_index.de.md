---
title: Umbraco Export Mitglieder nach Excel
type: docs
weight: 10
url: /de/net/umbraco-export-members-to-excel/
---

## **Einführung**

Export Members to Excel ist ein Add-on für Umbraco, mit dem Sie Mitglieder aus Ihrem Umbraco CMS in ein Excel- und OpenDocument-Spreadsheet unter Verwendung von [Aspose.Cells](https://products.aspose.com/cells/net/) exportieren können. Nach der Installation wird im Umbraco-Backend ein neuer Knoten mit dem Titel **Export Members To Excel** unter dem Mitglieder-Baum angezeigt, in dem Sie einfach Mitglieder zum Exportieren und Ausgabeformat auswählen können, um Mitglieder im ausgewählten Dokumentformat zu erhalten.

### **Modulfunktionen**

Diese erste Version des Add-ons enthält folgende Funktionen:

- Exportieren von Mitgliedern in Microsoft Excel-Dokumente (.xls, .xlsx und .xlsb)
- Exportieren von Mitgliedern in tabellarisches Textdokument (.txt)
- Exportieren von Mitgliedern in CSV (durch Komma getrennt) (*.csv)
- Exportieren von Mitgliedern in OpenDocument-Spreadsheet (*.ods)
- Option zur Auswahl des gewünschten Ausgabeformats vor dem Exportieren
- Option zum Exportieren aller oder ausgewählter Mitglieder in das ausgewählte Ausgabedokumentformat.
- Funktioniert mit allen .NET-Versionen ab .NET 2.0.
- Das exportierte Dokument wird automatisch zum Herunterladen an den Browser gesendet
- Wenn ausgewählt, wird eine Kopie des exportierten Dokuments im Ordner App_Data/AsposeMemberExport auf dem Server zur späteren Verwendung gespeichert.
- Kompatibel mit einer breiten Palette von Umbraco-Versionen **4.5**+ **einschließlich Version 6 und 7.**

## **Systemanforderungen und unterstützte Plattformen**

### **Systemanforderungen**

Um dieses Modul einzurichten, müssen folgende Anforderungen erfüllt sein:

- Umbraco 6.0 +

Bitte kontaktieren Sie uns, wenn Sie dieses Modul auf anderen Versionen von Umbraco installieren möchten.

### **Unterstützte Plattformen**

Das Modul wird auf allen Versionen von

- Umbraco unter ASP.NET 4.0 unterstützt

## **Herunterladen**

Sie können das Export Members to Excel Add-on von einem der folgenden Orte herunterladen

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installation**

Nach dem Download folgen Sie bitte diesen Schritten, um das Paket in Ihre Umbraco-Website zu installieren:

1. Melden Sie sich im Entwicklerbereich von Umbraco an, z.B. `http://www.myblog.com/umbraco/`
1. Öffnen Sie im Baum die **Pakete**-Ordner.
1. Es gibt zwei Möglichkeiten, ein Paket zu installieren: Wählen Sie **Lokales Paket installieren** oder durchsuchen Sie das **Umbraco Package Repository.**
1. Wenn Sie ein **lokales Paket** installieren, entpacken Sie das Paket nicht, sondern laden Sie die ZIP-Datei in Umbraco hoch.
1. Befolgen Sie die Anweisungen auf dem Bildschirm.

**Hinweis:** Beim Installieren kann ein Fehler 'Maximale Anforderungslänge überschritten' auftreten. Sie können dieses Problem leicht beheben, indem Sie den Wert 'maxRequestLength' in Ihrer Umbraco-Web.config-Datei aktualisieren.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Verwendung**

Nachdem Sie das Makro installiert haben, ist es wirklich einfach, es auf Ihrer Website zu verwenden:

1. Stellen Sie sicher, dass Sie im Umbraco **Entwickler**-Bereich angemeldet sind, z.B. `http://www.myblog.com/umbraco/`
1. Klicken Sie im Abschnittslisten unten links auf dem Bildschirm auf **Mitglieder**.
1. Am Ende des Baums sehen Sie einen Knoten mit dem Titel **Mitglieder in Excel exportieren**. Klicken Sie darauf, um das Exportieren in Excel-Add-On zu starten.
1. Wählen Sie Ihr gewünschtes Ausgabe-Dokumentformat aus und wählen Sie die zu exportierenden Mitglieder. Wenn Sie alle Mitglieder exportieren möchten, lassen Sie die Mitgliedsauswahl leer oder klicken Sie auf die Kontrollkästchen in der Kopfzeile.
1. Klicken Sie auf die Schaltfläche **Exportieren** unten und Sie werden aufgefordert, die exportierte Datei herunterzuladen.

## **Video-Demo**

Bitte schauen Sie sich [das Video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) unten an, um das Modul in Aktion zu sehen.

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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **So konfigurieren Sie den Quellcode**

Sie müssen Folgendes installiert haben, um den Quellcode öffnen und erweitern zu können

- Visual Studio 2010 oder höher

Befolgen Sie bitte diese einfachen Schritte, um loszulegen

1. Den Quellcode herunterladen/klonen.
1. Öffnen Sie Visual Studio 2010 und wählen Sie **Datei** > **Projekt öffnen**
1. Gehen Sie zum neuesten heruntergeladenen Quellcode und öffnen Sie z. B. **Aspose.UmbracoMemberExportToExcel.sln**

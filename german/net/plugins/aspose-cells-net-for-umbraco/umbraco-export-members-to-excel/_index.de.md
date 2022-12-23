---
title: Umbraco Mitglieder nach Excel exportieren
type: docs
weight: 10
url: /de/net/umbraco-export-members-to-excel/
---
## **Einführung**

 Mitglieder nach Excel exportieren ist ein Add-on für Umbraco, mit dem Sie Mitglieder aus Ihrem Umbraco-CMS in eine Excel- und OpenDocument-Tabelle exportieren können[Aspose.Cells](https://products.aspose.com/cells/net/) . Ein neuer Knoten mit dem Titel**Mitglieder nach Excel exportieren**erscheint nach der Installation im Mitgliederbaum im Umbraco-Backend, wo Sie einfach Mitglieder zum Exportieren und Ausgabeformat auswählen können, um Mitglieder im ausgewählten Ausgabedokumentformat zu erhalten.

### **Modulfunktionen**

Diese erste Version des Add-ons hat die folgenden Funktionen:

- Mitglieder in Microsoft Excel-Dokumente exportieren (.xls, .xlsx und .xlsb)
- Mitglieder in ein tabulatorgetrenntes Textdokument (.txt) exportieren
- Mitglieder exportieren nach CSV (kommagetrennt) (*.csv)
- Mitglieder in OpenDocument Spreadsheet (*.ods) exportieren
- Option zur Auswahl des gewünschten Ausgabeformats vor dem Export
- Option zum Exportieren aller oder ausgewählter Elemente in das ausgewählte Ausgabedokumentformat.
- Funktioniert mit allen .NET-Versionen ab .NET 2.0.
- Das exportierte Dokument wird automatisch zum Herunterladen an den Browser gesendet
- Wenn ausgewählt, wird eine Kopie des exportierten Dokuments im Ordner „App_Data/AsposeMemberExport“ auf dem Server zur späteren Verwendung gespeichert.
-  Kompatibel mit einer Vielzahl von Umbraco-Versionen**4.5**+ **einschließlich Version 6 und 7.**

## **Systemanforderungen und unterstützte Plattformen**

### **System Anforderungen**

Um dieses Modul einzurichten, müssen Sie die folgenden Voraussetzungen erfüllen:

- Umbraco 6.0 +

Bitte zögern Sie nicht, uns zu kontaktieren, wenn Sie dieses Modul auf anderen Versionen von Umbraco installieren möchten.

### **Unterstützte Plattformen**

Das Modul wird von allen Versionen von unterstützt

- Umbraco läuft auf ASP.NET 4.0

## **wird heruntergeladen**

Sie können das Export Members to Excel Add-on von einem der folgenden Orte herunterladen

- [ GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installieren**

Führen Sie nach dem Herunterladen die folgenden Schritte aus, um dieses Paket auf Ihrer Umbraco-Website zu installieren:

1.  Melden Sie sich bei Umbraco an**Entwickler** Abschnitt, zum Beispiel `http://www.myblog.com/umbraco/`
1.  Erweitern Sie aus dem Baum die**Pakete** Mappe.
1.  Von hier aus gibt es zwei Möglichkeiten, ein Paket zu installieren: select**Lokales Paket installieren** oder durchsuchen Sie die**Umbraco-Paket-Repository.**
1. Wenn Sie installieren**lokales Paket**, entpacken Sie das Paket nicht, sondern laden Sie die Zip-Datei in Umbraco.
1. Folgen Sie den Anweisungen auf dem Bildschirm.

**Notiz:** Möglicherweise erhalten Sie bei der Installation die Fehlermeldung „Maximale Anforderungslänge überschritten“. Sie können dieses Problem einfach beheben, indem Sie den Wert „maxRequestLength“ in Ihrer web.config-Datei von Umbraco aktualisieren.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Verwenden**

Nachdem Sie das Makro installiert haben, ist es wirklich einfach, es auf Ihrer Website zu verwenden:

1. Stellen Sie sicher, dass Sie bei Umbraco angemeldet sind**Entwickler** Abschnitt, zum Beispiel `http://www.myblog.com/umbraco/`
1.  Klicken**Mitglieder** in der Liste der Abschnitte unten links auf dem Bildschirm.
1.  Am Ende des Baums sehen Sie einen Knoten mit dem Titel**Mitglieder nach Excel exportieren** Klicken Sie darauf, um das Add-on „Export to Excel“ zu starten.
1. Wählen Sie das gewünschte Ausgabedokumentformat und wählen Sie Mitglieder zum Exportieren aus. Wenn Sie alle Mitglieder exportieren möchten, verlassen Sie die Mitgliederauswahl oder klicken Sie auf das Kontrollkästchen in der Kopfzeile.
1.  Klicken**Export** Schaltfläche unten und Sie werden aufgefordert, die exportierte Datei herunterzuladen.

## **Video-Demo**

 Bitte prüfe[das Video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) unten, um das Modul in Aktion zu sehen.

## **Unterstützen, erweitern und beitragen**

### **Unterstützung**

Von den ersten Tagen der Aspose wussten wir, dass es nicht ausreichen würde, unseren Kunden nur gute Produkte zu geben. Wir mussten auch einen guten Service bieten. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Macke in der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht um sie zu erschaffen.

Aus diesem Grund bieten wir kostenlosen Support an. Jeder, der unser Produkt verwendet, ob er es gekauft hat oder eine Bewertung verwendet, verdient unsere volle Aufmerksamkeit und unseren Respekt.

Sie können alle Probleme oder Vorschläge im Zusammenhang mit Aspose.Words .NET für Umbraco-Module über eine der folgenden Plattformen protokollieren

- [ GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Erweitern und beitragen**

Export Members to Excel ist ein Open-Source-Add-on und sein Quellcode ist auf den unten aufgeführten wichtigen Social-Coding-Websites verfügbar. Entwickler werden ermutigt, den Quellcode herunterzuladen und die Funktionalität gemäß ihren eigenen Anforderungen zu erweitern.

#### **Quellcode**

Den neuesten Quellcode erhalten Sie von einer der folgenden Stellen

- [ GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **So konfigurieren Sie den Quellcode**

Sie müssen Folgendes installiert haben, um den Quellcode öffnen und erweitern zu können

- Visual Studio 2010 oder höher

Bitte befolgen Sie diese einfachen Schritte, um loszulegen

1. Laden Sie den Quellcode herunter/klonen Sie ihn.
1.  Öffnen Sie Visual Studio 2010 und wählen Sie aus**Datei** > **Offenes Projekt**
1.  Navigieren Sie zum neuesten Quellcode, den Sie heruntergeladen und geöffnet haben**zB Aspose.UmbracoMemberExportToExcel.sln**

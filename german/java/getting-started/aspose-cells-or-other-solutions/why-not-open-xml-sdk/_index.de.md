---
title: Warum nicht Open XML SDK
type: docs
weight: 20
url: /de/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

Manchmal hören wir diese Frage:

**Warum sollten wir Aspose-Produkte anstelle des kostenlosen Open XML SDK verwenden?**

 Diese Frage ist einfach zu beantworten:**Eigenschaften und Funktionalität**.

{{% /alert %}} 
## ** Was ist Open XML SDK?**
Gemäß der MSDN Library ist Open XML SDK wie folgt definiert: Das Open XML SDK 2.0 vereinfacht die Aufgabe, Open XML-Pakete und die zugrunde liegenden Open XML-Schemaelemente innerhalb eines Pakets zu manipulieren. Das Open XML SDK 2.0 kapselt viele allgemeine Aufgaben, die Entwickler an Open XML-Paketen ausführen, sodass Sie komplexe Vorgänge mit nur wenigen Codezeilen ausführen können. OOXML-Dokumente sind im Wesentlichen gezippte XML-Dateien und Open XML SDK ist eine Sammlung von Klassen, die dies ermöglichen Ihnen, stark typisiert mit dem Inhalt von OOXML-Dokumenten zu arbeiten. Anstatt eine Datei zu entpacken, um XML zu extrahieren, dieses XML in einen DOM-Baum zu laden und direkt mit XML-Elementen und -Attributen zu arbeiten, bietet Open XML SDK Klassen, um dies zu tun.
## ** Was ist Aspose.Cells?**
Aspose.Cells ist eine Klassenbibliothek, mit der Ihre Anwendung die folgenden Tabellenverarbeitungsaufgaben ausführen kann: Hochwertige Konvertierungen zwischen allen gängigen Excel-Formaten, einschließlich Konvertierung in PDF, HTML, TIFF und Drucken. Programmieren mit einem Arbeitsmappen-Objektmodell. Fähigkeit, Dokumente aus Fragmenten, aus einem oder mehreren Dokumenten zu erstellen, während Daten durch stilistische Formatierung, Diagramme und Grafiken automatisch zusammengeführt werden. High-Level-Funktionen, wie z. B. Importieren von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable / ResultSet. Robustes Formelberechnungsmodul, das fast alle Standard- und erweiterten Microsoft-Excel-Funktionen unterstützt.

{{% alert color="primary" %}}
## ** Vergleichen Sie Open XML SDK und Aspose.Cells**
 In der folgenden Tabelle werden die Funktionen von Open XML SDK und Aspose.Cells verglichen.{{% /alert %}}

|**Feature oder Feature-Kategorie**|**Öffnen Sie das XML-SDK**|**Aspose.Cells**|
|:- |:- |:- |
|Unterstützte Excel- oder andere Formate|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tabulatorgetrennt, ODS, Nur-Text (TXT), PDF, XPS|
|Konvertieren Sie zwischen Excel-Formaten|Nein|Ja|
|<p>High-Level-Programmierung mit einem Arbeitsmappen-Objektmodell:</p><p>- Suchen und Ersetzen.</p><p>- Erstellen Sie Tabellenkalkulationen.</p><p>- Kopieren Sie Fragmente und Arbeitsblätter zwischen Arbeitsmappen.</p>|Nein|Ja|
|Detaillierte Programmierung mit einem Document Object Model, Zugriff auf einzelne Elemente und Formatierungseigenschaften aller Spreadsheet-Elemente.|Ja|Ja|
|Direkter und vollständiger Low-Level-Zugriff auf die zugrunde liegenden XML-Elemente und -Attribute wie Beziehungskennungen, Listenkennungen eines OOXML-Dokuments.|Ja|Nein|
|<p>Berichte erstellen, Dokumente mit Daten füllen:</p><p>- Importieren/Exportieren von Daten zu/von a*Datentabelle /*Ergebnissatz.</p><p>- Smart-Marker-Funktion.</p><p>- Zeilen/Spalten/Bereiche einfügen/löschen.</p><p>- Benutzerdefinierte Datenquellen.</p>|Nein|Ja|
|<p>Rendern und Drucken:* Rendern Sie Arbeitsblattseiten in Rasterbilder (TIFF, mehrseitiges TIFF, PNG, JPEG, BMP).*Rendern Sie Tabellenkalkulationsseiten in Vektorgrafiken (EMF).* Konvertieren Sie Diagramme in Bilder (TIFF, mehrseitiges TIFF, PNG, JPEG, BMP, EMF usw.)</p><p>- Geben Sie Bildauflösung, Qualität, Komprimierung und andere Optionen an. </p><p>- Drucken Sie Tabellen mit der Druckinfrastruktur .NET. Die Komponente verfügt über eine integrierte Druckmethode zum Drucken der Arbeitsblätter, wie in der Druckvorschau von MS Excel gezeigt.</p>|Nein|Ja|
|Formeln dynamisch berechnen/neu berechnen| Nein| Ja|
|Unterstützte Plattformen|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Fazit**
  {{% alert color="primary" %}}Open XML SDK und Aspose.Cells konkurrieren nicht direkt, da sie ganz unterschiedliche Anforderungen und Zielgruppen ansprechen. Open XML SDK ist eine Klassenbibliothek, die eine stark typisierte Möglichkeit bietet, mit OOXML-Dokumenten zu arbeiten. Aspose.Cells ist eine sehr nützliche Tabellenverarbeitungsbibliothek, die alle Microsoft Excel- und andere Dateiformate hervorragend unterstützt. Wenn Sie nur einen ziemlich einfachen Programmiervorgang für ein XLSX-Dokument ausführen müssen, ist Open XML SDK möglicherweise eine geeignete Wahl. Mit Open XML SDK können Sie einfache Aufgaben wie das Generieren eines einfachen XLSX-Dokuments oder das Entfernen von Kommentaren, Kopf-/Fußzeilen, das Extrahieren von Bildern usw. ziemlich bequem erledigen. Einige Aufgaben können mit Open XML SDK erfüllt werden, aber nicht mit Aspose.Cells. Wenn Sie beispielsweise direkt auf die XML-Elemente und Attribute eines OOXML-Dokuments zugreifen müssen, sollten Sie Open XML SDK verwenden Führen Sie komplexe Operationen an Dokumenten durch, wie z. B. einige der folgenden Aufgaben, dann ist die Verwendung von Aspose.Cells Ihre beste Option: Unterstützung anderer Dateiformate zusätzlich zu XLSX. Kopieren Sie Fragmente und Arbeitsblätter zwischen Arbeitsmappen oder verbinden Sie Arbeitsmappen auf eine Weise, die Objekte, Stile und andere Formatierungen auf geeignete Weise kombiniert. Formatierten oder unformatierten Text ersetzen. High-Level-Funktionen, wie z. B. Importieren von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable / ResultSet. Generieren Sie ein Geschäftsdokument, z. B. eine Bestellung mit Bestelldetails aus einer Datenquelle. Konvertieren Sie ein Dokument in PDF oder XPS, sodass es genau so aussieht, wie Microsoft Excel es konvertiert hätte. Entwickeln Sie eine .NET- oder Java-Anwendung.{{% /alert %}}

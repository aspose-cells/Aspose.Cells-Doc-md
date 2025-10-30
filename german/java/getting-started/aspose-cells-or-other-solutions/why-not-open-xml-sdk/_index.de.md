---
title: Warum nicht Open XML SDK
type: docs
weight: 20
url: /de/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

Manchmal hören wir diese Frage:

**Warum sollten wir Aspose-Produkte anstelle des kostenlosen Open XML SDK verwenden?**

Diese Frage ist leicht zu beantworten: **Funktionen und Funktionalität**.

{{% /alert %}} 
## **Was ist Open XML SDK?**
Laut der MSDN Library wird das Open XML SDK folgendermaßen definiert: Das Open XML SDK 2.0 vereinfacht die Aufgabe der Manipulation von Open XML-Paketen und der zugrunde liegenden Open XML-Schemaelemente innerhalb eines Pakets. Das Open XML SDK 2.0 kapselt viele der gängigen Aufgaben ein, die Entwickler mit Open XML-Paketen ausführen, sodass Sie komplexe Operationen mit nur wenigen Codezeilen ausführen können. OOXML-Dokumente sind im Wesentlichen komprimierte XML-Dateien, und das Open XML SDK ist eine Sammlung von Klassen, die es Ihnen ermöglichen, mit dem Inhalt von OOXML-Dokumenten in einer stark typisierten Weise zu arbeiten. Anstatt also eine Datei zu entpacken, um XML zu extrahieren, dieses XML in einen DOM-Baum zu laden und direkt mit XML-Elementen und Attributen zu arbeiten, bietet das Open XML SDK Klassen, um das zu erledigen.
## **Was ist Aspose.Cells?**
Aspose.Cells ist eine Klassenbibliothek, die es Ihrer Anwendung ermöglicht, folgende Tabellenkalkulationsverarbeitungsaufgaben auszuführen: Hochwertige Konvertierungen zwischen allen gängigen Excel-Formaten, einschließlich der Konvertierung nach PDF, HTML, TIFF und Drucken. Programmierung mit einem Arbeitsmappenobjektmodell. Möglichkeit, Dokumente aus Fragmenten, aus einem oder mehreren Dokumenten zu erstellen, während Daten automatisch durch stilistische Formatierung, Diagramme und Grafiken zusammengeführt werden. Hochrangige Funktionen, wie z. B. Import von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable / ResultSet. Robuste Formelberechnungsmaschine, die fast alle Standard- und erweiterten Microsoft Excel-Funktionen unterstützt.


## **Vergleichen Sie Open XML SDK und Aspose.Cells**
Die folgende Tabelle vergleicht Open XML SDK und Aspose.Cells Features. 

|**Funktion oder Funktionskategorie**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Unterstützte Excel- oder andere Formate|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tabulatorgetrennt, ODS, Klartext (TXT), PDF, XPS|
|Konvertierung zwischen Excel-Formaten|Nein|Ja|
|<p>Hochstufige Programmierung mit einem Arbeitsmappen-Objektmodell:</p><p>- Suchen und Ersetzen.</p><p>- Tabellenkalkulationen zusammenstellen.</p><p>- Fragmente und Tabellenblätter zwischen Arbeitsmappen kopieren.</p>|Nein|Ja|
|Detailliertes Programmieren mit einem Dokumentenobjektmodell, Zugriff auf einzelne Elemente und Formatierungseigenschaften aller Elemente in der Tabellenkalkulation|Ja|Ja|
|Niedrigstufiger direkter und vollständiger Zugriff auf die zugrunde liegenden XML-Elemente und -Attribute wie Beziehungsidentifikatoren, Listenidentifikatoren eines OOXML-Dokuments.|Ja|Nein|
|<p>Generieren von Berichten, Befüllen von Dokumenten mit Daten:</p><p>- Import/Export von Daten zu/von einem *DataTable /* ResultSet.</p><p>- Smart Markers-Funktion.</p><p>- Zeilen/Spalten/Bereiche einfügen/löschen.</p><p>- Benutzerdefinierte Datenquellen.</p>|Nein|Ja|
|<p>Rendering und Drucken:* Arbeitsblattseiten als Rasterbilder rendern (TIFF, mehrseitiges TIFF, PNG, JPEG, BMP).* Tabellenkalkulationsseiten als Vektorbilder rendern (EMF).* Diagramme in Bilder umwandeln (TIFF, mehrseitiges TIFF, PNG, JPEG, BMP, EMF usw.)</p><p>- Bildauflösung, Qualität, Komprimierung und andere Optionen festlegen.</p><p>- Tabellenkalkulationen mit der .NET-Druckinfrastruktur drucken. Das Komponente verfügt über eine integrierte Druckmethode, um die Arbeitsblätter wie in der Druckvorschau von MS Excel zu drucken.</p>|Nein|Ja|
|Formeln dynamisch berechnen/neu berechnen|Nein |Ja |
|Unterstützte Plattformen|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Fazit**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}

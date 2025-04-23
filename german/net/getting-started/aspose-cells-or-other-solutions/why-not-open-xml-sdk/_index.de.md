---
title: Warum nicht Open XML SDK
type: docs
weight: 90
url: /de/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

Manchmal hören wir diese Frage:

**Warum sollten wir Aspose-Produkte anstelle des kostenlosen Open XML SDK verwenden?**

Diese Frage ist leicht zu beantworten: Funktionen und Funktionalität.

{{% /alert %}}

## **Was ist das Open XML SDK?**

Gemäß der [MSDN-Bibliothek](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN) wird das Open XML SDK definiert als:

"Das Open XML SDK 2.5 vereinfacht die Aufgabe der Manipulation von Open XML-Paketen und der zugrunde liegenden Open XML-Schemaelemente innerhalb eines Pakets. Das Open XML SDK 2.5 umfasst viele gängige Aufgaben, die Entwickler bei Open XML-Paketen ausführen, so dass Sie komplexe Operationen mit nur wenigen Codezeilen ausführen können."

OOXML-Dokumente sind im Wesentlichen komprimierte XML-Dateien, und das Open XML SDK ist eine Sammlung von Klassen, die es Ihnen ermöglicht, mit dem Inhalt von OOXML-Dokumenten auf eine stark typisierte Weise zu arbeiten. Dadurch, anstatt eine Datei zu entpacken, um XML zu extrahieren, dieses XML in einen DOM-Baum zu laden und direkt mit XML-Elementen und -Attributen zu arbeiten, bietet das Open XML SDK Klassen, um dies zu tun.

## **Was ist Aspose.Cells?**

Aspose.Cells ist eine Klassenbibliothek, die Anwendungen die folgenden Tabellenkalkulationsverarbeitungsaufgaben ermöglicht:

- Hochwertige Konvertierungen zwischen allen gängigen Microsoft Excel-Formaten, einschließlich Konvertierung in PDF, HTML, TIFF und Drucken.
- Programmierung mit einem Arbeitsmappen-Objektmodell.
- Möglichkeit, Dokumente aus Fragmenten, aus einem oder mehreren Dokumenten, zu erstellen, während Daten automatisch durch stilistische Formatierung, Diagramme und Grafiken zusammengeführt werden.
- Hochrangige Funktionen wie Importieren von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable / ResultSet.
- Robuste Formelberechnungsmaschine, die nahezu alle gängigen und erweiterten Microsoft Excel-Funktionen unterstützt.

## **Vergleich zwischen Open XML SDK und Aspose.Cells**

Die folgende Tabelle vergleicht die Funktionen des Open XML SDK und von Aspose.Cells:

|**Funktion oder Funktionskategorie**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Unterstützte Excel- oder andere Formate|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tabulatorgetrennt, ODS, Klartext (TXT), PDF, XPS|
|Konvertierung zwischen Excel-Formaten|Nein|Ja|
|<p>Hochstufige Programmierung mit einem Arbeitsmappen-Objektmodell:</p><p>- Suchen und Ersetzen.</p><p>- Tabellenkalkulationen zusammenstellen.</p><p>- Fragmente und Tabellenblätter zwischen Arbeitsmappen kopieren.</p>|Nein|Ja|
|Detailliertes Programmieren mit einem Dokumentenobjektmodell, Zugriff auf einzelne Elemente und Formatierungseigenschaften aller Elemente in der Tabellenkalkulation|Ja|Ja|
|Niedrigstufiger direkter und vollständiger Zugriff auf die zugrunde liegenden XML-Elemente und -Attribute wie Beziehungsidentifikatoren, Listenidentifikatoren eines OOXML-Dokuments.|Ja|Nein|
|<p>Generieren von Berichten, Befüllen von Dokumenten mit Daten:</p><p>- Import/Export von Daten aus/ein eine DataTable / _ResultSet.</p><p>- Smart-Markers-Funktion.</p><p>- Einfügen/Löschen von Zeilen/Spalten/Bereichen.</p><p>- Benutzerdefinierte Datenquellen.</p>|Nein|Ja|
|<p>Rendering und Drucken:* Arbeitsblattseiten als Rasterbilder rendern (TIFF, mehrseitige TIFF, PNG, JPEG, BMP).* Tabellenkalkulationsseiten als Vektorbilder rendern (EMF).</p><p>- Diagramme in Bilder umwandeln (TIFF, mehrseitige TIFF, PNG, JPEG, BMP, EMF usw.)</p><p>- Bildauflösung, Qualität, Komprimierung und andere Optionen festlegen.</p><p>- Tabellenkalkulationen mit der .NET-Druckinfrastruktur drucken. Das Modul verfügt über eine integrierte Druckmethode, um die Arbeitsblätter wie in der Druckvorschau von Microsoft Excel anzuzeigen.</p>|Nein|Ja|
|Formeln dynamisch berechnen/neu berechnen|Nein|Ja|
|Unterstützte Plattformen|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Sie können OpenXML mit Aspose.Cells vergleichen, um diese Aufgaben zu erledigen, schlagen wir vor, dass Sie sich mit dem Aspose.Cells for OpenXML-Projekt vertraut machen - es zeigt, wie verschiedene Aufgaben mit der Aspose.Cells for .NET-API im Vergleich zu OpenXML erledigt werden können. Das Projekt behandelt auch Funktionen zum Arbeiten mit Textdokumenten, die nur in Aspose.Cells, jedoch nicht in OpenXML verfügbar sind.

Dieses Projekt ist auch für Entwickler nützlich, die von OpenXML zu Aspose.Cells migrieren möchten.

{{% alert color="primary" %}}

Erkunden Sie [das Plugin mit Quellcodebeispielen der Aspose.Cells for .NET-Funktionen im Vergleich zu OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Dieses Plugin verwendet die Evaluierungsversion von Aspose.Cells. Wenn Sie mit Ihrer Evaluierung zufrieden sind, können Sie eine Lizenz von der [Aspose-Website](https://purchase.aspose.com/buy) erwerben. Um die Evaluierungsmeldung und die Funktionsbeschränkungen zu entfernen, müssen Sie eine Produktlizenz anwenden. Nach dem Kauf des Produkts erhalten Sie eine Lizenzdatei. Befolgen Sie bitte die Anweisungen im ["Lizenzierung und Abonnement"](/cells/de/net/licensing/) Artikel.

{{% /alert %}}

**Fazit**: Open XML SDK und Aspose.Cells konkurrieren nicht direkt miteinander, da sie ziemlich unterschiedliche Anforderungen und Zielgruppen berücksichtigen.

## **Warum nicht Open XML SDK**
Open XML SDK ist eine Klassenbibliothek, die eine typsichere Möglichkeit zum Arbeiten mit OOXML-Dokumenten bietet. Aspose.Cells ist eine sehr nützliche Tabellenkalkulationsverarbeitungsbibliothek, die umfassende Unterstützung für alle Microsoft Excel- und andere Dateiformate bietet.

Wenn alles, was Sie tun müssen, eine ziemlich einfache Programmieroperation an einem XLSX-Dokument ist, dann könnte Open XML SDK eine geeignete Wahl sein. Mit Open XML SDK werden Sie sich recht wohl dabei fühlen, einfache Aufgaben wie die Generierung eines einfachen XLSX-Dokuments oder das Entfernen von Kommentaren, Kopf-/Fußzeilen, Extrahieren von Bildern oder andere zu erledigen. 
Einige Aufgaben können mit dem Open XML SDK erledigt werden, können jedoch nicht mit Aspose.Cells erledigt werden. Zum Beispiel, wenn Sie direkten Zugriff auf die XML-Elemente und -Attribute eines OOXML-Dokuments benötigen, dann sollten Sie das Open XML SDK verwenden.

Wenn Sie jedoch komplexe Operationen an Dokumenten durchführen müssen, wie einige der folgenden Aufgaben, dann ist die Verwendung von Aspose.Cells die beste Option:

- Unterstützung anderer Dateiformate zusätzlich zu XLSX.
- Kopieren von Fragmenten und Arbeitsblättern zwischen Arbeitsmappen oder Verknüpfen von Arbeitsmappen in einer Weise, die Objekte, Stile und andere Formatierungen angemessen kombiniert.
- Ersetzen von formatiertem oder unformatiertem Text.
- Hochrangige Funktionen wie Importieren von Daten aus verschiedenen Datenquellen, einschließlich Array, ArrayList, DataTable / ResultSet.
- Generieren Sie ein Geschäftsdokument, wie beispielsweise eine Bestellung mit Bestelldetails aus einer Datenquelle.
- Konvertieren Sie ein Dokument in PDF oder XPS, sodass es genau so aussieht, als hätte Microsoft Excel es konvertiert.
- Entwickeln Sie eine .NET- oder Java-Anwendung.

{{< app/cells/assistant language="csharp" >}}

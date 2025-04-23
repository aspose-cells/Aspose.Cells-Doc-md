---
title: Web Erweiterungen  Office Add ins
type: docs
weight: 120
url: /de/java/web-extensions-office-add-ins/
---

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit dem Inhalt in Office-Dokumenten. Web-Erweiterungen fügen Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office Add-ins) in Excel hinzufügen, indem Sie auf das **Einfügen**-Register und dann auf den Link **Store**/**Add-ins abrufen** klicken. Suchen Sie im Add-ins-Feld nach dem gewünschten Add-in und fügen Sie es hinzu.

Aspose.Cells bietet auch die Funktion, Web-Erweiterungen mithilfe der Klassen WebExtension und WebExtensionTaskPane hinzuzufügen. Das folgende Codebeispiel zeigt die Verwendung der Klassen WebExtension und WebExtensionTaskPane zum Hinzufügen einer Web-Erweiterung zur Excel-Datei. Bitte sehen Sie die generierte [Output-Excel-Datei](AddWebExtension_Out.xlsx), um Bezug zu nehmen.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells bietet die Möglichkeit, die Informationen von Web-Erweiterungen in Excel-Dateien abzurufen. Das folgende Codebeispiel zeigt, wie auf Informationen zu Web-Erweiterungen zugegriffen wird, indem die [Beispiel-Excel-Datei](WebExtensionsSample.xlsx) geladen wird. Bitte sehen Sie die Konsolenausgabe, die durch den Code generiert wird, für Bezugnahme.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

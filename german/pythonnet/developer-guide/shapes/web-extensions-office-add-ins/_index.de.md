---
title: Web Erweiterungen  Office Add ins
type: docs
weight: 130
url: /de/python-net/web-extensions-office-add-ins/
---

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit dem Inhalt in Office-Dokumenten. Web-Erweiterungen fügen Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells für Python via .NET bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office-Add-Ins) in Excel hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann auf den Link **Store**/**Add-ins abrufen** klicken. Im Add-Ins-Feld suchen Sie das Add-In, das Sie möchten, und fügen Sie es hinzu.

Aspose.Cells für Python via .NET ermöglicht außerdem das Hinzufügen von Web-Erweiterungen durch die Klassen [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). Das folgende Beispiel demonstriert die Verwendung der Klassen [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane), um eine Web-Erweiterung zu einer Excel-Datei hinzuzufügen. Bitte sehen Sie sich die durch den Code generierte [Ausgabedatei Excel](89849869.xlsx) zur Referenz an.

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells für Python via .NET ermöglicht den Zugriff auf Informationen zu Web-Erweiterungen in Excel-Dateien. Das folgende Beispiel zeigt, wie man Web-Erweiterungsinformationen durch Laden der [Beispiel-Excel-Datei](89849870.xlsx) abruft. Bitte sehen Sie sich die Konsolenausgabe an, die vom Code generiert wird, zur Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}

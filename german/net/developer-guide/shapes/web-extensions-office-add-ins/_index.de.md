---
title: Web Erweiterungen  Office Add ins
type: docs
weight: 130
url: /de/net/web-extensions-office-add-ins/
---

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit dem Inhalt in Office-Dokumenten. Web-Erweiterungen fügen Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office-Add-Ins) in Excel hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann auf den Link **Store**/**Add-ins abrufen** klicken. Im Add-Ins-Feld suchen Sie das Add-In, das Sie möchten, und fügen Sie es hinzu.

Aspose.Cells bietet auch die Möglichkeit, Web-Erweiterungen mit den Klassen [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) hinzuzufügen. Das folgende Codebeispiel zeigt die Verwendung der Klassen [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane), um eine Web-Erweiterung zur Excel-Datei hinzuzufügen. Bitte sehen Sie die durch den Code generierte [Ausgabedatei im Excel-Format](89849869.xlsx) als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells bietet die Möglichkeit, auf die Informationen von Web-Erweiterungen in der Excel-Datei zuzugreifen. Das folgende Codebeispiel zeigt, wie auf die Informationen der Web-Erweiterung durch Laden der [Beispiel-Excel-Datei](89849870.xlsx) zugegriffen wird. Bitte sehen Sie die durch den Code generierte Konsolenausgabe als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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

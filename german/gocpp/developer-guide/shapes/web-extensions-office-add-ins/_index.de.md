---
title: Web Erweiterungen  Office Add ins mit Golang über C++
linktitle: Web Erweiterungen  Office Add ins
type: docs
weight: 130
url: /de/go-cpp/web-extensions-office-add-ins/
description: Erfahren Sie, wie Sie Web Erweiterungen (Office Add ins) in Excel Dateien mit Aspose.Cells und Golang über C++ hinzufügen und zugreifen.
---

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit Inhalten in Office-Dokumenten. Web-Erweiterungen fügen den Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office-Add-Ins) in Excel hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann auf den Link **Store**/**Add-Ins holen**. Im Add-In-Fenster durchsuchen Sie nach dem gewünschten Add-In und fügen es hinzu.

Aspose.Cells bietet auch die Funktion, Web-Erweiterungen mit den Klassen [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) hinzuzufügen. Das folgende Codebeispiel zeigt die Verwendung der Klassen [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/), um eine Web-Erweiterung zu einer Excel-Datei hinzuzufügen. Bitte sehen Sie sich die [Ausgabedatei](89849869.xlsx) an, die durch den Code erstellt wurde.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells ermöglicht den Zugriff auf Informationen von Web-Erweiterungen in einer Excel-Datei. Das folgende Codebeispiel zeigt, wie man Web-Erweiterungsinformationen durch Laden der [Beispiel-Excel-Datei](89849870.xlsx) abruft. Bitte sehen Sie sich die Konsolenausgabe an, die vom Code erzeugt wird.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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

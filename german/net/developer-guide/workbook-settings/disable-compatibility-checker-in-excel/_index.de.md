---
title: Kompatibilitätsprüfung in Excel deaktivieren
type: docs
weight: 170
url: /de/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## Deaktivieren Sie die Kompatibilitätsprüfung in Excel-Arbeitsblättern in C#

{{% alert color="primary" %}}

Microsoft Flags der Kompatibilitätsprüfung von Excel beim Speichern einer Datei in einem früheren Dateiformat können zu Funktionsproblemen oder Verlust der Wiedergabetreue führen. Die Kompatibilitätsprüfung ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, aus Excel 2007 oder Excel 2010 speichern, scannt die Kompatibilitätsprüfung die Arbeitsmappe, um festzustellen, ob sie Features enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen zu helfen, Entscheidungen zur Behandlung von Kompatibilitätsproblemen zu treffen, zeigt die Kompatibilitätsprüfung Dialogfelder mit Optionen an. Es kann auch verwendet werden, um einen Bericht zu Problemen in der Arbeitsmappe zu erstellen oder die Funktion zu deaktivieren.

Manchmal müssen Sie die Kompatibilitätsprüfung für eine bestimmte Tabelle deaktivieren. Mit Aspose.Cells'-APIs können Sie dies programmgesteuert tun, damit Benutzer nicht frustriert oder verwirrt werden, wenn das Dialogfeld „Kompatibilitätsprüfung“ angezeigt wird, wenn sie die Datei erneut manuell in Microsoft Excel speichern.

{{% /alert %}}

## **Mit Microsoft Excel**

So deaktivieren Sie die Kompatibilitätsprüfung in Microsoft Excel (z. B. Microsoft Excel 2007/2010):

-  (Excel 2007) Klicken Sie auf die Office-Schaltfläche**Vorbereiten** , dann**Führen Sie die Kompatibilitätsprüfung aus** , und löschen Sie dann die**Überprüfen Sie die Kompatibilität, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.
-  (Excel 2010) Klicken Sie auf der Registerkarte Datei auf**Die Info** , dann**Auf Probleme prüfen** , klicken**Kompatibilität prüfen** , und löschen Sie schließlich die**Überprüfen Sie die Kompatibilität, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.

## **Verwenden von Aspose.Cells-APIs**

 Stellen Sie die ein[**Arbeitsmappe.Einstellungen.Kompatibilität prüfen**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) Eigentum zu**FALSCH** um die Kompatibilitätsprüfung von Microsoft Excel zu deaktivieren.

### **Codebeispiele**

Die folgenden Codebeispiele zeigen, wie Sie die Kompatibilitätsprüfung mit Aspose.Cells for .NET deaktivieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}

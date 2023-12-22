---
title: Deaktivieren Sie die Kompatibilitätsprüfung in Excel
type: docs
weight: 170
url: /de/net/disable-compatibility-checker-in-excel/
description: In diesem Artikel wird gezeigt, wie Sie die Kompatibilitätsprüfung über Aspose.Cells for .NET API deaktivieren.
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  Deaktivieren Sie die Kompatibilitätsprüfung in Excel-Arbeitsblättern in C#

{{% alert color="primary" %}}

Microsoft Die Flags der Kompatibilitätsprüfung von Excel beim Speichern einer Datei in einem früheren Dateiformat können zu Funktionsproblemen oder Wiedergabetreue führen. Der Kompatibilitätsprüfer ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht die Kompatibilitätsprüfung die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei der Entscheidungsfindung zum Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Es kann auch verwendet werden, um einen Bericht zu allen Problemen in der Arbeitsmappe zu erstellen oder die Funktion zu deaktivieren.

Manchmal müssen Sie die Kompatibilitätsprüfung für eine bestimmte Tabelle deaktivieren. Mit Aspose.Cells'-APIs können Sie dies programmgesteuert tun, damit Benutzer nicht durch das Popup-Dialogfeld „Kompatibilitätsprüfung“ frustriert oder verwirrt werden, wenn sie die Datei in Microsoft Excel manuell erneut speichern.

{{% /alert %}}

##  **So deaktivieren Sie die Kompatibilitätsprüfung mit Microsoft Excel**

So deaktivieren Sie die Kompatibilitätsprüfung in Microsoft Excel (zum Beispiel Microsoft Excel 2007/2010):

-  (Excel 2007) Klicken Sie auf die Office-Schaltfläche**Bereiten Sie vor**, **führen Sie dann die Kompatibilitätsprüfung aus** und deaktivieren Sie dann **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.
-  (Excel 2010) Klicken Sie auf der Registerkarte Datei auf**Info**, dann **Auf Probleme prüfen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie abschließend das Kontrollkästchen **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.

##  **So deaktivieren Sie die Kompatibilitätsprüfung mithilfe der APIs Aspose.Cells**

 Stellen Sie die ein[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) Eigentum zu**FALSCH** um die Kompatibilitätsprüfung von Microsoft Excel zu deaktivieren.

###  **Codebeispiele**

Die folgenden Codebeispiele zeigen, wie Sie die Kompatibilitätsprüfung mit Aspose.Cells for .NET deaktivieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}

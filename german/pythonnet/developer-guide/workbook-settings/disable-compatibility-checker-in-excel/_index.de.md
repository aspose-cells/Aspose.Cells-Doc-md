---
title: Kompatibilitätsprüfung in Excel deaktivieren
type: docs
weight: 170
url: /de/python-net/disable-compatibility-checker-in-excel/
description: Dieser Artikel zeigt, wie man den Kompatibilitätsprüfer über die Aspose.Cells für Python via .NET API deaktiviert.
keywords: Python Deaktivieren des Kompatibilitätsprüfers, Excel Kompatibilitätsprüfer in C#, Deaktivieren des Kompatibilitätsprüfers in Arbeitsmappen. 
---

## Deaktivieren des Kompatibilitätsprüfers in Excel-Worksheet in Python 

{{% alert color="primary" %}}

Microsoft Excels Kompatibilitätsprüfer warnt, wenn das Speichern einer Datei in einem früheren Dateiformat zu Funktionsproblemen oder Qualitätsverlust führen könnte. Der Kompatibilitätsprüfer ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht der Kompatibilitätsprüfer die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei Entscheidungen über den Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Er kann auch verwendet werden, um einen Bericht über Probleme in der Arbeitsmappe zu erstellen oder das Feature zu deaktivieren.

Manchmal müssen Sie den Kompatibilitätsprüfer für eine bestimmte Tabelle deaktivieren. Mit den Aspose.Cells für Python via .NET-APIs können Sie dies programmatisch tun, damit Benutzer nicht durch das Pop-up-Fenster des Kompatibilitätsprüfers verwirrt oder frustriert werden, wenn sie die Datei manuell in Microsoft Excel erneut speichern.

{{% /alert %}}

## **Wie Sie den Kompatibilitätsprüfer in Microsoft Excel deaktivieren**

Um den Kompatibilitätsprüfer in Microsoft Excel zu deaktivieren (z.B. Microsoft Excel 2007/2010):

- (Excel 2007) Klicken Sie auf die Office-Schaltfläche, dann auf **Vorbereiten**, anschließend auf **Kompatibilitätsprüfung ausführen** und deaktivieren Sie die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.
- (Excel 2010) Klicken Sie auf die Registerkarte **Datei**, dann auf **Info**, klicken Sie auf **Nach Problemen suchen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie anschließend die Option **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern**.

## **So deaktivieren Sie den Kompatibilitätsprüfer mithilfe von Aspose.Cells-APIs**

Setzen Sie die [**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility)-Eigenschaft auf **False**, um den Kompatibilitätsprüfer von Microsoft Excel zu deaktivieren.

### **Codebeispiele**

Die folgenden Codebeispiele zeigen, wie man den Kompatibilitätsprüfer mit Aspose.Cells für Python via .NET deaktiviert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

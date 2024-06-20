---
title: Kompatibilitätsprüfung in Excel deaktivieren
type: docs
weight: 270
url: /de/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excels Kompatibilitätsprüfer zeigt an, dass beim Speichern einer Datei in einem früheren Dateiformat das Speichern der Datei möglicherweise Funktionsprobleme oder Qualitätsverlust verursachen könnte. Der Kompatibilitätsprüfer ist ein Feature von Microsoft Office Excel 2007, 2010 & 2013.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht der Kompatibilitätsprüfer die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei Entscheidungen über den Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Er kann auch verwendet werden, um einen Bericht über Probleme in der Arbeitsmappe zu erstellen oder das Feature zu deaktivieren.

Manchmal müssen Sie den Kompatibilitätsprüfer für eine bestimmte Tabelle deaktivieren. Mit den APIs von Aspose.Cells können Sie dies dynamisch tun, damit die Benutzer nicht durch das Dialogfeld des Kompatibilitätsprüfers frustriert oder verwirrt werden, wenn sie die Datei manuell in Microsoft Excel erneut speichern.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um den Kompatibilitätsprüfer in Microsoft Excel zu deaktivieren (z.B. Microsoft Excel 2007/2010):

- (Excel 2007) Klicken Sie auf die Office-Schaltfläche, dann auf **Vorbereiten**, anschließend auf **Kompatibilitätsprüfung ausführen** und deaktivieren Sie die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.
- (Excel 2010 & 2013) Klicken Sie auf der Registerkarte Datei auf **Info**, dann auf **Nach Problemem suchen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie schließlich die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.

## **Verwendung von Aspose.Cells APIs**

Setzen Sie die [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)-Eigenschaft auf **False**, um den Kompatibilitätsprüfer von Microsoft Excel zu deaktivieren.

Angenommen, wir haben eine Vorlagendatei im XLS-Format. Wenn ein Benutzer diese Datei in MS Excel 2007/2010/2013 speichert oder erneut speichert, wird das Dialogfeld des Kompatibilitätsprüfers angezeigt, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Der folgende Code zeigt, wie Sie den Kompatibilitätsprüfer mit Aspose.Cells for Java deaktivieren können.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}

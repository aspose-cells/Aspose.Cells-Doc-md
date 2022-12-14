---
title: Kompatibilitätsprüfung in Excel deaktivieren
type: docs
weight: 270
url: /de/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Die Kompatibilitätsprüfung von Excel weist beim Speichern einer Datei in einem früheren Dateiformat darauf hin, dass das Speichern der Datei zu Funktionsproblemen oder Verlust der Wiedergabetreue führen kann. Die Kompatibilitätsprüfung ist eine Funktion von Microsoft Office Excel 2007, 2010 und 2013.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, aus Excel 2007 oder Excel 2010 speichern, scannt die Kompatibilitätsprüfung die Arbeitsmappe, um festzustellen, ob sie Features enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen zu helfen, Entscheidungen zur Behandlung von Kompatibilitätsproblemen zu treffen, zeigt die Kompatibilitätsprüfung Dialogfelder mit Optionen an. Es kann auch verwendet werden, um einen Bericht zu Problemen in der Arbeitsmappe zu erstellen oder die Funktion zu deaktivieren.

Manchmal müssen Sie die Kompatibilitätsprüfung für eine bestimmte Tabelle deaktivieren. Mit Aspose.Cells'-APIs können Sie dies dynamisch tun, damit die Benutzer nicht frustriert oder verwirrt werden, wenn das Dialogfeld Kompatibilitätsprüfung erscheint, wenn sie die Datei manuell in Microsoft Excel erneut speichern.

{{% /alert %}}

## **Mit Microsoft Excel**

So deaktivieren Sie die Kompatibilitätsprüfung in Microsoft Excel (z. B. Microsoft Excel 2007/2010):

-  (Excel 2007) Klicken Sie auf die Office-Schaltfläche**Vorbereiten** , dann**Führen Sie die Kompatibilitätsprüfung aus** , und löschen Sie dann die**Überprüfen Sie die Kompatibilität, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.
-  (Excel 2010 & 2013) Klicken Sie auf der Registerkarte Datei auf**Die Info** , dann**Auf Probleme prüfen** , klicken**Kompatibilität prüfen** , und löschen Sie schließlich die**Überprüfen Sie die Kompatibilität, wenn Sie diese Arbeitsmappe speichern** Möglichkeit.

## **Verwenden von Aspose.Cells-APIs**

 Stellen Sie die ein[**WorkbookSettings.CheckComptilibility**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) Eigentum zu**FALSCH** um die Kompatibilitätsprüfung von Microsoft Excel zu deaktivieren.

Angenommen, wir haben eine XLS-Vorlagendatei. Wenn ein Benutzer es in MS Excel 2007/2010/2013 speichert oder erneut speichert, wird das Dialogfeld Kompatibilitätsprüfung angezeigt, wie im folgenden Screenshot gezeigt.

![todo: Bild_alt_Text](disable-compatibility-checker-in-excel_1.png)

Der folgende Code zeigt, wie die Kompatibilitätsprüfung mit Aspose.Cells for Java deaktiviert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}

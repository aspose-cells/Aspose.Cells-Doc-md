---
title: Warnungen beim Laden einer Excel Datei erhalten
type: docs
weight: 60
url: /de/java/get-warnings-while-loading-excel-file/
---

## **Mögliche Verwendungsszenarien**

Manchmal versucht der Benutzer, die Arbeitsmappe zu laden, die etwas beschädigt, aber ladbar ist. In einem solchen Fall gibt Aspose.Cells beim Laden der Arbeitsmappe Warnungen aus. Sie können diese Warnungen einfangen, indem Sie die Schnittstelle [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) implementieren und die Eigenschaft [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback) festlegen.

## **Warnungen beim Laden von Excel-Dateien erhalten**

Der folgende Beispielcode zeigt, wie Sie Warnungen beim Laden einer Excel-Datei erhalten. Der Code lädt die [beispielhafte Excel-Datei](sampleDuplicateDefinedName.xlsx), die beim Laden eine [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) Warnung auslöst. Diese Warnung wird dann von der Methode [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) eingefangen, die die Warnmeldungen in der Konsole ausgibt. Der Code speichert dann die Arbeitsmappe als [Ausgabe-Excel-Datei](outputDuplicateDefinedName.xlsx). Wenn Sie die beispielhafte Excel-Datei in Microsoft Excel öffnen, wird Ihnen diese Warnung ebenfalls angezeigt, wie im Screenshot gezeigt. Bitte überprüfen Sie auch die Konsolenausgabe des unten stehenden Codes für ein besseres Verständnis.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Codes bei Ausführung mit der bereitgestellten [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}

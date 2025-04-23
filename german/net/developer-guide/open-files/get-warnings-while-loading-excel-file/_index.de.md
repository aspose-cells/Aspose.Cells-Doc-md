---
title: Warnungen beim Laden einer Excel Datei erhalten
type: docs
weight: 110
url: /de/net/get-warnings-while-loading-excel-file/
---

## **Mögliche Verwendungsszenarien**

Manchmal versucht der Benutzer, die Arbeitsmappe zu laden, die etwas beschädigt, aber ladbar ist. In einem solchen Fall gibt Aspose.Cells beim Laden der Arbeitsmappe Warnungen aus. Sie können diese Warnungen einfangen, indem Sie die Schnittstelle [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) implementieren und die Eigenschaft [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback) festlegen.

## **Warnungen beim Laden von Excel-Dateien erhalten**

Der folgende Beispielcode zeigt, wie Sie Warnungen beim Laden einer Excel-Datei erhalten. Der Code lädt die [beispielhafte Excel-Datei](sampleDuplicateDefinedName.xlsx), die beim Laden eine [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) Warnung auslöst. Diese Warnung wird dann von der Methode [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) eingefangen, die die Warnmeldungen in der Konsole ausgibt. Der Code speichert dann die Arbeitsmappe als [Ausgabe-Excel-Datei](outputDuplicateDefinedName.xlsx). Wenn Sie die beispielhafte Excel-Datei in Microsoft Excel öffnen, wird Ihnen diese Warnung ebenfalls angezeigt, wie im Screenshot gezeigt. Bitte überprüfen Sie auch die Konsolenausgabe des unten stehenden Codes für ein besseres Verständnis.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Codes bei Ausführung mit der bereitgestellten [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

---
title: Erhalten Sie Warnungen beim Laden einer Excel-Datei
type: docs
weight: 110
url: /de/net/get-warnings-while-loading-excel-file/
---
## **Mögliche Nutzungsszenarien**

Manchmal versucht der Benutzer, die Arbeitsmappe zu laden, die etwas beschädigt, aber ladbar ist. In diesem Fall gibt Aspose.Cells beim Laden der Arbeitsmappe Warnungen aus. Sie können diese Warnungen abfangen, indem Sie die implementieren**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** Schnittstelle und Einstellung**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**Eigentum.

## **Erhalten Sie Warnungen beim Laden einer Excel-Datei**

 Der folgende Beispielcode erläutert, wie Warnungen beim Laden einer Excel-Datei angezeigt werden. Der Code lädt die[Excel-Beispieldatei](sampleDuplicateDefinedName.xlsx) der wirft**[DuplicateDefinedName](https://reference.aspose.com/cells/net/aspose.cells/warningtype)** Warnung beim Laden. Diese Warnung wird dann abgefangen**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** Methode, die die Warnmeldungen auf der Konsole ausgibt. Der Code speichert dann die Arbeitsmappe als[Excel-Datei ausgeben](outputDuplicateDefinedName.xlsx)Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen, wird Ihnen auch diese Warnung angezeigt, wie in diesem Screenshot gezeigt. Bitte überprüfen Sie zum besseren Verständnis auch die Konsolenausgabe des unten angegebenen Codes.

![todo: Bild_alt_Text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsolenausgabe**

 Hier ist die Konsolenausgabe des obigen Codes, wenn er mit dem bereitgestellten ausgeführt wird[Excel-Beispieldatei](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}

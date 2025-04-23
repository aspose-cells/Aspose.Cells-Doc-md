---
title: Externe Ressourcen mithilfe von WorkbookSetting.StreamProvider steuern
type: docs
weight: 10
url: /de/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Mögliche Verwendungsszenarien**
Manchmal enthält Ihre Excel-Datei externe Ressourcen wie verknüpfte Bilder usw. Aspose.Cells ermöglicht es Ihnen, diese externen Ressourcen mithilfe von [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) zu steuern, das die Implementierung des [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Interface übernimmt. Wenn Sie versuchen, Ihr Arbeitsblatt mit externen Ressourcen wie verknüpften Bildern zu rendern, werden die Methoden des [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Interfaces aufgerufen, um Ihnen die Möglichkeit zu geben, angemessene Maßnahmen für Ihre externen Ressourcen zu ergreifen.
## **Externe Ressourcen mithilfe von WorkbookSetting.StreamProvider steuern**
Im folgenden Beispielcode wird die Verwendung von [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) erläutert. Es lädt die [Beispiel-Excel-Datei](61767877.xlsx) mit einem verknüpften Bild und ersetzt das verknüpfte Bild durch das [Aspose-Logo](61767874.png). Anschließend rendert der Code das gesamte Blatt mit der [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-Klasse in ein einzelnes Bild. Der folgende Screenshot zeigt die Beispiel-Excel-Datei und ihr [gerendertes Ausgabebild](61767874.png) zur Referenz. Wie Sie sehen können, wurde das defekte verknüpfte Bild durch das Aspose-Logo ersetzt.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
{{< app/cells/assistant language="java" >}}

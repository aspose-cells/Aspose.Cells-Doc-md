---
title: Externe Ressourcen mithilfe von WorkbookSetting.StreamProvider steuern
type: docs
weight: 10
url: /de/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält Ihre Excel-Datei externe Ressourcen wie verknüpfte Bilder usw. Aspose.Cells ermöglicht es Ihnen, diese externen Ressourcen mithilfe von [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider), das die Implementierung des [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)-Interface übernimmt, zu steuern. Immer wenn Sie versuchen, Ihr Arbeitsblatt mit externen Ressourcen wie verknüpften Bildern zu rendern, werden die Methoden des [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)-Interfaces aufgerufen, die es Ihnen ermöglichen, angemessene Maßnahmen für Ihre externen Ressourcen zu ergreifen.

## **Externe Ressourcen mithilfe von WorkbookSetting.StreamProvider steuern**

Der folgende Beispielcode erläutert die Verwendung des [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Er lädt die [Beispiel-Excel-Datei](61767863.xlsx) mit einem verknüpften Bild. Der Code ersetzt das verknüpfte Bild durch das [Aspose-Logo](61767862.png) und rendert das gesamte Blatt in ein einzelnes Bild unter Verwendung der Klasse [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). Der folgende Screenshot zeigt die Beispiel-Excel-Datei und ihr [gerendertes Ausgabe-Bild](61767865.png) zur Referenz. Wie Sie sehen können, wird das defekte verknüpfte Bild durch das Aspose-Logo ersetzt.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

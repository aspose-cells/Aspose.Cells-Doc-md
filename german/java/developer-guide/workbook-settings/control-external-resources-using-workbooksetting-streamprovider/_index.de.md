---
title: Steuern Sie externe Ressourcen mithilfe von WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /de/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Mögliche Nutzungsszenarien**
Manchmal enthält Ihre Excel-Datei externe Ressourcen, z. B. verknüpfte Bilder usw. Mit Aspose.Cells können Sie diese externen Ressourcen steuern[Arbeitsmappe.Einstellungen.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)was die Umsetzung übernimmt[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)Schnittstelle. Wann immer Sie versuchen, Ihr Arbeitsblatt mit externen Ressourcen, z. B. verknüpften Bildern, zu rendern, verwenden Sie die Methoden von[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)wird eine Schnittstelle aufgerufen, die es Ihnen ermöglicht, geeignete Aktionen für Ihre externen Ressourcen durchzuführen.
## **Steuern Sie externe Ressourcen mithilfe von WorkbookSetting.StreamProvider**
Der folgende Beispielcode erläutert die Verwendung von[Arbeitsmappe.Einstellungen.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Es lädt die[Beispiel-Excel-Datei](61767877.xlsx)mit einem verlinkten Bild. Der Code ersetzt das verlinkte Bild durch[Aspose Logo](61767874.png)und rendert das gesamte Blatt in ein einzelnes Bild mit[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)Klasse. Der folgende Screenshot zeigt die Beispiel-Excel-Datei und ihre[gerendertes Ausgabebild](61767874.png)für eine Referenz. Wie Sie sehen können, wird das defekte verlinkte Bild durch das Aspose-Logo ersetzt.

![todo: Bild_alt_Text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}

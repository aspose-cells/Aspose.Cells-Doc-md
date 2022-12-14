---
title: Steuern Sie externe Ressourcen mithilfe von WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /de/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Mögliche Nutzungsszenarien**

Manchmal enthält Ihre Excel-Datei externe Ressourcen, z. B. verknüpfte Bilder usw. Mit Aspose.Cells können Sie diese externen Ressourcen steuern[**Arbeitsmappe.Einstellungen.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)das dauert die Umsetzung der[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)Schnittstelle. Wann immer Sie versuchen, Ihr Arbeitsblatt zu rendern, das externe Ressourcen enthält, z. B. verknüpfte Bilder, verwenden die Methoden der[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)wird eine Schnittstelle aufgerufen, die es Ihnen ermöglicht, geeignete Aktionen für Ihre externen Ressourcen durchzuführen.

## **Steuern Sie externe Ressourcen mithilfe von WorkbookSetting.StreamProvider**

Der folgende Beispielcode erläutert die Verwendung der[**Arbeitsmappe.Einstellungen.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . Es lädt die[Beispiel-Excel-Datei](61767863.xlsx) mit einem verlinkten Bild. Der Code ersetzt das verlinkte Bild durch[Aspose Logo](61767862.png) und rendert das gesamte Blatt in ein einzelnes Bild mit[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) Klasse. Der folgende Screenshot zeigt die Beispiel-Excel-Datei und ihre[gerendertes Ausgabebild](61767865.png) für eine Referenz. Wie Sie sehen können, wird das defekte verlinkte Bild durch das Aspose-Logo ersetzt.

![todo: Bild_alt_Text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}

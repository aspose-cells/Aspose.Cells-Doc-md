---
title: Steuerung des Ladens externer Ressourcen in MS Excel Arbeitsmappe beim Rendern in PDF
type: docs
weight: 40
url: /de/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Ihre Excel-Datei kann externe Ressourcen wie verlinkte Bilder oder Objekte enthalten. Wenn Sie Ihre Excel-Datei in PDF konvertieren, ruft Aspose.Cells diese externen Ressourcen ab und rendert sie in PDF. Manchmal möchten Sie jedoch diese externen Ressourcen nicht laden und darüber hinaus möchten Sie sie manipulieren. Dies können Sie mit [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) tun, das das [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)-Interface implementiert.

## **Steuerung des Ladens externer Ressourcen in MS Excel-Arbeitsmappe beim Rendern in PDF**

Der folgende Beispielcode erklärt, wie [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) genutzt werden kann, um das Laden externer Ressourcen zu steuern und sie zu manipulieren. Bitte überprüfen Sie die im Code verwendete [Beispiel-Excel-Datei](50528322.xlsx) und das vom Code generierte [Ausgabepdf](50528325.pdf). Der [Screenshot](50528326.png) zeigt, wie das [alte externe Bild](50528324.png) in der Beispiel-Excel-Datei durch ein [neues Bild](50528323.png) im Ausgabepdf ersetzt wurde.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}

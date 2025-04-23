---
title: Steuerung des Ladens externer Ressourcen in MS Excel Arbeitsmappe beim Rendern in PDF
type: docs
weight: 40
url: /de/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Ihre Excel-Datei kann externe Ressourcen wie verknüpfte Bilder oder Objekte enthalten. Wenn Sie Ihre Excel-Datei in PDF konvertieren, ruft Aspose.Cells diese externen Ressourcen ab und rendert sie in PDF. Manchmal möchten Sie jedoch diese externen Ressourcen nicht laden und darüber hinaus möchten Sie sie manipulieren. Dies können Sie mit [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) tun, das das [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Interface implementiert.

## **Steuerung des Ladens externer Ressourcen in MS Excel-Arbeitsmappe beim Rendern in PDF**

Der folgende Beispielcode erläutert, wie man [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) verwendet, um das Laden externer Ressourcen zu steuern und sie zu manipulieren. Bitte prüfen Sie die im Code verwendete [Beispiel-Excel-Datei](50528353.xlsx) und das generierte [Ausgabe-PDF](50528354.pdf). Das [Screenshot](50528357.png) zeigt, wie das [alte externe Bild](50528356.png) in der Beispiel-Excel-Datei durch ein [neues Bild](50528355.png) im Ausgabe-PDF ersetzt wurde.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}

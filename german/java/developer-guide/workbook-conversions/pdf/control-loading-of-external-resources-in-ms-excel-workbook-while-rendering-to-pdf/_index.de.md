---
title: Steuern Sie das Laden externer Ressourcen in der MS Excel-Arbeitsmappe, während Sie auf PDF rendern
type: docs
weight: 40
url: /de/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Mögliche Nutzungsszenarien**

Ihre Excel-Datei kann externe Ressourcen enthalten, zB verlinkte Bilder oder Objekte. Wenn Sie Ihre Excel-Datei in PDF konvertieren, ruft Aspose.Cells diese externen Ressourcen ab und rendert sie in PDF. Aber manchmal möchten Sie diese externen Ressourcen nicht laden und darüber hinaus möchten Sie sie manipulieren. Sie können dies mit tun[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)die die implementiert[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)Schnittstelle.

## **Steuern Sie das Laden externer Ressourcen in der MS Excel-Arbeitsmappe, während Sie auf PDF rendern**

Der folgende Beispielcode erläutert die Verwendung von[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)um das Laden externer Ressourcen zu steuern und zu manipulieren. Bitte überprüfen Sie die[Beispiel-Excel-Datei](50528353.xlsx)innerhalb des Codes und der verwendet[Ausgang PDF](50528354.pdf)vom Code generiert. Das[Bildschirmfoto](50528357.png)zeigt, wie die[altes Außenbild](50528356.png)in der Beispiel-Excel-Datei wurde durch a ersetzt[neues Bild](50528355.png)in der Ausgabe PDF.

![todo: Bild_alt_Text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}

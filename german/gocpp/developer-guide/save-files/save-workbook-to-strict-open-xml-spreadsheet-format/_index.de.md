---
title: Arbeitsmappe im strengen Open XML Spreadsheet Format speichern mit Golang über C++
linktitle: Arbeitsmappe im strengen Open XML Tabellenformat speichern
type: docs
weight: 150
url: /de/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Lernen Sie, wie Sie eine Arbeitsmappe im Strict Open XML Spreadsheet Format mit Aspose.Cells for C++ speichern.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Arbeitsmappe im *Strict Open XML Spreadsheet*-Format zu speichern. Dafür bietet es die [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/)-Eigenschaft. Wenn Sie ihren Wert auf [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) setzen, wird die Ausgabedatei im Strict Open XML Spreadsheet-Format gespeichert.

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**

Das folgende Beispiel erstellt eine Arbeitsmappe, setzt die [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/)-Eigenschaft auf [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) und speichert sie als [Ausgabedatei](67338272.xlsx). Wenn Sie die Ausgabedatei in Microsoft Excel öffnen und den „Speichern unter“-Dialog öffnen, sehen Sie das Format als *Strict Open XML Spreadsheet*, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}

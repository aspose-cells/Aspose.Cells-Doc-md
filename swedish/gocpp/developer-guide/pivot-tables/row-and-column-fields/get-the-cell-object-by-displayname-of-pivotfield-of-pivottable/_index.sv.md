---
title: Hämta cellobjektet efter displaynamnet för PivotField i PivotTable med Golang via C++
linktitle: Hämta cellobjektet genom visningsnamn för PivotField i PivotTable
type: docs
weight: 70
url: /sv/go-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Lär dig hur du hämtar cellobjektet via visningsnamnet för ett pivotelement och tillämpar formatering med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller metoden [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/go-cpp/pivottable/getcellbydisplayname/), vilken du kan använda för att komma åt cellobjektet via visningsnamnet för ett pivotelement. Denna metod är användbar när du vill markera eller formatera din pivothuvud. Denna artikel förklarar hur man hämtar cellobjektet via visningsnamnet för ett datafält och sedan tillämpar formatering på det.

{{% /alert %}}

## **Hämta cellobjektet genom visningsnamn för PivotField i PivotTable**

Följande kod får den första pivot-tabellen i kalkbladet och hämtar sedan cellen genom visningsnamnet för det andra datafältets pivot-tabell. Den ändrar sedan fyllnadsfärgen och teckensnittsfärgen till ljusblå respektive svart. Nedan visas skärmbilder på hur pivot-tabellen ser ut före och efter kodens körning.

|**Pivot-tabel - Före**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetTheCellObjectByDisplaynameOfPivotfieldOfPivottable.go" >}}
|**Pivot-tabel - Efter**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|

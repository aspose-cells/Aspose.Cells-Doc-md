---
title: Range mit externen Verknüpfungen mit Node.js über C++ abrufen
linktitle: Bereich mit externen Links abrufen
type: docs
weight: 120
url: /de/nodejs-cpp/get-range-with-external-links/
description: Erfahren Sie, wie man mit Aspose.Cells for Node.js via C++ Bereiche mit externen Verknüpfungen erhält. Daten aus verschiedenen Excel Dateien effizient abrufen.
---

## **Bereich mit externen Links abrufen**

Viele Excel-Dateien greifen auf Daten aus anderen Excel-Dateien mit externen Verknüpfungen zu. Aspose.Cells for Node.js via C++ bietet die Möglichkeit, diese externen Verknüpfungen über die [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)-Methode abzurufen. Die [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)-Methode gibt ein Array vom Typ [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) zurück. Die [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea)-Klasse bietet eine [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--)-Eigenschaft, die den Namen der externen Datei zurückgibt. Die [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea)-Klasse enthält die folgenden Mitglieder.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): Die Endspalte des Bereichs
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): Die Endzeile des Bereichs
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Holt den Namen der externen Datei, falls dies eine externe Referenz ist
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Gibt an, ob dies ein Bereich ist
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Gibt an, ob dies eine externe Verknüpfung ist
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Gibt an, in welchem Blatt sich diese Referenz befindet
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): Der Anfangsspalte des Bereichs
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): Die Startzeile des Bereichs

Der nachstehende Beispielcode zeigt die Verwendung der [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)-Methode, um Bereiche mit externen Verknüpfungen zu erhalten.

## **Beispielcode**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```

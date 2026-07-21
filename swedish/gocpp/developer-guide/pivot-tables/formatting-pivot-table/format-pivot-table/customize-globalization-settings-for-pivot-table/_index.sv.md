---
title: Anpassa globaliseringsinställningar för pivottabell med Golang via C++
linktitle: Anpassa globaliseringsinställningarna för Pivot tabell
type: docs
weight: 50
url: /sv/go-cpp/customize-globalization-settings-for-pivot-table/
description: Lär dig hur man anpassar globaliseringsinställningar för pivot tabeller med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland vill du anpassa texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* efter dina behov. Aspose.Cells for C++ låter dig anpassa globaliseringsinställningarna för pivot-tabellen för att hantera sådana scenarier. Du kan också använda denna funktion för att ändra etiketter till andra språk som arabiska, hindi, polska m.m.

## **Anpassa globaliseringsinställningarna för Pivot-tabell**

 Följande kodexempel förklarar hur man anpassar globaliseringsinställningar för pivot-tabellen i C++. Den skapar en klass *CustomPivotTableGlobalizationSettings* som är härledd från basklassen [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) och åsidosätter alla nödvändiga metoder. Dessa metoder returnerar anpassad text för olika element i pivot-tabellen. Koden tilldelar sedan denna implementation till egenskapen [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). Exemplet laddar en [käll-Excel fil](40468488.xlsx), uppdaterar pivot-data och sparar den som [utdata PDF](40468487.pdf). Nedan visas en skärmbild på anpassade etiketter i utgången.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}

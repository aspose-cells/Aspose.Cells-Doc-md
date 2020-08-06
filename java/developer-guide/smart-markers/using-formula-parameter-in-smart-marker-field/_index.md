---
title: Using Formula parameter in Smart Marker field
type: docs
weight: 30
url: /java/using-formula-parameter-in-smart-marker-field/
---

## **Possible Usage Scenarios**
Sometimes, you want to embed formula in the smart marker field. This article describes how to make use of Formula parameter to embed formula in smart marker field.
## **Using Formula parameter in Smart Marker field**
The following sample code embeds the formula in the smart marker variable named Test and its data source name is also Test, so the complete field with formula parameter looks like **&=$Test(formula)** and after the execution of the code, the [final output Excel file](attachments/46858371/47153156.xlsx) will have formulas in cells from A1 till A5.
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
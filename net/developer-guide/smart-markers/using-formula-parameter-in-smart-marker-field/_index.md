---
title: Using Formula parameter in Smart Marker field
type: docs
weight: 40
url: /net/using-formula-parameter-in-smart-marker-field/
---


## **Possible Usage Scenarios**
Sometimes, you want to embed formula in the smart marker field. This article describes how to make use of the *Formula* parameter to embed formula in the smart marker field.
## **Using Formula parameter in Smart Marker field**
The following sample code embeds the formula in the smart marker field named TestFormula and its data source name is MyDataSource, so the complete field with formula parameter looks like &=MyDataSource.TestFormula(formula) and after the execution of the code, the [final output Excel file](46465047.xlsx) will have formulas in cells from A1 till A5.
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}

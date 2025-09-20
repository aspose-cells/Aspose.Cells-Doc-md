---
title: Extract Text from the Gear Type SmartArt Shape with Golang via C++
linktitle: Extract Text from the Gear Type SmartArt Shape
type: docs
weight: 500
url: /go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Learn how to extract text from Gear Type SmartArt shapes in Excel using Aspose.Cells for C++ with step-by-step guidance and code examples.
---

## **Possible Usage Scenarios**

Aspose.Cells for C++ can extract text from the Gear Type SmartArt Shape. To achieve this, follow these steps:
1. Convert SmartArt Shape to Group Shape using the [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/) method.
2. Retrieve all individual shapes forming the Group Shape using the [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/) method.
3. Iterate through each individual shape and extract text using the [**GetText()**](https://reference.aspose.com/cells/go-cpp/) method.

## **Extract Text from the Gear Type SmartArt Shape**

The following sample code loads a [sample Excel file](67338483.xlsx) containing a Gear Type SmartArt Shape and extracts text from its individual shapes. Refer to the console output below for results.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Console Output**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
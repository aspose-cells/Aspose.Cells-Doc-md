---
title: Access and Modify the Display Label of the Linked Ole Object with Golang via C++
linktitle: Access and Modify the Display Label of the Linked Ole Object
type: docs
weight: 100
url: /go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Learn how to access and modify the display label of linked Ole Objects in Excel files using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to change the display label of the Ole Object as shown in the following screenshot. You can also access or modify the display label of the Ole object using Aspose.Cells APIs with the [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) and [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) methods.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Access and Modify the Display Label of the Linked Ole Object**

Please see the following sample code, it loads the [sample Excel file](64716810.xlsx) that contains the Ole Object. The code accesses the Ole Object and changes its Label from Sample APIs to Aspose APIs. Please see the console output given below that shows the effect of the sample code on the sample Excel file for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}
## **Console Output**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
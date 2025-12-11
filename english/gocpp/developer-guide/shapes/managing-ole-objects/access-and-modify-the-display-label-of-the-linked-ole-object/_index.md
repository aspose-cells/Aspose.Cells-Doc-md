---
title: Access and Modify the Display Label of the Linked OLE Object with Golang via C++
linktitle: Access and Modify the Display Label of the Linked OLE Object
type: docs
weight: 100
url: /go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Learn how to access and modify the display label of linked OLE objects in Excel files using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to change the display label of the OLE object as shown in the following screenshot. You can also access or modify the display label of the OLE object using Aspose.Cells APIs with the [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) and [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) methods.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Access and Modify the Display Label of the Linked OLE Object**

Please see the following sample code; it loads the [sample Excel file](64716810.xlsx) that contains the OLE object. The code accesses the OLE object and changes its Label from Sample APIs to Aspose APIs. Please see the console output given below, which shows the effect of the sample code on the sample Excel file for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}

## **Console Output**

{{< highlight go >}}
Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs
{{< /highlight >}}
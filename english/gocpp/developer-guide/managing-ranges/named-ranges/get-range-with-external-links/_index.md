---
title: Get Range with External Links with Golang via C++
linktitle: Get Range with External Links
type: docs
weight: 120
url: /go-cpp/get-range-with-external-links/
description: Learn how to retrieve ranges with external links in Excel files using Aspose.Cells with Golang via C++.
---

## **Get Range with External Links**

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells provides the option to retrieve these external links by using the [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) method. The [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). The [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) class provides an [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) class exposes the following members.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): The end column of the area
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): The end row of the area
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Get the external file name if this is an external reference
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Indicates whether this is an area
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Indicates whether this is an external link
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Indicates which sheet this reference is in
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): The start column of the area
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): The start row of the area

The sample code given below demonstrates the use of [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) method to get Ranges with external links.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
---
title: Get Range with External Links
type: docs
weight: 120
url: /python-net/get-range-with-external-links/
description: This article shows how to Get Range with External Links by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get Range with External Links.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Range with External Links**

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells for Python via .NET provides the option to retrieve these external links by using the [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) method. The [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). The [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) class provides an [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) class exposes the following members.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): The end column of the area
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): The end row of the area
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Get the external file name if this is an external reference
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Indicates whether this is an area
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Indicates whether this is an external link
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Indicates which sheet this reference is in
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): The start column of the area
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): The start row of the area

The sample code given below demonstrates the use of [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) method to get Ranges with external links.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

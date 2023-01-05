---
title: Get Range with External Links
type: docs
weight: 60
url: /python-java/get-range-with-external-links/
---

## **Get Range with External Links**
There are many instances where excel files access data from other excel files by the use of external links. Aspose.Cells for Python via Java provides the option to retrieve these external links by using the [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) method. The [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) method returns an array of type [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). The [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) class provides an [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) property that returns the name of the external file.

The following code snippet shows how to get external links.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}

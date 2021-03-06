---
title: Get Range with External Links
type: docs
weight: 60
url: /pythonjava/get-range-with-external-links/
---

## **Get Range with External Links**
There are many instances where excel files access data from other excel files by the use of external links. Aspose.Cells for Python via Java provides the option to retrieve these external links by using the [Name.GetReferredAreas](https://apireference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) method. The [Name.GetReferredAreas](https://apireference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) method returns an array of type [ReferredArea](https://apireference.aspose.com/cells/python/asposecells.api/ReferredArea). The [ReferredArea](https://apireference.aspose.com/cells/python/asposecells.api/ReferredArea) class provides an [ExternalFileName](https://apireference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) property that returns the name of the external file.

The following code snippet shows how to get external links.

{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "Worksheets-GetRangeWithExternalLinks.py" >}}

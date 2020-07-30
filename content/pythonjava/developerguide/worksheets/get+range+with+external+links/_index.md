---
title : "Get Range with External Links" 
description : "" 
weight : 12019 
toc : false
type: docs
url: /pythonjava/developerguide/worksheets/get+range+with+external+links/
---

# Aspose.Cells for Python via Java : Get Range with External Links


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Get Range with External Links](#get-range-with-external-links)
{{< /panel >}}
 

 

## Get Range with External Links

There are many instances where excel files access data from other excel files by the use of external links. Aspose.Cells for Python via Java provides the option to retrieve these external links by using the [Name.GetReferredAreas](https://apireference.aspose.com/cells/python/asposecells.api/name#getReferredAreas(boolean)) method. The [Name.GetReferredAreas](https://apireference.aspose.com/cells/python/asposecells.api/name#getReferredAreas(boolean)) method returns an array of type [ReferredArea](https://apireference.aspose.com/cells/python/asposecells.api/ReferredArea). The [ReferredArea](https://apireference.aspose.com/cells/python/asposecells.api/ReferredArea)class provides an [ExternalFileName](https://apireference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) property that returns the name of the external file.

The following code snippet shows how to get external links.


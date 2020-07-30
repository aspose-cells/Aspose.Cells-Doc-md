---
title : "Determining if the License is loaded successfully" 
description : "" 
weight : 20447 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/determining+if+the+license+is+loaded+successfully/
---

# Aspose.Cells for .NET : Determining if the License is loaded successfully


Aspose.Cells provides [Workbook.IsLicensed](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/islicensed) property which you can use to determine if the license is loaded successfully or not. If you access this property before setting the license, it will return **false** and if you will call this property after setting the license, it will return **true** indicating that license has been loaded successfully.

The following code accesses the [Workbook.IsLicensed](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/islicensed) property before setting a license and it returns **false**. Then it loads the license and accesses the property again which now returns **true**.

## Console Output

Here is the console (debug) output of the above sample code

{{< code lang="cs" >}}
False
True
{{< /code >}}


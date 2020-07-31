---
title : "Check Version Number" 
description : "" 
weight : 12058 
toc : false
type: docs
url: /net/developerguide/introduction/check+version+number/
---

# Aspose.Cells for .NET : Check Version Number


Wonder which version of Aspose.Cells you are using? We publish new versions of Aspose.Cells, both to introduce new features and to fix issues, on a regular basis. The version number consists of major and minor version numbers, build and revision number. The major and minor version numbers are required; the build and revision versions are optional. Each number must be an integer from 0 up. The format is as follows (optional components are shown in square brackets ('\[' and '\]'):

`major.minor[.build[.revision]]`

When we release a new build of Aspose.Cells, we update the version number.

This article explains how to check which version of Aspose.Cells is installed on the system manually and using the Aspose.Cells API.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Check Version Number Manually](#check-version-number-manually)
*   2 [Check Version Number Using the Aspose.Cells API](#check-version-number-using-the-aspose.cells-api)
{{< /panel >}}
 

 

## Check Version Number Manually

To find out which version of Aspose.Cells you are using manually:

1.  Right-click the Aspose.Cells.dll file and select **Properties**.
2.  Click the Version (or Details) tab to check the version number.

## Check Version Number Using the Aspose.Cells API

To find out which version of Aspose.Cells you are using through the API, use the [`CellsHelper`](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.CellsHelper+Class&linkCreation=true&fromPageId=5018377) class `GetVersion` static method to get Aspose.Cell's version number.


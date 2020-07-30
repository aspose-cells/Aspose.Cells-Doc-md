---
title : "Setting Formula for Named Range" 
description : "" 
weight : 12210 
toc : false
type: docs
url: /net/developerguide/data/setting+formula+for+named+range/
---

# Aspose.Cells for .NET : Setting Formula for Named Range


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Formula for Named Range](#setting-formula-for-named-range)
    *   1.1 [Setting a Simple Formula for Named Range](#setting-a-simple-formula-for-named-range)
    *   1.2 [Setting a Complex Formula for Named Range](#setting-a-complex-formula-for-named-range)
{{< /panel >}}
 

## Setting Formula for Named Range

Like Excel application, Aspose.Cells APIs provide the ability to specify a formula for a named range while using its [RefersTo](https://apireference.aspose.com/cells/net/aspose.cells/range/properties/refersto) property. There could be numerous usability scenarios for this feature, a few of which are detailed as follow.

### Setting a Simple Formula for Named Range

A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.

### Setting a Complex Formula for Named Range

A complex formula could be anything such as a dynamic range or a formula spanning over multiple cells in different worksheets. The following example creates a dynamic range using the INDEX function to get the value from a list based on its location.

Here is another example that uses a named range to sum values from 2 cells in different worksheets.


---
title : "Access and Modify Cell Values" 
description : "" 
weight : 16711 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebcells/access+and+modify+cell+values/
---

# Aspose.Cells for .NET : Access and Modify Cell Values


[Access Worksheet Cells](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebcells/access+worksheet+cells) discussed accessing cells. This topic extends that discussion to show how to access and modify cell values using the Aspose.Cells.GridWeb API.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing & Modifying a Cell's Value](#accessing-&-modifying-a-cell's-value)
    *   1.1 [String Values](#string-values)
    *   1.2 [All Types of Values](#all-types-of-values)
{{< /panel >}}
 

## Accessing & Modifying a Cell's Value

### String Values

Before accessing and modifying the value of a cell, you need to know how to access cells. For details about the different approaches for accessing cells, refer to [Access Worksheet Cells](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebcells/access+worksheet+cells).

Each cell has a property named `StringValue`. Once a cell is accessed, developers can use the `StringValue` property to access the cells string value. To modify cell values, a special method `PutValue` is provided, which can be used to update the cell's string value.

### All Types of Values

`PutValue` method of a cell's object has 8 overloads available which can be used to modify any type of value (Boolean, int, double, DateTime and string) in a cell.

There is also an overloaded version of the `PutValue` method that can take any kind of value in string format and convert it to a proper data type automatically. To make it happen, pass the Boolean value `true` to another parameter of the `PutValue` method as shown below in the example.


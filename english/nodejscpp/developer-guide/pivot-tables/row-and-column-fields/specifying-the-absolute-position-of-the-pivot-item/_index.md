---
title: Specifying the Absolute Position of the Pivot Item
type: docs
weight: 50
url: /nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, a user needs to specify the absolute position of the pivot items. Aspose.Cells for Node.js via C++ API has exposed a few new properties and a method to **meet the user's requirements**.

- Added the **PivotItem.setPosition** property, which can be used to specify the position index among all the PivotItems regardless of the parent node. Added the **PivotItem.setPositionInSameParentNode** property, which can be used to specify the position index among the PivotItems under the same parent node.  
- Added the **PivotItem.move** method in order to move the item up or down based on the count value, where **count** is the number of **positions** to move the PivotItem up or down. If the count value is less than zero, the item will be moved up, **whereas** if the count value is larger than zero, the PivotItem will move down. The Boolean‑type **isSameParent** parameter **specifies** whether the moving operation has to be performed in the same parent node or not.  
- The *PivotItem.move(int count)* method **is obsolete**; therefore, it is suggested to use the newly added method **PivotItem.move(number, boolean)** instead.

{{% /alert %}}

The following sample code creates a Pivot Table and then **specifies the Pivot Items'** positions in the same parent node. You can download the [source Excel](5112632.xlsx) and [output Excel](5112619.xlsx) files for your reference. If you open the output Excel file, you will see that the Pivot Item **"4H12"** is at the **0th** position in parent **"K11"**, and **"DIF400"** is at the **3rd** position. Similarly, **CA32** is at position **1** and **AAA3** is at position **2**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Please note, it is necessary to call the **PivotTable.RefreshData** and **PivotTable.CalculateData** methods before using **PivotItem.setPosition**, **PivotItem.setPositionInSameParentNode** properties and **PivotItem.move** method.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}

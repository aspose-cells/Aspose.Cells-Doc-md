---
title: Access Hyperlink object of the GridWeb Cell
type: docs
weight: 60
url: /java/access-hyperlink-object-of-the-gridweb-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
You can check if a cell contains a hyperlink or not using the following two methods. These methods will return **null** if the cell does not contain a hyperlink, and if it contains a hyperlink, they will return a **GridHyperlink** object.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row, int column)

## **Open Hyperlink in New or Existing Window**
If your Excel file contains a hyperlink that links to a URL like <http://www.aspose.com/> and you load it in GridWeb, the hyperlinks will be rendered with the **target** attribute set to `_blank`. This means that when you click the hyperlink in a GridWeb cell, it will open in a new window instead of the current window. Alternatively, if you want to open the hyperlink in the existing window, set **GridHyperlink.Target** to `_self`.

## **Access Hyperlink object of the GridWeb Cell**
The following sample code accesses the hyperlink of cell **A1**. If cell **A1** contains a hyperlink, it will return a **GridHyperlink** object; otherwise, it will return **null**.

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

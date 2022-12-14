---
title: Manage Comments in Worksheet
type: docs
weight: 110
url: /net/manage-comments-in-worksheet/
---

{{% alert color="primary" %}} 

This topic discusses adding, accessing and removing comments from worksheets. Comments are useful for adding notes or useful information for users who will work with the sheet. Developers have the flexibility to add comments to any cell of the worksheet.

{{% /alert %}} 
## **Working with Comments**
### **Adding Comments**
To add a comment to worksheet, please follow the steps below:

1. Add the Aspose.Cells.GridWeb control to the Web Form.
1. Access the worksheet you're adding comments to.
1. Add a comment to a cell.
1. Set a note for the new comment.

**A comment has been added to the worksheet** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Accessing Comments**
To access a comment:

1. Access the cell that contains the comment.
1. Get the cell's reference.
1. Pass the reference to the Comment collection's to access the comment.
1. It's now possible to modify the comment's properties.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Removing Comments**
To remove a comment:

1. Access the cell as explained above.
1. Use the Comment collection's RemoveAt method to remove the comment.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}

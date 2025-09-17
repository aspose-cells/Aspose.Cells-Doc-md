##Managing Comments in a Worksheet
This article introduces how to work with comment in GridDesktop.
In MS Excel, you must be familiar with the comments feature that allows users to add comments to cells. This feature is helpful in those cases when it is required to provide some information to the users when they are about to enter values into the cells. Whenever a user places his mouse cursor on a commented cell, a small popup message is appeared to provide some information to the user. Using Aspose.Cells.GridDesktop, developers can create comments on cells. In this topic, we will explain the usage of this feature in detail.
## **Adding Comments**
To add a comment to a cell using Aspose.Cells.GridDesktop, please follow the steps below:
- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Comment** to the worksheet by specifying the cell (using its name or row & column number) in which the comment would be added.
The code below will add comments to the **b2** and **b4** cells of the worksheet.
**Comments** collection in the **Worksheet** object provides an overloaded **Add** method. Developers can use any overloaded version of **Add** method according to their specific needs.
## **Accessing Comments**
To access and modify an existing comment in the worksheet, developers can access the comment from the **Comments** collection of the **Worksheet** by specifying the cell (using cell name or its location in terms of row and column number) in which the comment is inserted. Once the comment is accessed, developers can modify its Text at runtime.
## **Removing Comments**
To remove an existing comment, developers can simply access a desired worksheet and then **Remove** comment from the **Comments** collection of the **Worksheet** by specifying the cell (using its name or row & column number) containing comment.

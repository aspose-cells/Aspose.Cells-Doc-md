---
title: Threaded Comments
type: docs
weight: 140
url: /net/threaded-comments/
---

# **Threaded Comments**
MS Excel 365 provides a feature to add threaded comments. These comments work as conversations and can be used for discussions. The comments now come with a Reply box that allows for threaded conversations. The old comments are called Notes in Excel 365. The screenshot below shows how threaded comments are displayed when opened in Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Threaded comments are shown like this in older versions of Excel. The following images have been taken by opening the sample file in Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



Aspose.Cells also provides the feature to manage threaded comments. 
## **Add Threaded Comments**
### **Add Threaded comment with Excel**
To add threaded comments in Excel 365, follow the following steps.

- Method 1
  - Click the **Review** Tab
  - Click the **New Comment** button
  - This will open a dialogue to enter comments in the active cell.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Method 2
  - Right click on the cell where you want to insert the comment.
  - Click the **New Comment** option.
  - This will open a dialogue to enter comments in the active cell.
  - ![todo:image_alt_text](threaded-comments_5)
### **Add Threaded Comment using Aspose.Cells**
Aspose.Cells provides [Comments.AddThreadedComment](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/addthreadedcomment/methods/1) method to add threaded comments.The [Comments.AddThreadedComment](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/addthreadedcomment/methods/1) method accepts the following three parameters.

- Cell Name: The name of the cell where the comment will be inserted.
- Comment Text: The text of the comment.
- [ThreadedCommentAuthor](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentauthor): The author of the comment

The following code sample demonstrates the use of [Comments.AddThreadedComment](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/addthreadedcomment/methods/1) method to add threaded Comment to cell A1. Please see the [output Excel file ](attachments/89686042/89849859.xlsx)generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}
## **Read Threaded Comments**
### **Read Threaded comments with Excel**
To read threaded comments in Excel, simply hover your mouse over the cell containing comments to view the comments. The comments view will look like the view in the following image.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Read Threaded comments using Aspose.Cells**
Aspose.Cells provides [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method to retrieve threaded comments for the specified column. [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method accepts the column name as a parameter and returns the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection). You can iterate over the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection) to view the comments.

The following example demonstrates reading comments from column A1 by loading the [sample Excel File](attachments/89686042/89849861.xlsx). Please see the console output generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}
#### **Console Output**
Comment: Test Threaded Comment

Author: Aspose Test
### **Read Created Time of threaded comments**
Aspose.Cells provides [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method to retrieve threaded comments for the specified column. [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method accepts the column name as a parameter and returns the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection). You can iterate over the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection) and use the [ThreadedComment.CreatedTime](https://apireference.aspose.com/net/cells/aspose.cells/threadedcomment/properties/createdtime) property. 

The following example demonstrates reading the created time of threaded comments by loading the [sample Excel File](attachments/89686042/89849861.xlsx). Please see the console output generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}
#### **Console Output**
Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM
## **Edit Threaded Comments**
### **Edit Threaded comment with Excel**
To edit a threaded comment in Excel, click the **Edit** link on the comment as shown in the following image.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Edit Threaded comment using Aspose.Cells**
Aspose.Cells provides [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method to retrieve threaded comments for the specified column. [Comments.GetThreadedComments](https://apireference.aspose.com/net/cells/aspose.cells.commentcollection/getthreadedcomments/methods/1) method accepts the column name as a parameter and returns the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection). You can update the required comment in the [ThreadedCommentCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentcollection) and save the workbook.

The following example demonstrates editing the first threaded comment in column A1 by loading the [sample Excel File](attachments/89686042/89849861.xlsx). Please see the [output Excel file](attachments/89686042/89849862.xlsx) generated by the code showing the updated comment for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}
## **Remove Threaded Comments**
### **Remove Threaded comments with Excel**
To remove threaded comments in Excel, right click on the cell containing the comments and click the **Delete Comment** option as shown in the following image.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Remove Threaded comments using Aspose.Cells**
Aspose.Cells provides [Comments.RemoveAt](https://apireference.aspose.com/net/cells/aspose.cells/commentcollection/methods/removeat/index) method to remove comments for the specified column. [Comments.RemoveAt](https://apireference.aspose.com/net/cells/aspose.cells/commentcollection/methods/removeat/index) method accepts the column name as a parameter removes the comments in that column. 

The following example demonstrates removing comments in column A1 by loading the [sample Excel File](attachments/89686042/89849861.xlsx). Please see the [output Excel file](attachments/89686042/89849864.xlsx) generated by the code for reference.
#### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}} 

Please note that by removing comment with Aspose.Cells, the author is not removed automatically. If you need to remove the author as well, please use the RemoveAt method of [ThreadedCommentAuthorCollection](https://apireference.aspose.com/net/cells/aspose.cells/threadedcommentauthorcollection) class as shown in the example above.

{{% /alert %}}
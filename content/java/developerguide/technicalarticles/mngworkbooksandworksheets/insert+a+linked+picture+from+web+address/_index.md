---
title : "Insert a Linked Picture from Web Address" 
description : "" 
weight : 16419 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngworkbooksandworksheets/insert+a+linked+picture+from+web+address/
---

# Aspose.Cells for Java : Insert a Linked Picture from Web Address


Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL and the picture will be downloaded every time the spreadsheet is opened in Microsoft Excel. The image is not physically embedded into the Excel document, but points to a web resource.

### Inserting a Linked Picture from Web Address

#### Using Microsoft Excel

In Microsoft Excel (for example 2007):

1.  Click the **Insert** menu and select **Picture**.  
      
    ![image](5473005.png)
2.  Specify the web address for the picture in the Insert Picture dialog.  
      
    ![image](5473000.png)  
      
    The image is inserted.  
      
    ![image](5473076.png)

#### Using Aspose.Cells for Java

Aspose.Cells for Java supports adding a linked image using the method [ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

The method returns a [Picture](https://apireference.aspose.com/java/cells/com.aspose.cells/Picture) object.

The following example shows how to add linked picture from web address to a worksheet.

After running the code, the generated Excel file contains a linked image on the first worksheet.

**The output file**  
![image](5473004.png)



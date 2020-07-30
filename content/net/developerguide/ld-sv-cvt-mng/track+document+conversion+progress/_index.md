---
title : "Track Document Conversion Progress" 
description : "" 
weight : 12076 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/track+document+conversion+progress/
---

# Aspose.Cells for .NET : Track Document Conversion Progress


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Track Document Conversion Progress](#track-document-conversion-progress)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
## Possible Usage Scenarios

Sometimes converting large excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion process by providing the [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface. The [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface provides [PageStartSaving](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) and [PageEndSaving](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the T*estPageSavingCallback* custom class.

## Track Document Conversion Progress

The following code sample loads the [source excel file](https://docs2.aspose.com/cells/net/attachments/94635041/94896151.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface.

## Sample Code

The following is the code for the *TestPageSavingCallback* custom class.

## Console Output

Start saving page index 0 of pages 11  
End saving page index 0 of pages 11  
Start saving page index 1 of pages 11  
End saving page index 1 of pages 11  
Start saving page index 2 of pages 11  
End saving page index 2 of pages 11  
Start saving page index 3 of pages 11  
End saving page index 3 of pages 11  
Start saving page index 4 of pages 11  
End saving page index 4 of pages 11  
Start saving page index 5 of pages 11  
End saving page index 5 of pages 11  
Start saving page index 6 of pages 11  
End saving page index 6 of pages 11  
Start saving page index 7 of pages 11  
End saving page index 7 of pages 11  
Start saving page index 8 of pages 11  
End saving page index 8 of pages 11

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [PagesBook1.xlsx](https://docs2.aspose.com/cells/net/attachments/94635041/94896151.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  


---  
title: Freeze Panes in Jython  
type: docs  
weight: 60  
url: /java/freeze-panes-in-jython/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Freeze Panes**  
To demonstrate freeze panes using **Aspose.Cells Java for Jython**. Here you can see an example code.  

**Jython Code**  

{{< highlight java >}}  

 from aspose-cells import Settings  

from com.aspose.cells import Workbook  


class FreezePanes:  

    def __init__(self):  

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'  



        workbook = Workbook(dataDir + "Book1.xls")  



        # Accessing the first worksheet in the Excel file  

        worksheets = workbook.getWorksheets()  

        worksheet = worksheets.get(0)  

        # Applying freeze panes settings  

        worksheet.freezePanes(3,2,3,2)  

        # Saving the modified Excel file in default format  

        workbook.save(dataDir + "book.out.xls")  

        # Print Message  

        print "Panes freeze successful."  

if __name__ == '__main__':         

    FreezePanes()  

{{< /highlight >}}  

## **Download Running Code**  
Download the sample code (Aspose.Cells) from any of the below‑mentioned social coding sites:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)

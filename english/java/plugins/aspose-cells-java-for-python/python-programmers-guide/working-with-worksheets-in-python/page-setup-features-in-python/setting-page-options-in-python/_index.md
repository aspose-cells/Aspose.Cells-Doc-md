---
title: Setting Page Options in Python
type: docs
weight: 10
url: /java/setting-page-options-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Setting Page Options**
### **Page Orientation**
To apply page orientation settings using **Aspose.Cells Java for Python**, call the **page_orientation** method of the [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pageSetup) class.

**Python Code**

{{< highlight python >}}
def page_orientation(self):
    # Instantiating a Workbook object by Excel file path
    workbook = self.Workbook()

    # Accessing the first worksheet in the Excel file
    worksheets = workbook.getWorksheets()
    sheet_index = worksheets.add()
    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait
    page_setup = sheet.getPageSetup()
    page_orientation_type = self.PageOrientationType
    page_setup.setOrientation(page_orientation_type.PORTRAIT)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(self.dataDir + "Page_Orientation.xls")
    print "Set page orientation, please check the output file."
{{< /highlight >}}

### **Scaling Factor**
To apply scaling using **Aspose.Cells Java for Python**, call the **scaling** method of the [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pageSetup) class.

**Python Code**

{{< highlight python >}}
def scaling(self):        
    # Instantiating a Workbook object by Excel file path
    workbook = self.Workbook(self.dataDir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file
    worksheets = workbook.getWorksheets()
    sheet_index = worksheets.add()
    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100
    page_setup = sheet.getPageSetup()
    page_setup.setZoom(100)

    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(self.dataDir + "Scaling.xls")
    print "Set scaling, please check the output file."
{{< /highlight >}}

## **Download Running Code**
Download **Setting Page Options (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)

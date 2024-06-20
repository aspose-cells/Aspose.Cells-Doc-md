---
title: Jython da Belge Özelliklerini Yönetme
type: docs
weight: 60
url: /tr/java/managing-document-properties-in-jython/
---

## **Aspose.Cells - Belge Özelliklerini Yönetme**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class ManagingDocumentProperties:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ManagingDocumentProperties/'

        workbook = Workbook(dataDir + "Book1.xls")

        #Retrieve a list of all custom document properties of the Excel file

        customProperties = workbook.getWorksheets().getCustomDocumentProperties()

        #Accessing a custom document property by using the property index

        #customProperty1 = customProperties.get(3)

        #Accessing a custom document property by using the property name

        customProperty2 = customProperties.get("Owner")


        #Adding a custom document property to the Excel file

        publisher = customProperties.add("Publisher", "Aspose")

        #Save the file

        workbook.save(dataDir + "Test_Workbook.xls")

        #Removing a custom document property

        customProperties.remove("Publisher")

        #Save the file

        workbook.save(dataDir + "Test_Workbook_RemovedProperty.xls")

        # Print message

        print "Excel file's custom properties accessed successfully."



if __name__ == '__main__':        

    ManagingDocumentProperties()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ManagingDocumentProperties.py)

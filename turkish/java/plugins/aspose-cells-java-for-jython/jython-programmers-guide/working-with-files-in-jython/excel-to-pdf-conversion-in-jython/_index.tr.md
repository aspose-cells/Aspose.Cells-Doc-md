---
title: Jython'da Excel'den PDF'ye Dönüştürme
type: docs
weight: 50
url: /tr/java/excel-to-pdf-conversion-in-jython/
---
## **Aspose.Cells - Excel'den Pdf'ye Dönüştürme**
 Belgeleri kullanarak eklemek için**Jython için Aspose.Cells Java**. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat



class Excel2PdfConversion:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/Excel2PdfConversion/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Save the document in PDF format

        workbook.save(dataDir + "OutBook1.pdf", saveFormat.PDF)

        # Print message

        print "\n Excel to PDF conversion performed successfully."



if __name__ == '__main__':        

    Excel2PdfConversion()

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Belgeleri Ekleyin (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)

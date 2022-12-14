---
title: Преобразование Excel в PDF в Jython
type: docs
weight: 50
url: /ru/java/excel-to-pdf-conversion-in-jython/
---
## **Aspose.Cells - Преобразование Excel в PDF**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

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
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)

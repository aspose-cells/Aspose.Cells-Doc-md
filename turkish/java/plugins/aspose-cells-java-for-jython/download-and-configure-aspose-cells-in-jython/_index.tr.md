---
title: Jython da Aspose.Cells i İndirme ve Yapılandırma
type: docs
weight: 10
url: /tr/java/download-and-configure-aspose-cells-in-jython/
---

## **İndirme**

**Sosyal kodlama sitelerinden örnekleri indirin**

Çalışan örnek sürümlerini aşağıda belirtilen tüm sosyal kodlama sitelerinden indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Aspose.Cells for Java bileşenini indirin**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Yüklemek**

- İndirilen Aspose.Cells for Java jar dosyasını "lib" dizinine yerleştirin.
- _*init*_.py dosyasında "your-lib" yerine indirilen jar dosya adını değiştirin.

## **Kullanarak**

Aşağıdaki örnek kodu kullanarak HelloWorld belgesi oluşturabilirsiniz:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

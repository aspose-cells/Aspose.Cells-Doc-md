---
title: Jython で Aspose.Cells をダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-jython/
---
## **ダウンロード中**

**ソーシャル コーディング Web サイトからサンプルをダウンロードする**

実行中のサンプルの次のリリースは、以下で言及されているすべてのソーシャル コーディング サイトでダウンロードできます。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Aspose.Cells for Java コンポーネントをダウンロード**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **インストール**

- ダウンロードした Aspose.Cells for Java jar ファイルを「lib」ディレクトリに配置します。
- _*init*_.py ファイルで、「your-lib」をダウンロードした jar ファイル名に置き換えます。

## **使用する**

次のコード例を使用して、HelloWorld ドキュメントを作成できます。

{{< highlight "java" >}}

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

---
title: JythonでAspose.Cellsのダウンロードと構成
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-jython/
---

## **ダウンロード**

**ソーシャルコーディングWebサイトから例をダウンロード**

実行例の次のリリースを以下で言及されるすべてのソーシャルコーディングサイトからダウンロードできます:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Aspose.Cells for Javaコンポーネントをダウンロード**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **インストール**

- ダウンロードしたAspose.Cells for Java JARファイルを「lib」ディレクトリに配置します。
- _*init*_.pyファイルで「your-lib」をダウンロードしたJARファイル名に置き換えます。

## **を使用する**

次の例コードを使用してHelloWorldドキュメントを作成できます:

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

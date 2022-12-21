---
title: xlsx4j でワークシートのタブの色を設定する
type: docs
weight: 60
url: /ja/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - ワークシートのタブの色を設定する**
Aspose.Cells では、個々のワークシート タブの色を変更して、他のタブよりも目立つようにすることができます。たとえば、経費を赤、売上を緑、資産を青などにすることができます。
### **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブ シートのタブを右クリックします。
1. 選択する**タブの色**.
1. パレットから色を選択します。
1. クリック**わかった**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークシートのタブの色を設定](/java/set-worksheet-tab-color).

{{% /alert %}}

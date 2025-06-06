---
title: xlsx4jでのワークシートタブの色の設定
type: docs
weight: 60
url: /ja/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - ワークシートのタブの色を設定**
Aspose.Cells を使用すると、個々のワークシートタブの色を変更して目立たせることができます。たとえば、Expenses を赤、Sales を緑、Assets を青などにすることができます。
### **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブシートでタブを右クリックします。
1. **タブの色** を選択します。
1. パレットから色を選択します。
1. **OK** をクリックします。

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

詳細については、[ワークシートタブの色を設定](/java/set-worksheet-tab-color)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

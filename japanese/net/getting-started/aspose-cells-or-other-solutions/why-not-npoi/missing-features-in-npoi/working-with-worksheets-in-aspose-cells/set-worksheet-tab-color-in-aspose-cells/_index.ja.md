---
title: Aspose.Cells でワークシートのタブの色を設定
type: docs
weight: 20
url: /ja/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - ワークシートのタブの色を設定**
Aspose.Cells を使用すると、個々のワークシートタブの色を変更して目立たせることができます。たとえば、Expenses を赤、Sales を緑、Assets を青などにすることができます。
### **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブシートでタブを右クリックします。
1. **タブの色** を選択します。
1. パレットから色を選択します。
1. **OK** をクリックします。

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから **ワークシートのタブの色を設定** をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[セルのワークシートのタブの色の設定](/cells/ja/net/set-worksheet-tab-color/)を参照してください。

{{% /alert %}}

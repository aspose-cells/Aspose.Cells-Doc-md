---
title: Aspose.Cells でワークシートのタブの色を設定する
type: docs
weight: 20
url: /ja/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - ワークシートのタブの色を設定する**
Aspose.Cells では、個々のワークシート タブの色を変更して、他のタブよりも目立つようにすることができます。たとえば、経費を赤、売上を緑、資産を青などにすることができます。
### **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブ シートのタブを右クリックします。
1. 選択する**タブの色**.
1. パレットから色を選択します。
1. クリック**わかった**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートのタブの色を設定**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークシートのタブの色を設定](/cells/ja/net/set-worksheet-tab-color/).

{{% /alert %}}

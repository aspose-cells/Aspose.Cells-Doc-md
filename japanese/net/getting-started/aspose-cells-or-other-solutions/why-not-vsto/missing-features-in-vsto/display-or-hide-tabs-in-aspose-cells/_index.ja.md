---
title: Aspose.Cells でタブを表示または非表示にする
type: docs
weight: 80
url: /ja/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel ファイルの下部をよく見ると、多数のコントロールが表示されます。これらには以下が含まれます：

- シート タブ。
- タブスクロールボタン。

シート タブは、Excel ファイル内のワークシートを表します。任意のタブをクリックして、そのワークシートに切り替えます。ワークブック内のワークシートが多いほど、シート タブが多くなります。 Excel ファイルに十分な数のワークシートがある場合は、それらをナビゲートするためのボタンが必要です。そのため、Microsoft Excel には、シート タブをスクロールするためのタブ スクロール ボタンが用意されています。

**シート タブとタブ スクロール ボタン** 

![todo:画像_代替_文章](display-or-hide-tabs-in-aspose-cells_1.png)

Aspose.Cells を使用すると、開発者は Excel ファイルのシート タブとタブ スクロール ボタンの表示を制御できます。

{{% /alert %}} 

以下は、Excel ファイル (book1.xls) を開き、そのタブを非表示にして、変更したファイルを output.xls として保存する完全な例です。

下の図では、Book1.xls ファイルにタブが含まれていることがわかります。以下の output.xls ファイルのスクリーンショットからわかるように、サンプル コードを実行すると、タブが非表示になります。

**book1.xls: 変更前の Excel ファイル** 

![todo:画像_代替_文章](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls：修正後のExcelファイル** 

![todo:画像_代替_文章](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **タブバーの幅の制御**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

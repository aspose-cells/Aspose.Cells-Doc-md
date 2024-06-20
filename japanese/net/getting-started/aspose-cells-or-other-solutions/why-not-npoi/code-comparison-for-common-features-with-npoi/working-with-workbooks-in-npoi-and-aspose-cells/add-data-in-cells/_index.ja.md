---
title: セルにデータを追加
type: docs
weight: 10
url: /ja/net/add-data-in-cells/
description: この記事では、Aspose.Cells for .NET APIsを使用してセルにデータを追加する方法について説明します。
keywords: C#でセルにデータを追加、C#でワークシートにデータを挿入、C#でセルのデータを設定します。
---


## **Aspose.Cells for .NETを使用したセルにデータを追加する方法**
Aspose.Cellsは、Microsoft Excelファイルを表すWorkbookクラスを提供します。Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetCollectionが含まれています。ワークシートはWorksheetクラスで表され、WorksheetクラスにはCellsコレクションがあります。Cellsコレクションの各アイテムは、Cellクラスのオブジェクトを表します。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - セルにデータを追加する**
NPOIでは、row.createCell(1).setCellValueを使用してセルにデータを追加することができます。

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから、**セルにデータを追加する**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細は[セルにデータを追加する](/cells/ja/net/add-data-in-cells/)を参照してください。

{{% /alert %}}

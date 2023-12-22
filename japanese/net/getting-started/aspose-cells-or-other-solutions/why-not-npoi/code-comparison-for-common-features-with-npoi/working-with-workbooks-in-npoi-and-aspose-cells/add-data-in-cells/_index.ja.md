---
title: Cellsにデータを追加
type: docs
weight: 10
url: /ja/net/add-data-in-cells/
description: この記事では、Aspose.Cells for .NET API を使用して Cells にデータを追加する方法について説明します。
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Aspose.Cells for .NET を使用して Cells にデータを追加する方法**
Aspose.Cells は、Microsoft Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection が含まれています。ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは Cellscollection を提供します。 Cells コレクション内の各項目は、Cell クラスのオブジェクトを表します。

**C#**

{{< highlight "cs" >}}

 //Workbook オブジェクトをインスタンス化する

ワークブック workbook = new Workbook();

// Excel ファイルに追加されたワークシートにアクセスします

ワークシート worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Cells にデータを追加**
NPOI では、 row.createCell(1).setCellValue を使用してセルにデータを追加できます。

**C#**

{{< highlight "cs" >}}

 IWorkbook ワークブック = new XSSFWorkbook();

ISheetsheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("これはサンプルです");

int x = 1;

for (int i = 1; i<= 15; i++)

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
##  **実行コードをダウンロード**
ダウンロード**Cellsにデータを追加**以下に挙げるソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次のサイトをご覧ください。[Cellsにデータを追加する](/cells/ja/net/add-data-in-cells/).

{{% /alert %}}

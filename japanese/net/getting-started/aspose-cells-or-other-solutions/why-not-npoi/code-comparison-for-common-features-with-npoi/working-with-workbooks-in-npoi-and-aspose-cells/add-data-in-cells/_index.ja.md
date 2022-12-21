---
title: Cells にデータを追加
type: docs
weight: 10
url: /ja/net/add-data-in-cells/
---
## **Aspose.Cells - Cells にデータを追加**
Aspose.Cells は、Microsoft Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは Cellscollection を提供します。 Cells コレクションの各アイテムは、Cell クラスのオブジェクトを表します。

**C#**

{{< highlight "cs" >}}

// Workbook オブジェクトのインスタンス化

ワークブック ワークブック = 新しいワークブック();

//Excel ファイルに追加されたワークシートにアクセスする

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
## **NPOI HSSF XSSF - Cells にデータを追加**
NPOI では、row.createCell(1).setCellValue を使用してセルにデータを追加できます。

**C#**

{{< highlight "cs" >}}

 IWorkbook ワークブック = 新しい XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

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
## **実行中のコードをダウンロード**
ダウンロード**Cells にデータを追加**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[Cells にデータを追加する](/cells/ja/net/add-data-in-cells/).

{{% /alert %}}

---
title: 新しいワークブックを作成
type: docs
weight: 20
url: /ja/net/create-new-workbook/
---
## **Aspose.Cells - 新しいワークブックの作成**
ワークブッククラスは簡単に使用できます

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - 新規ワークブックの作成**
Workbook クラスを使用して新しい Workbook を作成し、FileOutputStream を使用して保存します。

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**新しいワークブックを作成**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)

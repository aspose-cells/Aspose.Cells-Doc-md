---
title: 新しいブックを作成
type: docs
weight: 20
url: /ja/net/create-new-workbook/
---

## **Aspose.Cells - 新しいブックを作成**
Workbookクラスは簡単に使用できます

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - 新しいブックを作成**
Workbookクラスを使用して新しいブックを作成し、FileOutputStreamを使用して保存してください。

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから、**新しいブックを作成**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)

---
title: ワークブックをテキストに保存するか、Aspose.Cells を使用して CSV 形式に保存します
type: docs
weight: 80
url: /ja/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存する必要があります。テキスト形式 (例: TXT、TabDelim、CSV など) の場合、既定では、Microsoft Excel と Aspose.Cells の両方で、アクティブなワークシートの内容のみが保存されます。

{{% /alert %}} 

次のコード例は、ブック全体をテキスト形式で保存する方法を示しています。 Microsoft Excel または OpenOffice スプレッドシート ファイル (XLS、XLSX、XLSM、XLSB、ODS など) のソース ワークブックを任意の数のワークシートと共に読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、TxtSaveOptions.Separator はコンマであるため、CSV 形式で保存する場合は区切り記号を指定しないでください。

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "ワークブックをテキストまたは CSV Format.xlsx に保存";

string destFileName = FilePath + "ワークブックをテキストまたは CSV Format.txt に保存";

// ソース ワークブックを読み込む

ワークブック ワークブック = 新しいワークブック(ファイル名);

//0 バイト配列

byte[]workbookData = 新しい byte[0];

//テキスト保存オプション。任意のタイプのセパレータを使用できます

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//各ワークシート データをワークブック データ配列内のテキスト形式でコピーします

for (int idx = 0; idx< workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **実行例をダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)

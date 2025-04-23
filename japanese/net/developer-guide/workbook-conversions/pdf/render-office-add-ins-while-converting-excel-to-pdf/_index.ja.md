---
title: ExcelをPDFに変換する際のOffice Add Insのレンダリング
type: docs
weight: 100
url: /ja/net/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能な使用シナリオ**

以前は、Aspose.CellsはExcelファイルをPDF形式で保存する際にOffice Add-Insをレンダリングできませんでした。現在は問題ありません。特別なメソッドやプロパティを使用する必要はありません。ExcelファイルをPDF形式に保存するだけでOffice Add-Insがレンダリングされます。

## **ExcelをPDFに変換する際のOffice Add-Insのレンダリング**

次のサンプルコードは、Officeアドインが含まれる[サンプルExcelファイル](60489769.xlsx)を保存します。以前のバージョン（17.11など）で生成された出力PDF（60489770.pdf）は空白ですが、新しいバージョン（17.12以降）で生成された出力PDF（60489771.pdf）はOfficeアドインが表示されます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.cs" >}}
{{< app/cells/assistant language="csharp" >}}

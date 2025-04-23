---
title: Excelでの互換性チェッカーを無効にする
type: docs
weight: 170
url: /ja/python-net/disable-compatibility-checker-in-excel/
description: この記事は、Aspose.Cells for Python via .NET APIを使用して互換性チェッカーを無効にする方法を示しています。
keywords: Pythonで互換性チェッカーを無効にする、Excelで互換性チェッカーを無効にする（C＃）、ワークブックで互換性チェッカーを無効にする。 
---

## PythonのExcelワークシートで互換性チェッカーを無効にする 

{{% alert color="primary" %}}

Microsoft Excelの互換性チェッカーは、以前のファイル形式でファイルを保存すると機能の問題や精度の低下が引き起こされる可能性があるとして警告を出します。互換性チェッカーはMicrosoft Office Excel 2007およびMicrosoft Excel 2010の機能です。

以前のバージョンのワークブックをExcel 2007またはExcel 2010からExcel 97からExcel 2003に保存する場合、互換性チェッカーは、以前のバージョンではサポートされていない機能が含まれていないかどうかをワークブックをスキャンします。互換性の問題についての決定を支援するために、互換性チェッカーはオプションを含むダイアログボックスを表示します。また、ワークブックの問題に関するレポートを作成したり、機能を無効にすることもできます。

特定のスプレッドシートについて互換性チェッカーを無効にする必要がある場合があります。Aspose.Cells for Python via .NETのAPIを使用すると、プログラムでこれを実行でき、ユーザーがMicrosoft Excelでファイルを再保存する際に互換性チェッカーのダイアログボックスが表示されて混乱したりフラストレーションを感じたりしないようにできます。

{{% /alert %}}

## **Microsoft Excelを使用して互換性チェッカーを無効にする方法**

Microsoft Excel（例: Microsoft Excel 2007/2010）で互換性チェッカーを無効にする場合:

- （Excel 2007）[Office] ボタンをクリックし、「準備」、[互換性の確認] をクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.
- (Excel 2010) ファイルタブをクリックし**情報**、**問題の確認**、**互換性を確認**をクリックし、最後に**このブックを保存する場合に互換性をチェック**のチェックを外します。

## **Aspose.Cells APIを使用して互換性チェッカーを無効にする方法**

Microsoft Excelの互換性チェッカーを無効にするには、[**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility)プロパティを**False**に設定します。

### **コード例**

以下のコード例は、Aspose.Cells for Python via .NETを使用して互換性チェッカーを無効にする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}


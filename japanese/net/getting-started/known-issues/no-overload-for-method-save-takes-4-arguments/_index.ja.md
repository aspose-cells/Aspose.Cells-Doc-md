---
title: Saveメソッドには4つの引数を取るオーバーロードが存在しません
type: docs
weight: 70
url: /ja/net/no-overload-for-method-save-takes-4-arguments/
---

## **症状**

Aspose.Cellsバージョンを使用していると、ResponseオブジェクトにWorkbookを保存しようとする際にSaveメソッドを使用すると、このエラーが発生します。このコードスニペットはオンラインドキュメントで記載されています。

### **エラーのスクリーンショット**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **解決策**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NETは、.NETフレームワークのすべてのバージョン（2.x、3.x、4.xなど）と互換性があり、どのタイプのプロジェクト（Asp.NET/Winforms、Webプロジェクト、Windows/Webサービス、コンソールアプリケーションまたはその他のプロジェクトなど）でも正常に機能します。異なる.NETフレームワークのバージョンに対応した異なるdllを提供しています。詳細については、インストールディレクトリの「\Bin」フォルダ内の「readme.txt」ファイルを参照してください。ただし、この「readme.txt」ファイルが存在します。

製品をWebアプリケーションで使用する場合は、「/bin」ディレクトリの「.NET 2.0」フォルダからAspose.Cells.dllを使用してください。ご注意ください、「.NET 3.5クライアントプロファイル」ディレクトリ内のdllは、VS.NETのターゲットフレームワークとしてNet frameクライアントプロファイルを持つコンソールアプリケーションでのみ使用されます。プロジェクトを確認してください。プロジェクトがこのdllを参照している可能性があります。

### **参照**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>

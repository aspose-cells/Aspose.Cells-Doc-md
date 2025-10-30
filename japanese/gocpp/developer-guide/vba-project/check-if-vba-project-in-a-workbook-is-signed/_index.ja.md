---
title: Workbook内のVBAプロジェクトに署名されているかどうかをGolangとC++を使って確認する
linktitle: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/go-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.CellsとGolangを使ってWorkbook内のVBAプロジェクトに署名があるかどうかを確認する
---

{{% alert color="primary" %}}

Microsoft Excelの**Tools > Digital Signatures...**メニューコマンドを使用して、VBAプロジェクトが署名されているかどうかを確認できます。同様に、Aspose.Cellsの[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/)を使用してプログラム的に確認することもできます。

{{% /alert %}}

## **C++でWorkbook内のVBAプロジェクトが署名されているかどうかを確認する**

以下のコードは、ワークブックをロードし、そのVBAプロジェクトが署名されているかどうかを [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/)プロパティを使用して判定します。署名されている場合は **true** を返し、そうでなければ**false**を返します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfVbaProjectInAWorkbookIsSigned.go" >}}

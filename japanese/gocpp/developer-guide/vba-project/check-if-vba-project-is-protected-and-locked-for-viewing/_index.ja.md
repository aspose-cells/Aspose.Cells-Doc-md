---
title: GolangとC++を使ってVBAプロジェクトが保護されていて閲覧できないようにロックされているか確認する
linktitle: VBA（Visual Basic for Applications）プロジェクトが保護されて表示ロックされているかどうかを確認
type: docs
weight: 30
url: /ja/go-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Excelファイル内のVBAプロジェクトが保護されているか、閲覧ロックされているかどうかをAspose.Cells for C++を使用して確認する方法を学びます。
---

## C++でVBAプロジェクトが保護されており閲覧可能かどうかを確認する方法

Aspose.Cellsを使用すると、ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されているかつ、閲覧のためにロックされているかどうかを確認できます。そのためにAPIは[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/go-cpp/vbaproject/getislockedforviewing/)プロパティを提供します。閲覧用にロックされている場合、[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/go-cpp/vbaproject/getislockedforviewing/)プロパティは**true**を返します。

## **サンプルコード**

次のサンプルコードは、[サンプルExcelファイル](43352065.xlsm)をロードし、そのExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されており閲覧用にロックされているかどうかを確認します。参考のために、そのコンソール出力もご覧ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfVbaProjectIsProtectedAndLockedForViewing.go" >}}
## **コンソール出力**

上記のサンプルコードを提供された[サンプル Excelファイル](43352065.xlsm)で実行した際のConsoleの出力です。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}

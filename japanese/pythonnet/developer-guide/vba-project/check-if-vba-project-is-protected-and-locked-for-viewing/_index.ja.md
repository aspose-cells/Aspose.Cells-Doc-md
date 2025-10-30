---
title: VBA（Visual Basic for Applications）プロジェクトが保護されて表示ロックされているかどうかを確認
type: docs
weight: 30
url: /ja/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/
---

## PythonでVBAプロジェクトが保護され閲覧ロックされているか確認する

Aspose.Cells for Python via .NETは、ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されて閲覧ロックされているかどうかを確認できます。このために、APIは[**VbaProject.islocked_for_viewing**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/islocked_for_viewing/)プロパティを提供します。閲覧ロックされている場合は、[**VbaProject.islocked_for_viewing**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/islocked_for_viewing/)プロパティが**true**を返します。

## **サンプルコード**

次のサンプルコードでは、[サンプル Excelファイル](43352065.xlsm)を読み込んで、ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護され、閲覧がロックされているかどうかを確認します。参考のために、Console の出力もご覧ください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckifVBAProjectisProtectedandLockedforViewing.py" >}}

## **コンソール出力**

上記のサンプルコードを提供された[サンプル Excelファイル](43352065.xlsm)で実行した際のConsoleの出力です。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}

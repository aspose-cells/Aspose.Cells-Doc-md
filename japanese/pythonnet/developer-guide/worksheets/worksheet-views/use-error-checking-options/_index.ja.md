---
title: エラーチェックオプションを使用する
type: docs
weight: 140
url: /ja/python-net/use-error-checking-options/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、Excelワークシートのエラー検出オプション（例：テキストとして保存された数字）をプログラム的に使用するサンプルコードを紹介します。
keywords: Python Excelライブラリ、Pythonでエラー検出の設定方法、エラー検出をPythonで管理する方法。
---

{{% alert color="primary" %}}

Microsoft Excelでは、ユーザーはエラーチェックのオプションやルールを定義することができます。ユーザーが数式を作成する際にエラーチェックが表示されることがよくあり、セルの右上隅に小さな三角形が表示されます。Excelは、一般的な問題を修正するための情報を提供します。

{{% /alert %}}

## **エラーの種類**

数値を0で割るなど、式が結果を返せないエラーは即座の対応が必要であり、セルにエラー値が表示されます。緑色の三角形をクリックすると感嘆符が表示され、これをクリックするとオプションのリストが開きます。

エラーはオプションを使用して解決したり、無視することができます。エラーを無視すると、以降のエラーチェックにそのエラーが表示されなくなります。

Aspose.Cells for Python via .NETは、エラー検出機能を提供します。[**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption)クラスは、テキストとして保存された数字、数式計算エラー、検証エラーなど、さまざまなエラー検出タイプを管理します。[**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype)列挙体を使って必要なエラー検出を設定します。

## **テキストとして保存された数値**

時折、数値はセル内でテキストとしてフォーマットされ保存されることがあります。これは計算に問題を引き起こしたり、混乱する並び順を生むことがあります。テキストとしてフォーマットされた数値は、セル内で右寄せではなく左寄せになります。セル内で数学的演算を行うはずの式が値を返さない場合は、式が参照しているセルの配置を確認し、これらのいくつかまたはすべてのセルがテキストとして保存された数値である可能性があります。

テキストとして保存された数値を実際の数値に素早く変換するために、エラーチェックオプションを使用できます。Microsoft Excel 2003では:

1. **ツール** メニューで **オプション** をクリックします。
1. エラー検出タブを選択します。**数字がテキストとして保存**オプションはデフォルトで有効です。
1. 無効にします。

以下のサンプルコードは、Aspose.Cells for Python via .NET APIを使用して、テンプレートのXLSファイル内のワークシートで「数字をテキストとして保存」のエラー検出を無効にする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

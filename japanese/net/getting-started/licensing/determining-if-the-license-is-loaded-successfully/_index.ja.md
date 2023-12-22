---
title: ライセンスが正常にロードされたかどうかを確認する
type: docs
weight: 260
url: /ja/net/determining-if-the-license-is-loaded-successfully/
description: NET API の Aspose.Cells を介してライセンスが正常にロードされたかどうかを検出する方法を学習します。
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cellsが提供します[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)このプロパティを使用して、ライセンスが正常にロードされたかどうかを判断できます。ライセンスを設定する前にこのプロパティにアクセスすると、次の結果が返されます。**間違い**ライセンスを設定した後にこのプロパティを呼び出すと、返されます。**真実**ライセンスが正常にロードされたことを示します。

{{% /alert %}}

##  C# ライセンスが正常にロードされたかどうかを判断するコード

次のコードは、[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)ライセンスを設定する前にプロパティを変更すると、*false** が返されます。次に、ライセンスをロードしてプロパティに再度アクセスし、*true** を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **コンソール出力**

上記のサンプル コードのコンソール (デバッグ) 出力は次のとおりです。

{{< highlight "java" >}}

False

True

{{< /highlight >}}

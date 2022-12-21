---
title: ライセンスが正常にロードされたかどうかの判断
type: docs
weight: 260
url: /ja/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

Aspose.Cells提供[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)ライセンスが正常にロードされたかどうかを判断するために使用できるプロパティ。ライセンスを設定する前にこのプロパティにアクセスすると、**間違い**ライセンスを設定した後にこのプロパティを呼び出すと、**真実**ライセンスが正常にロードされたことを示します。

{{% /alert %}}

## ライセンスが正常に読み込まれたかどうかを判断するための C# コード

次のコードは、[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)ライセンスを設定する前にプロパティを返し、それが返されます**間違い**.次に、ライセンスをロードし、再びプロパティにアクセスします。**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **コンソール出力**

上記のサンプル コードのコンソール (デバッグ) 出力は次のとおりです。

{{< highlight "java" >}}

False

True

{{< /highlight >}}

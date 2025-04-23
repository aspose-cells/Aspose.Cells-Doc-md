---
title: ライセンスが正常に読み込まれているかどうかを判断する
type: docs
weight: 260
url: /ja/net/determining-if-the-license-is-loaded-successfully/
description: ライセンスが正常に読み込まれているかどうかを Aspose.Cells for NET APIs を使用して検出する方法を学びます。
keywords: C#でライセンスが正常に読み込まれているかどうかを検出する方法、ライセンスが正常に読み込まれたかを決定する方法、C#を使用してライセンスが正常に読み込まれたかを確認する方法、ライセンスのステータスを確認する
---

{{% alert color="primary" %}}

Aspose.Cellsは、ライセンスが正常に読み込まれたかどうかを判断するために[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)プロパティを提供しています。このプロパティにアクセスするときは、ライセンスを設定する前にアクセスすると**false**を返し、ライセンスを設定した後にアクセスすると**true**を返します。これは、ライセンスが正常に読み込まれたことを示しています。

{{% /alert %}}

ライセンスが正常に読み込まれているかどうかを検出するためのC#コード

以下のコードはライセンスを設定する前に[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)プロパティにアクセスし、**false**を返します。その後ライセンスをロードし、再度このプロパティにアクセスすると、**true**を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **コンソール出力**

上記のサンプルコードのコンソール（デバッグ）出力はこちらです。

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

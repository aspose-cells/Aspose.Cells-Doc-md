---
title: ライセンスが正常に読み込まれているかどうかを判断する
type: docs
weight: 210
url: /ja/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells は、ライセンスが正常にロードされたかどうかを判断するために使用できる [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) プロパティを提供します。ライセンスを設定する前にこのメソッドを呼び出すと false を返し、ライセンスを設定した後にこのメソッドを呼び出すと true を返します。これにより、ライセンスが正常にロードされたことが示されます。

{{% /alert %}}

## **ライセンスが正常にロードされたかどうかを判断する**

以下のコードは、ライセンスを設定する前に [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) メソッドにアクセスして false を返し、その後ライセンスをロードしてプロパティに再度アクセスすると true を返します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

---
title: ライセンスが正常にロードされたかどうかの判断
type: docs
weight: 210
url: /ja/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

Aspose.Cells提供[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)ライセンスが正常にロードされたかどうかを判断するために使用できるプロパティ。ライセンスを設定する前にこのメソッドを呼び出すと false が返され、ライセンスを設定した後でこのメソッドを呼び出すと、ライセンスが正常に読み込まれたことを示す true が返されます。

{{% /alert %}}

## **ライセンスが正常にロードされたかどうかの判断**

次のコードは、[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)ライセンスを設定する前にメソッドを実行すると、false が返されます。次に、ライセンスをロードし、プロパティに再度アクセスすると、true が返されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **コンソール出力**

上記のサンプル コードのコンソール出力は次のとおりです。

{{< highlight "java" >}}

false

true

{{< /highlight >}}

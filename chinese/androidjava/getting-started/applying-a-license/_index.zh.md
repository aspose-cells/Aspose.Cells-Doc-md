---
title: 申请许可证
type: docs
weight: 40
url: /zh/java/applying-a-license/
---
{{% alert color="primary" %}}

一旦您对 Aspose.Cells 的评价感到满意，[购买许可证](https://purchase.aspose.com/buy)在 Aspose 网站上。让自己熟悉不同的[许可证类型](https://purchase.aspose.com/policies/license-types/)提供。如果您有任何问题，请不要犹豫[联系 Aspose 销售团队](https://about.aspose.com/contact).

每个 Aspose 许可证都包含一年订阅，可以免费升级到在此期间发布的任何新版本或修复程序。技术支持是免费和无限制的，同时提供给许可用户和评估用户。

许可证是一个纯文本 XML 文件，其中包含产品名称、许可开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件：即使在文件中添加额外的换行符也会使其失效。

在对文档执行任何操作之前，您需要设置许可证。确保在创建 Document 对象之前执行此操作。您只需为每个应用程序或进程设置一次许可证。

{{% /alert %}}

## **加载许可证文件**

Aspose.Cells for Android via Java，license可以[作为资源嵌入](/cells/zh/java/applying-a-license/#applying-a-license-from-an-embedded-resource)，或从流中加载：

1. 把license文件放在任意位置**/mnt/SD卡/**.
1. 创建引用文件的流。
1. 将流（包含许可证文件）传递到 SetLicense 方法中。

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **从嵌入式资源应用许可证**

要从 Android 包文件中按名称访问作为资源的许可证：

1. 将许可证文件作为资源添加到您的应用程序的**资源/原始**文件夹。
许可证文件应该在**资源/原始**文件夹。
1. 使用以下代码示例从资源访问/加载许可证。

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}

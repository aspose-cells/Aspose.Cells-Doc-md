---
title: Licensing
type: docs
weight: 50
url: /zh/java/licensing/
description: Aspose.Cells for JAVA 提供不同的购买计划，或提供免费试用和 30 天临时许可证以使用 Licensing 和 Java 中的订阅策略进行评估。
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **如何在Aspose.Cells组件中申请License**

该许可证是一个纯文本 XML 文件，其中包含产品名称、许可的开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件；即使无意中在文件中添加了额外的换行符也会使其失效。

如果您想避免其评估限制，您需要在使用 Aspose.Cells 之前设置许可证。您只需为每个应用程序或进程设置一次许可证。

可以从以下位置的流或文件加载许可证：

1. 显式路径。
1. 包含 Aspose.Cells.jar 的文件夹。

使用[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)方法来许可组件。通常，设置许可证的最简单方法是将许可证文件放在与 Aspose.Cells.jar 相同的文件夹中，并仅指定文件名而不指定路径，如下例所示：

###  **如何从磁盘应用许可证**

在这个例子中**Aspose.Cells**将尝试在包含应用程序 JAR 的文件夹中查找许可证文件。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **如何从 Stream 申请许可证**

从流初始化许可证。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **如何在Aspose.Cells.GridWeb中申请License**

建议将许可代码放在 Web 应用程序中应首先处理的位置。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **如何申请计量许可证**

Aspose.Cells 允许开发者应用计量密钥。这是一种新的许可机制。新的发牌机制将与现有的发牌方法同时使用。想要根据 API 功能的使用情况进行计费的客户可以使用计量许可。欲了解更多详情，请参阅[计量 Licensing 常见问题解答](https://purchase.aspose.com/faqs/licensing/metered)部分。

新班级[计量](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)已引入应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}

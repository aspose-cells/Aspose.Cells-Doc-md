---
title: 许可
type: docs
weight: 50
url: /zh/java/licensing/
description: Aspose.Cells for JAVA提供了不同的购买计划或提供免费试用并提供30天临时许可证，以使用Java中的许可证和订阅策略进行评估。
keywords: Java从磁盘或流应用许可证。Java从磁盘或流设置许可证。在Aspose.Cells for Java中应用许可证。
---

## **如何在Aspose.Cells组件中应用许可证**

许可证是包含产品名称、许可给开发人员数量、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此请勿修改文件; 即使意外添加额外的换行符到文件中也会使其无效。

如果要避免其评估限制，则需要在使用Aspose.Cells之前设置许可证。每个应用程序或进程只需要设置许可证一次。

许可证可以从以下位置的流或文件加载:

1. 明确的路径。
1. 包含Aspose.Cells.jar的文件夹。

使用[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream))方法来为组件提供许可证。通常设置许可证的最简单方法是将许可证文件放在与Aspose.Cells.jar相同的文件夹中，并仅指定文件名而不指定路径，如以下示例所示:

### **如何从磁盘应用许可证**

在这个例子中，**Aspose.Cells** 将尝试在包含您的应用程序JAR的文件夹中找到许可证文件。

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **如何从流应用许可证**

从流中初始化许可证。

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **如何在Aspose.Cells.GridWeb中应用许可证**

建议将许可代码放在Web应用程序中应首先处理的位置。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **如何申请按使用量计费的许可**

Aspose.Cells允许开发人员应用按使用量计费的密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。那些希望基于API功能的使用量计费的客户可以使用按使用量计费。有关更多详细信息，请参阅[Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)章节。

引入了一个新类[Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)，以应用计量公钥和私钥的示例代码如下。

{{< highlight java >}}

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

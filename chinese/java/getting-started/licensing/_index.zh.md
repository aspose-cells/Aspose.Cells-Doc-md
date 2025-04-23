---
title: 许可证
type: docs
weight: 50
url: /zh/java/licensing/
description: Aspose.Cells for JAVA提供不同的购买计划或提供免费试用和30天临时许可证以评估Java中的许可证和订阅政策。
keywords: Java从磁盘或流应用许可证。Java从磁盘或流设置许可证。在Aspose.Cells for Java中应用许可证。
---

## **如何在 Aspose.Cells 组件中应用许可证**

许可证是一个包含产品名称、许可给多少开发人员、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此不要修改文件; 即使在文件中无意添加额外的换行符也会使其失效。

如果要避免其评估限制，您需要在使用 Aspose.Cells 之前设置许可证。每个应用程序或进程只需要设置一次许可证。

许可证可以从流或文件中加载到以下位置：

1. 明确的路径。
1. 包含 Aspose.Cells.jar 的文件夹。

使用[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-)方法为组件授权。通常，设置许可证最简单的方法是将许可证文件放在与Aspose.Cells.jar相同的文件夹中，并只指定文件名（不包括路径），如下例所示：

### **如何从磁盘应用许可证**

在此示例中，**Aspose.Cells** 将尝试在包含应用程序 JAR 的文件夹中查找许可证文件。

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

### **如何在 Aspose.Cells.GridWeb 中应用许可证**

建议将许可证代码放在 Web 应用程序中应该首先处理的位置。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **如何应用计量许可证**

Aspose.Cells允许开发人员应用计量密钥。这是一种新的许可证机制。新的许可证机制将与现有的许可证方法一起使用。那些希望按照API功能的使用情况计费的客户可以使用计量许可证。有关更多详细信息，请参阅 [计量许可证常见问题解答](https://purchase.aspose.com/faqs/licensing/metered) 部分。

引入了一个新类 [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) 来应用按使用情况计费的密钥。以下是演示如何设置按使用情况计费的公钥和私钥的示例代码。

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
{{< app/cells/assistant language="java" >}}

---
title: Licensing
type: docs
weight: 50
url: /java/licensing/
description: Aspose.Cells for Java provides different plans for purchase or offers a free trial and a 30‑day Temporary License for evaluation using Licensing and Subscription policies in Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to Apply a License in Aspose.Cells Component**

The license is a plain text XML file that contains details such as the product name, number of developers it is licensed to, subscription expiry date and so on. The file is digitally signed, so do not modify the file; even the inadvertent addition of an extra line break into the file will invalidate it.

You need to set a license before utilizing Aspose.Cells if you want to avoid its evaluation limitations. You are only required to set a license once per application or process.

The license can be loaded from a stream or file in the following locations:

1. Explicit path.  
2. The folder that contains the Aspose.Cells.jar.

Use the [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-) method to license the component. Often the easiest way to set a license is to put the license file in the same folder as Aspose.Cells.jar and specify just the file name without path as shown in the following example:

### **How to Apply a License from Disk**

In this example **Aspose.Cells** will attempt to find the license file in the folder that contains the JARs of your application.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **How to Apply a License from Stream**

Initializes a license from a stream.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **How to Apply a License in Aspose.Cells.GridWeb**

It's recommended to put the licensing code at a place in your web application where it should be processed first.

{{< highlight csharp >}}

//Instantiate a license object and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **How to Apply Metered License**

Aspose.Cells allows developers to apply a metered key. It is a new licensing mechanism. The new licensing mechanism will be used along with the existing licensing method. Those customers who want to be billed based on the usage of the API features can use the metered licensing. For more details, please refer to [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.

A new class [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) has been introduced to apply a metered key. Following is the sample code demonstrating how to set metered public and private keys.

{{< highlight java >}}

//Set metered public and private keys

Metered metered = new Metered();

//Call the setMeteredKey method and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the consumption quantity again which should be greater by a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}

---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /java/aspose-cells-java-for-jython/
---

## **Introduction**

### **What is Jython?**

Jython is a Java implementation of Python that combines expressive power with clarity. Jython is freely available for both commercial and non-commercial use and is distributed with source code. Jython is complementary to Java and is especially suited for the following tasks:

- **Embedded scripting** - Java programmers can add the Jython libraries to their system to allow end users to write simple or complicated scripts that add functionality to the application.
- **Interactive experimentation** - Jython provides an interactive interpreter that can be used to interact with Java packages or with running Java applications. This allows programmers to experiment and debug any Java system using Jython.
- **Rapid application development** - Python programs are typically 2-10X shorter than the equivalent Java program. This translates directly to increased programmer productivity. The seamless interaction between Python and Java allows developers to freely mix the two languages both during development and in shipping products.

### **Aspose.Cells for Java**

Aspose.Cells for Java is an advanced class library for Java that enables you to perform a great range of document processing tasks directly within your Java
applications.

Aspose.Cells for Java supports processing Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF and all image formats. With Aspose.Cells you can
generate, modify, and convert documents without using Microsoft Cells.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jython is a project that demonstrates / provides the Aspose.Cells for Java API usage examples in Jython.

## **System Requirements and Supported Platforms**

### **System Requirements**

**Following are the system requirements to use Aspose.Cells Java for Jython:**

- Java 1.5 or above installed
- Downloaded Aspose.Cells component
- Jython 2.7.0

### **Supported Platforms**

**Following are the supported platforms:**

- Aspose.Cells 15.4 and above.
- Java IDE (Eclipse, NetBeans ...)

## **Download Installation and Usage**

### **Downloading**

**Download Examples from social coding websites**

Following releases of running examples are available to download on all of the below mentioned social coding sites:

- [CodePlex](http://asposecellsjavajython.codeplex.com/releases/view/619599)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Download Aspose.Cells for Java component**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

### **Installing**

- Place downloaded Aspose.Cells for Java jar file into "lib" directory.
- Replace "your-lib" with the downloaded jar filename in _*init*_.py file.

### **Using**

You can create HelloWorld document using following example code:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Support, Extend and Contribute**

### **Support**

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.Cells Java for Jython using any of the following platforms:

- [CodePlex](https://asposewordsjavajython.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposewords/Aspose_Words_Java/issues)

### **Extend and Contribute**

Aspose.Cells Java for Jython is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and contribute by suggesting or adding new feature or improving the existing ones, so that others could also benefit from it.

### **Source Code**

You can get the latest source code from one of the following locations

- [CodePlex](http://asposecellsjavajython.codeplex.com/releases/view/619599)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

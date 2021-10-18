---
title: Comparing VSTO with Aspose.Cells for .NET
type: docs
weight: 20
url: /net/comparing-vsto-with-aspose-cells-for-net/
---

{{% alert color="primary" %}}

This article compares using VSTO (Visual Studio Tools for Office) with other approaches for developing Microsoft Office-based solutions. In particular, it looks at Aspose.Cells and provides a comparison of how the two solutions work. The articles gives information developers can use to analyze, compare and evaluate different options before adopting a solution.

{{% /alert %}}

## **Overview**

Microsoft Excel is used widely by businesses and individuals in all kinds of industries. The spreadsheet application is close to ubiquitous and allows users not just to store and organize data, but build complex models with formulae and present data clearly with advanced formatting and chart.

VSTO allows Microsoft Office documents to execute code wrapped in a .NET assembly. It is used to develop applications that work with Microsoft Office files and features. Developers have used ASP, Office Web components and COM interop in applications for years. Microsoft has enhanced VSTO to make developing and deploying applications and improve memory management. But, the question remains: is VSTO designed to be easier to use and more reliable than other approaches available today? Developers want to work with solutions that won't let them down in terms of improved performance, security, scalability, stability, reliability or features.

[Aspose](http://www.aspose.com/) provides a great line of .NET, Java, Cloud and Android APIs. Aspose APIs include products such as Aspose.Cells, Aspose.Words, Aspose.Pdf, and Aspose.Slides, APIs that help[ developers open, modify, generate, save, merge, and convert documents in various formats including XLS, XLSX, DOC, DOCX, HTML, PDF, PPT.

In this article, we compare VSTO with Aspose.Cells for .NET.

[Aspose.Cells](https://products.aspose.com/cells/net/) is an independent Microsoft Excel spreadsheet manipulation API that reads and writes Microsoft Excel spreadsheets without Microsoft Excel installed on the client or server side. Aspose.Cells is feature rich component and offers much more than just basic data export. With Aspose.Cells developers can export data, format spreadsheets, import images, import create and manipulate charts, stream Excel data, and save to various formats. To find out more about the product and its features:

- Check out the [Aspose.Cells documentation](https://docs.aspose.com/cells/net/).
- See how it works in the [online demos](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
- Try it out: [download](https://downloads.aspose.com/cells/net) an evaluation version for free.

This article compares VSTO and Aspose.Cells on different aspects related to Microsoft Excel. The list is not complete but it represents a few issues that decision makers must understand before making a final decision before adopting an approach.

### **.NET Framework Requirement**

VSTO requires the .NET Framework (including Visual Studio Tools for Office SE Runtime) on the client side to execute the final application. In most corporate environments, especially in web scenarios, end-users cannot install application software and the related run-time frameworks. This requirement alone makes VSTO-based applications problematic. It practically rules out off-the-shelf applications based on VSTO.

On the contrary, Aspose.Cells for .NET does not necessarily demand the .NET Framework on the client side for the underlying scenario. The Office applications built with the component are light-weight and guaranteed to work on Microsoft Windows systems under significant load.

### **Features**

The features that VSTO provide depend on which combination of VSTO and Visual Studio products you have installed. Common tasks performed by VSTO for Microsoft Office Excel 2003 include adding data to Cells, creating, opening and saving workbooks, adding, moving and hiding worksheets, protecting worksheets, named ranges, list object, styles formatting, searching text in cells, sorting data, printing and Excel formula calculations.

Aspose.Cells provides everything necessary to manage Microsoft Office Excel files plus much, much more. The API gives developers great results with the least amount of effort. Aspose.Cells provides many powerful, time saving functions. the API provides easy-to-use APIs for all types of spreadsheet management activities, covering almost all the features Microsoft Excel provides. All the tasks listed for VSTO can easily be performed by Aspose.Cells.

Aspose.Cells also supports several advanced features, including support for Smart Markers, importing and exporting data to and from a number of data sources, objects and Excel files, support for COM clients (ASP client) Interoperability with the component, converting Excel files to PDF format, saving Excel charts and worksheets as image files.

### **Security**

By default, VSTO applications require Full Trust permissions for execution as it does not allow partially trusted callers. To lock down a web application and provide an additional level of application isolation in a hosted environment, you can use code access security to restrict the resources the application can access and the privileged operations it can perform. But you need to invest some time and effort to understand .NET security.

Internet Service Providers (ISPs) that host multiple applications from many different companies frequently use the medium trust level to help ensure that applications cannot read each other's data or interfere with one another. For security reasons, the ISPs may limit individual web applications on shared servers to Partial Trust.

Aspose.Cells for .NET can run under Medium Trust security level. No special privileges are required to run the assembly in a hosted environment. Medium trust places restrictions on the types of shared system resources that the applications can access. Many web applications are running in Web Hosting servers. In web hosting mode, most of them can only run under Medium Trust security level. Aspose.Cells for .NET can serve their need very well in this regard.

### **Performance**

Performance is the most critical factor when choosing any approach or methodology to build a solution.

The performance of a VSTO application falls back on VBA and COM approaches according to some user's report. There are several factors that influence VSTO performance, and it is important to put these factors in perspective.

- The .NET start up cost is inherently expensive. Applications written with .NET must incur the overhead of Just-In-Time (JIT) compilation, so the JIT compilation cannot be avoided.
- Another performance factor influencing VSTO-based applications has to do with the expense of calling through the thick layers of automation skin that wrap the Microsoft Office COM objects. VBA, built and optimized to interact with Microsoft Office, has a shorter distance to travel than .NET.
- Finally, hosting Excel objects in the Visual Studio IDE is expensive in terms of resources. VSTO applications have a larger memory footprint than VBA applications. VSTO Excel applications use a lot of memory, and never release it back to the OS until all instances of Microsoft Excel are closed.

If you are considering adopting VSTO as a development platform for Microsoft Office technology, spend some time looking into resources to get familiar with these attributes.

Moreover, the performance implication of always checking for updates may not be appropriate to the solution (slower deployment servers, slower network connections or simply being unable to reach the server frequently can negatively impact load times).

In contrast, Aspose.Cells for .NET is highly scalable, flexible and fast. Generally, Office applications were not designed to be simultaneously used by 100s and 1000s of users; however, Aspose.Cells is. The API is stable and can perform spreadsheet tasks flawlessly whether on a single server, powering a single application or on a load-balanced web farm powering an enterprise-wide application.

### **System Requirements**

Analyzing the system requirements for these two approaches, we find that VSTO is more expensive and need more essentials.

VSTO has a long list of pre-requisites:

- **Supported Operating Systems**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **.NET Framework versions supported**: only .NET framework 2.0 or greater.
- One or more of the following editions of Visual Studio Tools for Office:
  - Microsoft Visual Studio 2005 Tools for the Microsoft Office System
  - Microsoft Visual Studio 2005 Tools for the 2007 Microsoft Office System
  - Visual Studio 2008 Professional Edition
  - Visual Studio 2008 Team Suite Edition
  - One version of Microsoft Office:
  - Microsoft Office Professional 2003 SP1
  - 2007 Microsoft Office system

Aspose.Cells does not require Microsoft Excel to be installed either on the client or on the server, as it is a spreadsheet creation engine. To view Microsoft Excel documents, however, you need at least Microsoft Excel Viewer installed on the system.

- **Supported Operating Systems**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **.NET Framework versions supported**: all .NET frameworks are supported, 1.0, 1.1, 2.0, 3.x etc.

### **Installation and Deployment**

Installing VSTO can be a big and troublesome tasks. occasionally, an installation demands that you manually re-install aspects of the tools, and register them manually too. It can get complicated.

On the other hand, Aspose.Cells for .NET is packaged into a single DLL so there is no need to install additional apps. The component is only used by .NET applications and no portion of the component code is designed to wait on a human response. Just visit Aspose.Cells [download page](https://downloads.aspose.com/cells/net) and download the latest Aspose.Cells installer. Run the downloaded file and follow the installer instructions. Then, to use the component, reference it in your project.

## **Example Task**

To show the differences between the two approaches, the code below shows how to use both VSTO and Aspose.Cells APIs to fill a template file with data.

1. A Microsoft Excel file (TempBook.xls) is used as a template.
   The workbook contains a few worksheets with a few cells filled with data.
1. The example code puts 1000*20 records on the first worksheet in the template Excel file.
   The worksheet is filled with constant (dummy) data into the cells.

The task is performed on a system having Intel(R) Celeron(R) CPU 2.40 GHz, 760 MB of RAM on Microsoft Windows XP Professional operating system.

The code segments below illustrate how to perform these tasks with each API.

### **VSTO Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Aspose.Cells Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **Results**

The results showed that using VSTO API took about 2.5 minutes (approx. over 150 seconds) to finish the task while Aspose.Cells used less than 1 second on a common hardware with normal system configurations.

If the loop is extended, say to fill 10,000*20 cells, Aspose.Cells takes about 5.5 seconds to do the job.

## **Conclusion**

If you are considering to use a Microsoft Office technology in a business solution, first become familiar with alternatives available. Perform some tests based on different products and expose them to a variety of real world conditions such as load and stress to see how well they perform.

Aspose.Cells is a stable and mature product with worldwide customer base, and scalable enough to perform well under heavy loads.

The performance of VSTO is not refined yet. It is quite possible that some of these performance issues do not relate to VSTO itself rather have connections with .NET JIT compilation processes. But, still, there are certain doubts if the VSTO applications would be scaled themselves as the load increased. The newer model of VSTO does not require Excel to be resided on the web server for document processing but I think VSTO has a long way to go for making a real impact.

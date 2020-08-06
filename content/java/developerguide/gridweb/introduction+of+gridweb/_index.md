---
title : "Introduction of GridWeb" 
description : "" 
weight : 12325 
toc : false
type: docs
url: /java/developerguide/gridweb/introduction+of+gridweb/
---

# Aspose.Cells for Java : Introduction of GridWeb


{{< panel title="Contents Summary" style="primary" >}}
*   1 [How to run Aspose.Cells for GridWeb Java Demos](#how-to-run-aspose.cells-for-gridweb-java-demos)
    *   1.1 [Step by Step Guide to Run GridWeb Java Demos](#step-by-step-guide-to-run-gridweb-java-demos)
*   2 [Aspose.Cells.GridWeb - Demos](#aspose.cells.gridweb---demos)
*   3 [Browsers Capabilities and Aspose.Cells.GridWeb](#browsers-capabilities-and-aspose.cells.gridweb)
    *   3.1 [Comparison](#comparison)
{{< /panel >}}
 

 

## How to run Aspose.Cells for GridWeb Java Demos

Aspose.Cells for GridWeb Java demos are easy to run. You just need to deploy **gridwebdemo.war** in your web server. Please download the demos from this [link](https://forum.aspose.com/uploads/discourse_instance3/22292).

This article describes how to run Aspose.Cells for GridWeb Java Demos in Apache Tomcat Server.

### Step by Step Guide to Run GridWeb Java Demos

1.  Extract **apache-tomcat-7.0.52.zip** in any directory e.g C:\\Tomcat  
      
    ![image](5472644.png)  
      
    The following snapshot shows the extracted directories and files of the Apache Tomcat server  
      
    ![image](5472630.png)  
      
    You might also need to set the environment variable **CATALINA\_HOME**  
      
    ![image](5472631.png)
2.  Open the **tomcat-users.xml** file.  
      
    ![image](5472632.png)
3.  Add this user:
    
{{< code lang="cs" >}}
  <role rolename="manager-gui"/>
  <user username="tomcat" password="secret" roles="manager-gui"/>
{{< /code >}}
    
      
      
    **Here the user name is tomcat and the password is secret**  
    ![image](5472633.png)
    
4.  Run the **startup.bat** file.  
    It will run the Apache Tomcat Server.  
      
    ![image](5472634.png)  
      
    **Tomcat server running in a command window**  
    ![image](5472635.png)
5.  Now open the browser and type **localhost:8080**.  
    The Apache Tomcat web page is displayed.  
      
    **The Apache Tomcat web page**  
    ![image](5472636.png)
6.  Click **Manager App** and type user name and password. (As above: tomcat, secret)  
      
    ![image](5472637.png)
7.  Scroll down to the section **WAR file to deploy** and browse the **gridwebdemo.war** file.
8.  Click **Deploy**.  
      
    ![image](5472622.png)
9.  Browse **gridwebdemo.war** file.  
      
    ![image](5472623.png)
10.  Click **Deploy**.  
      
    ![image](5472624.png)
11.  Once it is deployed, click **/gridwebdemo** and start running demos.  
      
    ![image](5472626.png)  
    The GridWeb Demo page is displayed.  
      
    **The GridWeb Demo page**  
    ![image](5472625.png)
12.  Click any demo and run it.  
      
    **Creating contents demo running**  
    ![image](5472627.png)  
      
    **Worksheets demo running**  
    ![image](5472628.png)  
      
    **HeaderBar and CommandButton demo running**  
    ![image](5472629.png)

## Aspose.Cells.GridWeb - Demos

To get you up and running quickly, we provide a number of code examples and demos that show how to use the Aspose.Cells.GridWeb API.

Please download the demos from the below link:  
[Aspose.Cells.GridWeb Demos](https://forum.aspose.com/uploads/discourse_instance3/22292)

## Browsers Capabilities and Aspose.Cells.GridWeb

Aspose.Cells.GridWeb is a GUI based web control that can be embedded in JSP web pages like other web controls. The most important thing about web control is providing cross-browser support. Aspose.Cells.GridWeb provides cross-browser support.

### Comparison

Aspose.Cells.GridWeb is fully supported on Microsoft's Internet Explorer (IE). However, on other browsers, it has minor limitations. This topic provides a detailed comparison of which features are supported by different browsers.

{{< table style="table-striped" >}}
|Client Side Features|Microsoft Internet Explorer|Google Chrome|Mozilla Firefox|Opera|
|:----|:----|:----|:----|:----|
|Context Menu of Cell|![tick](check.png)|![tick](check.png)|![tick](check.png)|![minus](forbidden.png)|
|Client Side Validation|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Double Click Event|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|DropDownList ( *ComboBox Mode* )|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|DropDownList ( *Popup Menu Mode* )|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Formula Input/Edit|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Freeze or Unfreeze Rows/Columns|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Hyperlinks ( *CellCommand Mode* )|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Hyperlinks ( *URL Mode* )|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Merge or Unmerge Cells|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Multiple Cells Copy/Paste|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Multiple Cells Input/Edit, Single Postback|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Number Format|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Sheet Paging|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Read-only Cells|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Read-only Rows/Columns|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Data Validation using Regular Expressions|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Resize Column Width|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Resize Row Height|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Insert/Delete Rows & Columns|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Scroll Content|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Scroll Sheet Tabs|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Set Borders of Cells|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
|Set Font Settings of Cells|![tick](check.png)|![tick](check.png)|![tick](check.png)|![tick](check.png)|
{{< /table >}}

![minus](forbidden.png) Context menu of a cell can only be activated by clicking the Client side menu button.


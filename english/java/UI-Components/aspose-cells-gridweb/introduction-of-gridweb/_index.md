---
title: Introduction of GridWeb
type: docs
weight: 10
url: /java/introduction-of-gridweb/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
## **Basics of GridWeb**
Aspose.Cells.GridWeb is a GUI‑based web control that can be embedded in JSP web pages or any HTML page in a Java server.  

It is easy and simple to use.  

It helps you to build an online web editor for spreadsheet files quickly.  

It also supports importing and exporting all kinds of spreadsheet format files, which are 100% compatible with Microsoft Excel files.

## **Aspose.Cells.GridWeb - Demos**

To get you up and running quickly, we provide a number of code examples and demos that show how to use the Aspose.Cells.GridWeb API.

Please download the demos from the below link:  
[Aspose.Cells.GridWeb Demos](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb)


## **How to run Aspose.Cells for GridWeb Java Demos**
{{% alert color="primary" %}} 

Aspose.Cells for GridWeb Java demos are easy to run. You just need to deploy **gridwebdemo.war** in your web server. Please download the demos from this [link](https://forum.aspose.com/uploads/discourse_instance3/22292).

This article describes how to run Aspose.Cells for GridWeb Java Demos in Apache Tomcat Server.

{{% /alert %}} 
### **Step by Step Guide to Run GridWeb Java Demos**
1. Extract **apache-tomcat-7.0.52.zip** in any directory, e.g., `C:\Tomcat`  

   ![todo:image_alt_text](introduction-of-gridweb_1.png)

2. The following snapshot shows the extracted directories and files of the Apache Tomcat server  

   ![todo:image_alt_text](introduction-of-gridweb_2.png)

3. You might also need to set the environment variable **CATALINA_HOME**  

   ![todo:image_alt_text](introduction-of-gridweb_3.png)

4. Open the **tomcat‑users.xml** file.  

   ![todo:image_alt_text](introduction-of-gridweb_4.png)

5. Add this user:

   {{< highlight java >}}
   <role rolename="manager-gui"/>
   <user username="tomcat" password="secret" roles="manager-gui"/>
   {{< /highlight >}}

   **Here, the username is `tomcat` and the password is `secret`.**  

   ![todo:image_alt_text](introduction-of-gridweb_5.png)

6. Run the **startup.bat** file. It will start the Apache Tomcat Server.  

   ![todo:image_alt_text](introduction-of-gridweb_6.png)

   **Tomcat server running in a command window**  

   ![todo:image_alt_text](introduction-of-gridweb_7.png)

7. Now open the browser and type **localhost:8080**. The Apache Tomcat web page is displayed.  

   **The Apache Tomcat web page**  

   ![todo:image_alt_text](introduction-of-gridweb_8.png)

8. Click **Manager App** and type the username and password. (As above: `tomcat`, `secret`)  

   ![todo:image_alt_text](introduction-of-gridweb_9.png)

9. Scroll down to the section **WAR file to deploy** and browse to the **gridwebdemo.war** file.  

10. Click **Deploy**.  

    ![todo:image_alt_text](introduction-of-gridweb_10.png)

11. Browse the **gridwebdemo.war** file.  

    ![todo:image_alt_text](introduction-of-gridweb_11.png)

12. Click **Deploy**.  

    ![todo:image_alt_text](introduction-of-gridweb_12.png)

13. Once it is deployed, click **/gridwebdemo** and start running demos.  

    ![todo:image_alt_text](introduction-of-gridweb_13.png)

    The GridWeb Demo page is displayed.  

    **The GridWeb Demo page**  

    ![todo:image_alt_text](introduction-of-gridweb_14.png)

14. Click any demo and run it.  

    **Creating contents demo running**  

    ![todo:image_alt_text](introduction-of-gridweb_15.png)

    **Worksheets demo running**  

    ![todo:image_alt_text](introduction-of-gridweb_16.png)

    **HeaderBar and CommandButton demo running**  

    ![todo:image_alt_text](introduction-of-gridweb_17.png)


## **Browsers Capabilities and Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb is a GUI‑based web control that can be embedded in JSP web pages like other web controls. The most important aspect of a web control is providing cross‑browser support. Aspose.Cells.GridWeb provides cross‑browser support.
### **Comparison**
Aspose.Cells.GridWeb is fully supported on Microsoft’s Internet Explorer (IE). However, on other browsers, it has minor limitations. This topic provides a detailed comparison of which features are supported by different browsers.

| **Client Side Features** | **Microsoft Internet Explorer** | **Google Chrome** | **Mozilla Firefox** | **Opera** |
| :- | :- | :- | :- | :- |
| Context Menu of Cell | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/cross >}} |
| Client Side Validation | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Double Click Event | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| DropDownList (*ComboBox Mode*) | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| DropDownList (*Popup Menu Mode*) | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Formula Input/Edit | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Freeze or Unfreeze Rows/Columns | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Hyperlinks (*CellCommand Mode*) | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Hyperlinks (*URL Mode*) | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Merge or Unmerge Cells | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Multiple Cells Copy/Paste | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Multiple Cells Input/Edit, Single Postback | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Number Format | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Sheet Paging | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Read‑only Cells | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Read‑only Rows/Columns | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Data Validation using Regular Expressions | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Resize Column Width | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Resize Row Height | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Insert/Delete Rows & Columns | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Scroll Content | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Scroll Sheet Tabs | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Set Borders of Cells | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
| Set Font Settings of Cells | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} |
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the client‑side menu button.

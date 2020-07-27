+++
title = "Introduction of GridWeb" 
description = "" 
weight = 12325 
+++

Aspose.Cells for Java : Introduction of GridWeb  

# Aspose.Cells for Java : Introduction of GridWeb


{{< panel title="Contents Summary" style="primary" >}}
*   1 [How to run Aspose.Cells for GridWeb Java Demos](#IntroductionofGridWeb-HowtorunAspose.CellsforGridWebJavaDemos)
    *   1.1 [Step by Step Guide to Run GridWeb Java Demos](#IntroductionofGridWeb-StepbyStepGuidetoRunGridWebJavaDemos)
*   2 [Aspose.Cells.GridWeb - Demos](#IntroductionofGridWeb-Aspose.Cells.GridWeb-Demos)
*   3 [Browsers Capabilities and Aspose.Cells.GridWeb](#IntroductionofGridWeb-BrowsersCapabilitiesandAspose.Cells.GridWeb)
    *   3.1 [Comparison](#IntroductionofGridWeb-Comparison)
{{< /panel >}}
 

 

## How to run Aspose.Cells for GridWeb Java Demos

Aspose.Cells for GridWeb Java demos are easy to run. You just need to deploy **gridwebdemo.war** in your web server. Please download the demos from this [link](https://forum.aspose.com/uploads/discourse_instance3/22292).

This article describes how to run Aspose.Cells for GridWeb Java Demos in Apache Tomcat Server.

### Step by Step Guide to Run GridWeb Java Demos

1.  Extract **apache-tomcat-7.0.52.zip** in any directory e.g C:\\Tomcat  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472644.png)  
      
    The following snapshot shows the extracted directories and files of the Apache Tomcat server  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472630.png)  
      
    You might also need to set the environment variable **CATALINA\_HOME**  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472631.png)
2.  Open the **tomcat-users.xml** file.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472632.png)
3.  Add this user:
    
{{< code lang="cs" >}}
  <role rolename="manager-gui"/>
  <user username="tomcat" password="secret" roles="manager-gui"/>
{{< /code >}}
    
      
      
    **Here the user name is tomcat and the password is secret**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472633.png)
    
4.  Run the **startup.bat** file.  
    It will run the Apache Tomcat Server.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472634.png)  
      
    **Tomcat server running in a command window**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472635.png)
5.  Now open the browser and type **localhost:8080**.  
    The Apache Tomcat web page is displayed.  
      
    **The Apache Tomcat web page**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472636.png)
6.  Click **Manager App** and type user name and password. (As above: tomcat, secret)  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472637.png)
7.  Scroll down to the section **WAR file to deploy** and browse the **gridwebdemo.war** file.
8.  Click **Deploy**.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472622.png)
9.  Browse **gridwebdemo.war** file.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472623.png)
10.  Click **Deploy**.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472624.png)
11.  Once it is deployed, click **/gridwebdemo** and start running demos.  
      
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472626.png)  
    The GridWeb Demo page is displayed.  
      
    **The GridWeb Demo page**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472625.png)
12.  Click any demo and run it.  
      
    **Creating contents demo running**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472627.png)  
      
    **Worksheets demo running**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472628.png)  
      
    **HeaderBar and CommandButton demo running**  
    ![](https://docs2.aspose.com/cells/java/attachments/5276809/5472629.png)

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
|Context Menu of Cell|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(minus)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/forbidden.png)|
|Client Side Validation|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Double Click Event|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|DropDownList ( *ComboBox Mode* )|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|DropDownList ( *Popup Menu Mode* )|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Formula Input/Edit|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Freeze or Unfreeze Rows/Columns|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Hyperlinks ( *CellCommand Mode* )|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Hyperlinks ( *URL Mode* )|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Merge or Unmerge Cells|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Multiple Cells Copy/Paste|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Multiple Cells Input/Edit, Single Postback|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Number Format|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Sheet Paging|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Read-only Cells|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Read-only Rows/Columns|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Data Validation using Regular Expressions|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Resize Column Width|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Resize Row Height|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Insert/Delete Rows & Columns|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Scroll Content|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Scroll Sheet Tabs|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Set Borders of Cells|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
|Set Font Settings of Cells|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|![(tick)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/check.png)|
{{< /table >}}

![(minus)](s/en_GB-1988229788/4108/b47156ace146e4f759b49ef98258cb637bdd5af8.5/_/images/icons/emoticons/forbidden.png) Context menu of a cell can only be activated by clicking the Client side menu button.

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extract-apache-tomcat.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473420.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extracted-directories.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473394.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [environment-variable.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472631.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-users.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473396.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-added-user.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473411.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [startup-batch-file.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473408.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-server-running.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472635.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [apache-tomcat-webpage.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472636.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [manager-app.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472637.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [deploy-war-file.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472622.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [deploy-war-file-1.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472623.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [deploy-war-file-2.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472624.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [gridwebdemo-page.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472625.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [click-gridwebdemo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472626.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [creating-contents-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473419.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [worksheets-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473395.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [headerbar-commandbutton-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473393.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [creating-contents-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473398.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extract-apache-tomcat.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473397.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extracted-directories.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473400.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [headerbar-commandbutton-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473402.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-users.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473401.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [worksheets-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473404.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [creating-contents-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473409.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extract-apache-tomcat.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473403.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extracted-directories.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473399.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extracted-directories.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473405.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [headerbar-commandbutton-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473407.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-users.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473412.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [worksheets-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473410.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extract-apache-tomcat.png](https://docs2.aspose.com/cells/java/attachments/5276809/5473406.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extract-apache-tomcat.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472644.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [extracted-directories.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472630.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [startup-batch-file.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472634.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [headerbar-commandbutton-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472629.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [creating-contents-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472627.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [worksheets-demo.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472628.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-added-user.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472633.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [tomcat-users.png](https://docs2.aspose.com/cells/java/attachments/5276809/5472632.png) (image/png)  


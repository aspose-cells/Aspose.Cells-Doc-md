---
title : "Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005" 
description : "" 
weight : 20350 
toc : false
type: docs
url: /net/developerguide/technicalarticles/gridcontrols/databinding/binding+a+worksheet+with+database+using+worksheets+designer+in+vs.net+2005/
---

# Aspose.Cells for .NET : Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005


This article discusses an easiest approach to bind worksheets with database tables in **Visual Studio.Net 2005** using a special tool supplied with Aspose.Cells.GridWeb named as **Worksheets Designer** . This article would definitely make you feel that how easier it is to use data binding feature in Aspose.Cells.GridWeb with the help of **Worksheets Designer** .

##### *Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005  
*

The purpose of this article is to let all developers learn how you can create a data binding application in **VS.Net 2005** and understand the use & role of **Worksheets Designer** editor. The best way to learn and understand anything is through examples. So, in this article, it would also be best for us to create a sample application for demonstrating the use of **Worksheets Designer** in binding worksheets with database. Let's create an application step by step.

##### *Step 1: Creating a Sample Database  
*

First of all we will create a sample database that will be used in this article. We have used MS Access to create a sample database containing **Products** table whose schema is shown below:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112981.png)  

**Figure:** Design information of **Products** table

Few dummy records are added to the **Products** table as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112982.png)  

**Figure:** Records in **Products** table

##### *Step 2: Designing Sample Application  
*

An **ASP.NET Web Application** is created and designed in Visual Studio.NET 2005 as shown in the figures below. These screen shots are usefull for those developers who are not much familiar using Aspose.Cells.GridWeb in Visual Studio.Net 2005.

First start VS.Net 2005.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112983.png)  

**Figure:** Starting VS.Net 2005

Create a new Web Site from the File|New|Web Site... Menu.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112984.png)  

**Figure:** Creating a new WebSite

After clicking File|New|Web Site... menu option, **New Web Site** dialog is shown. Click the **Browse** button in it.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112985.png)  

**Figure:** New Web Site Dialog

After clicking the **Browse** button, choose the location folder in the local IIS. You may create a new folder and make it as virtual folder as shown in the figure.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112987.png)  

**Figure:** Creating a new Folder

  
After clicking the **Open** button in the **Choose Location** dialog, **New Web Site** dialog will look like.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112986.png)  

**Figure:** Setting Project Location

Now the project is created  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112989.png)  

**Figure:** Created Project

##### *XHTML and HTML Modes  
*

**Aspose.Cells.GridWeb** completely supports XHTML Mode which is implemented by default in VS.Net 2005 since the **XhtmlMode** property of the **GridWeb** control is set to **True** by default when you place the control on the web page. But if you want to implement HTML Mode for the control in VS.Net 2005, you may do it quite easily. You have to modify the **<!DOCTYPE>** tag a bit in the source code of the web page and set the **XhtmlMode** property of the **GridWeb** control to **False** .

#### *In this topic we will use HTML Mode for the control. So follow the steps below  
*

##### *1\. Switch to Source view of the web page and find the following <!DOCTYPE> tag in the source code.  
*

**[XML](/pages/createpage.action?spaceKey=cellsnet&title=XML&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 
{{< /code >}}

Once you find that tag, select that complete tag in the source code as shown below.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112988.png)  

**Figure:** Selecting **<!DOCTYPE> tag**

Replace the **<!DOCTYPE>** tag from your source code with the following one.

**[XML](/pages/createpage.action?spaceKey=cellsnet&title=XML&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 
 
{{< /code >}}

  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112991.png)  
**Figure:** Modifying **<!DOCTYPE> tag**

##### *2\. After you will add the GridWeb control to the web form. You should select the control and choose the XhtmlMode property from the Properties window to set it to False.  
*

**Adding GridWeb to the WebForm**

Right-Click on **ToolBox** and select **Choose Items...** from the menu.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112990.png)  

**Figure:** Choosing Items

Now select **GridWeb** component and click **OK**

  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112993.png)  
**Figure:** Selecting **GridWeb** component in the component dialog

Now the **GridWeb** is added as show in the figure below.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112992.png)  

**Figure:** **GridWeb** is added in the toolbox

Place the **GridWeb** on the web form as shown below.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112995.png)  

**Figure:** Placing **GridWeb** on the web page

**Procedure** : Select the control, Now, choose the **XhtmlMode** property from the **Properties** window and set it to **False** value.

##### *Step 3: Connecting with Database Using Server Explorer and Setting Connection Object  
*

First we add the MS Access database to the project which we previously created in **Step 1** . You may see that **db.mdb** file is added to the project.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112994.png)  

**Figure:** Added database to the project folder

Now, we go to **Component Designer** window of the web form using the web page's right-click menu option.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112997.png)  

**Figure:** Selecting **View Component Designer** option

The Component Designer window is shown as below.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112996.png)  

**Figure:** Component Designer Window

Double-Click the **OleDbConnection** component from Data panel to place oleDbConnection1 object to window.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112999.png)  

**Figure:** oleDbConnection1 object

Now, it's time to connect with the database. We can do it easily by using **Server Explorer** in Visual Studio.NET 2005. Just select **Data Connection** in **Server Explorer** and right click. You will see a context menu appearing in front of you. Select **Add Connection...** option from the menu as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112998.png)  

**Figure:** Selecting **Add Connection...** option from menu

  
After selecting **Add Connection...** option from menu, **Add Connection** dialog will be opened and **Browse** to select the database file as shown below.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5113001.png)  

**Figure:** Selecting the database file

You may test the Connection.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5113000.png)  

**Figure:** Testing the connection

You may browse the connection to check the table and its fields.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112944.png)  

**Figure:** Checking the table and its fields of the connection

Now if you select **oleDbConnection1** object in the **Component Designer** window, you may select the connection string related the existing connection which is just created, it is there in the "ConnectionString" property of the **oleDbConnection1** object in the Properties window.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112945.png)  

**Figure:** Selecting the connection string for the object

Finally the object's modifier is changed to **Protected** for better accessibility.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112942.png)  

**Figure:** Setting the modifier of the object

##### *Step 4: Configuring Data Adapter Object  
*

Now, add an **OleDbDataAdapter** component from the Data panel in the toolbox to configure it. Double-Click the **OleDbDataAdapter** in the Data panel of the toolbox, it will start its configuration wizard and select the existing connection as shown in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112943.png)  

**Figure:** Data Adapter Configuration Wizard

After clicking **Next** button, click the **Query Builder** to add the **Products** table, select All Columns and click **OK** button.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112940.png)  

**Figure:** Adding Product table  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112941.png)  

**Figure:** Query Builder

Now click **Finish** button to finish the wizard.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112938.png)  

**Figure:** Finishing the Wizard

After configuring the wizard, the oleDbDataAdapter1 is automatically added to the window as shown below. Also, you may set its modifier to **Protected** .  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112939.png)  

**Figure:** Retrieving the OleDbDataAdapter object on the designer window

##### *Step 5: Generating DataSet  
*

As we have created database connection and data adapter objects but still we need something where we can store data after conencting with database. A **DataSet** object can store data precisely and we can also generate it easily using VS.NET 2005 IDE. To do so, select **oleDbDataAdaper1** and right click. A context menu would be popped up with some options. Select **Generate** **DataSet...** option from the menu as shown below in the figure.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112952.png)  

**Figure:** Selecting **Generate** **DataSet...** option from menu

After selecting **Generate** **DataSet...** option from menu, a **Generate DataSet** dialog would be opened. Using this dialog, we can select that what would be the name of the new **DataSet** object to be created and which tables should be added to **DataSet** . Check **Add this dataset to designer** option and click **OK** button as shown below in the figure.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112953.png)  

**Figure:** Clicking **OK** button to generate **DataSet**

Now, you can see a **dataSet11** object added to designer as shown below in the figure. Set the object modifier to **Protected** .  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112950.png)  

**Figure:** **DataSet** generated and added to the designer window

Certain code is automatically generated in the .cs file related connection, data adapter, dataset object.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112951.png)  

**Figure:** Generated Code

##### *Step 6: Using Worksheets Designer  
*

Now, its time to open the secret. Select the control and right click. A context menu would be opened. Select Worksheets Designer... option from the menu as shown below in the figure.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112948.png)  

**Figure:** Selecting **Worksheets Designer...** option from menu

After that **Worksheet Collection Editor** dialog (also called **Worksheets Designer** ) will be opened, you can see several properties that can be configured to bind the **Sheet1** with any table in the database. Let's select **DataSource** property. Write **dataSet11** in it (that we generated and added to designer window in previous step). Then click on **DataMember** property. Write **Products** as a table name here as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112949.png)  

**Figure:** Setting **DataSource** and **DataMember** properties

Now, you can configure **BindColumns** property. After clicking it, Now you may add the binding columns and set the **Caption** , **DataField** (It should be same as **Products** table fields), and other properties. You can set the **IsAutoCreated** to **true** and apply **Validation** and set the **NumberType** of different fields for your requirements.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112946.png)  

**Figure:** Clicking **BindColumns** property  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112947.png)  

**Figure:** **BindColumn Collection Editor** dialog

##### *Step 7: Adding Some Lines of Code for the Web Page  
*

We have used **Worksheets Designer** easily and now we just have to add some lines of code

First we will add **OnInit** event related code to instialize **InitializeComponent** method to intialize and create connection, command, dataadapter and dataset objects. These lines of code are not added with the auto generated code, so we have to add them manually.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112961.png)  

**Figure:** Adding some code1  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112960.png)  

**Figure:** Adding some code2

Now we add some code in the **Page\_Load** event handler for filling **dataSet11** object with data from database (using **oleDbDataAdapter1** ) and binding **GridWeb** control with **dataSet11** by calling its **DataBind** method.

##### *Example:  
*

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
//Implementing Page_Load event handler
protected void Page_Load(object sender, EventArgs e)
{
    //Checking if there is not any PostBack
    if (!IsPostBack)
    {
        try
        {
            //Filling DataSet with data 
            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet
            GridWeb1.DataBind();
        }
        finally
        {
            //Finally, closing database connection
            oleDbConnection1.Close();
        }
    }
}
 
{{< /code >}}

**[VB.NET](/pages/createpage.action?spaceKey=cellsnet&title=VB.NET&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
'Implementing Page_Load event handler
Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

    'Checking if there is not any PostBack
    If Not IsPostBack Then
        Try
            'Filling DataSet with data 
            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet
            GridWeb1.DataBind()
        Finally
            'Finally, closing database connection
            oleDbConnection1.Close()
        End Try
    End If
End Sub
 
{{< /code >}}

You can also check the code added to **Page\_Load** event handler as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112959.png)  

**Figure:** Code added to **Page\_Load** event handler

By far, we have built a very useful database application. But, this application only enables you to view the data of the table. Although you can edit data in **GridWeb** control but when you will close your browser window and open your database. You would find that nothing is changed. It means, the changes that you made are not saved to the database. So, there is something that you have to do.

Now we will add some code to our application so that **GridWeb** may save its changes to actual database. Let's open **Properties** pane and select **SaveCommand** event of the **GridWeb** control from the list of its events. If you double click on **SaveCommand** event then VS.NET 2005 IDE will create **GridWeb1\_SaveCommand** event handler for you. Add some code to this event handler for updating database with modified data contained in **DataSet** (bound with the worksheet) using **oleDbDataAdapter1** .

##### *Example:  
*

**[C#](/pages/createpage.action?spaceKey=cellsnet&title=C&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
//Implementing the event handler for SaveCommand event
protected void GridWeb1_SaveCommand(object sender, EventArgs e)
{
    try
    {
        //Getting the modified data of worksheet as a DataSet
        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet
        oleDbDataAdapter1.Update(dataset);
    }
    finally
    {
        //Closing database connection
        oleDbConnection1.Close();
    }
}
 
{{< /code >}}

**[VB.NET](/pages/createpage.action?spaceKey=cellsnet&title=VB.NET&linkCreation=true&fromPageId=5017582)**

{{< code lang="cs" >}}
'Implementing the event handler for SaveCommand event
Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)
  Handles GridWeb1.SaveCommand
    Try
        'Getting the modified data of worksheet as a DataSet
        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet
        oleDbDataAdapter1.Update(dataset)
    Finally
        'Closing database connection
        oleDbConnection1.Close()
    End Try
End Sub
 
{{< /code >}}

You can also check the code added to **GridWeb1\_SaveCommand** event handler as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112958.png)  

**Figure:** Code added to **GridWeb1\_SaveCommand** event handler

Now, if you will save your changes to database using **Save** button of the **GridWeb** , they would definitely be saved.

##### *Step 8: Running Your Application  
*

Finally, we can compile and run our application by either pressing **Ctrl+F5** or clicking **Start** button. In the debugging dialog, you may specify appropriate debugging option and click **OK** button as shown below in the figure.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112957.png)  

**Figure:** Running application

After compilation, **Default.aspx** page of our web application will be opened in a new browser window where we can see all data loaded from database as shown below:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112956.png)  

**Figure:** Data loaded into **GridWeb** control from database

When data is loaded into **GridWeb** control then you would feel that Aspose.Cells.GridWeb provides an implicit control of data to its users. Let's check that what kind of data manipulation features are offered by **GridWeb** to its users.

##### *Data Validation  
*

Aspose.Cells.GridWeb automatically creates appropriate validation rules for all bound columns according to their data types defined in the database. You can see the validation type of a cell by hovering your mouse pointer on it as shown below in the figure:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112955.png)  

**Figure:** Checking validation type of a cell

In the above figure, we can see that selected cell contains **<INT>** type of validation, which means that users can only enter integer value to it otherwise a validation error will occur. Moreover, **<REQUIRED>** shows that the value of **Product ID** is required to be submitted by user.

##### *Deleting Rows  
*

To delete a row, you should first select a row (or any cell of the row) and select **Delete Row** option from right click menu as shown below:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112954.png)  

**Figure:** Selecting **Delete Row** option from menu

After selecting **Delete Row** from menu, the row is deleted from the **GridWeb** . Now click **save** button of the **GridWeb** to delete that record in the original database table.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112969.png)  

**Figure:** Grid data (after a row is deleted)

##### *Editing Rows  
*

You may also edit data in cells or rows and then click **Save** button to save your changes.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112968.png)  

**Figure:** Grid data (Editing Record1)  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112967.png)  

**Figure:** Grid data (Editing Record2)

##### *Adding Rows  
*

To add a row, select **Add Row** option from right click menu as shown below:  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112966.png)  

**Figure:** Selecting **Add Row** option from menu

A new row will be added to sheet at the end of the rows after selecting **Add Row** option from the menu. At the left of the newly added row, you would notice an **asterisk** mark, indicating that the row is a newly added.  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112965.png)  

**Figure:** New row added to Grid

After input the values in the new row, click **Save** button to confirm the changes in the original database table as shown below  
  
![](https://docs2.aspose.com/cells/net/attachments/5017582/5112964.png)  

**Figure:** Saving changes to database table by clicking **Save** button

##### *Conclusion  
*

**Data Binding** is an important feature of Aspose.Cells.GridWeb . It's really effortless for developers to bind their worksheets with database using **Worksheets Designer** utility offered by Aspose.Cells.GridWeb . Aspose.Cells.GridWeb is very helpful for the developers to save their time and efforts in creating powerful Grid solutions.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-001.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112981.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-002.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112982.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-003.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112983.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-004.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112984.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-005.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112985.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-006.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112987.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-007.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112986.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-008.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112989.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-009.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112988.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-010.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112991.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-011.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112990.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-012.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112993.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-013.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112992.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-014.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112995.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-015.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112994.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-016.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112997.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-017.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112996.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-018.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112999.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-019.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112998.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-020.png](https://docs2.aspose.com/cells/net/attachments/5017582/5113001.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-021.png](https://docs2.aspose.com/cells/net/attachments/5017582/5113000.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-022.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112944.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-023.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112945.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-024.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112942.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-025.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112943.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-026.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112940.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-027.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112941.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-028.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112938.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-029.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112939.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-030.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112952.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-031.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112953.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-032.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112950.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-033.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112951.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-034.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112948.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-035.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112949.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-036.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112946.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-037.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112947.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-038.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112961.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-039.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112960.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-040.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112959.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-041.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112958.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-042.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112957.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-043.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112956.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-044.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112955.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-045.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112954.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-046.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112969.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-047.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112968.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-048.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112967.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-049.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112966.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-050.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112965.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Binding a Worksheet with Database Using Worksheets Designer in VS.Net 2005-051.png](https://docs2.aspose.com/cells/net/attachments/5017582/5112964.png) (image/png)  


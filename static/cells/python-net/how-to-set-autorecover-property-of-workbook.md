##How to set AutoRecover property of Workbook
You can use Aspose.Cells for Python via .NET to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables AutoRecover (Autosave) on that Excel file.
Aspose.Cells for Python via .NET provides [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) property to enable or disable this option.
The following code explains how to use  [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is **false** at this time.
## C# code to set the AutoRecover property of Workbook
## **Output**
Here is the console output of the above sample code.
AutoRecover: True
AutoRecover: False

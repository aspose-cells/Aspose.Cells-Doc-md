---
title: 在 VSTO 和 Aspose.Cells 中向工作簿添加新工作表并激活工作表
type: docs
weight: 30
url: /zh/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **迁移提示：**
1. 将新工作表添加到现有 Microsoft Excel 文件。
1. 将数据填充到每个新工作表的单元格中。
1. 激活工作簿中的工作表。
1. 另存为 Microsoft Excel 文件。

下面是 VSTO (C#) 和 Aspose.Cells for .NET (C#) 的并行代码片段，展示了如何完成这些任务。

**VSTO**

{{< highlight "csharp" >}}

//初始化应用对象

Excel.Application excelApp = 应用程序；

//指定模板excel文件路径。

string myPath = "Book1.xls";

//打开excel文件。

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值）；

//声明一个工作表对象。

Excel.Worksheet 新工作表；

//向工作簿中添加5个新工作表并填充一些数据

//进入细胞。

对于 (int i = 1; i< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 //实例化一个license实例并设置license文件

//通过它的路径

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Total.lic");

//指定模板excel文件路径。

string myPath = "Book1.xls";

//实例化一个新的工作簿。

//打开excel文件。

工作簿工作簿=新工作簿（myPath）；

//声明一个工作表对象。

工作表新工作表；

//向工作簿中添加5个新工作表并填充一些数据

//进入细胞。

对于 (int i = 0; i< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/下载)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\)。压缩）

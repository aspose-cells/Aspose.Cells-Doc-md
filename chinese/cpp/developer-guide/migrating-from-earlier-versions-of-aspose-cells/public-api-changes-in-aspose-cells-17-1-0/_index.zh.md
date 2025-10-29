---
title: Aspose.Cells 17.1.0 中的公共API更改
type: docs
weight: 20
url: /zh/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 中对于模块/应用程序开发者可能感兴趣的更改。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括对于 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **命名范围的支持**
Aspose.Cells for C++ 现在支持创建以及操作命名区域。 以下代码片段演示了如何使用 Aspose.Cells for C++ API [创建命名区域](/cells/zh/cpp/create-named-range-in-a-workbook/)。

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

除了创建新命名区域外，Aspose.Cells for C++ APIs 还支持操作现有命名区域。 以下代码片段使用 Aspose.Cells for C++ API 来[操作现有命名区域](/cells/zh/cpp/manipulate-named-range-in-a-workbook/)。

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **添加了 ICells::LinkToXmlMap 方法**
ICells 类中添加了 LinkToXmlMap 方法，用于链接 XML 映射。
### **添加了 ICells::ImportCSV 方法**
ICells 类中添加了 ImportCSV 方法，用于将 CSV 文件导入工作表的单元格中。
### **添加了 ICells::ImportTwoDimensionArray 方法**
ICells 类中添加了 GetIProtectedRangeCollection 方法，用于将二维数据数组导入工作表。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
IWorksheet 类中添加了 GetIProtectedRangeCollection 方法，用于检索 IProtectedRange 对象的集合。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
IWorksheet 类中添加了 GetIProtectedRangeCollection 方法，用于从工作表中检索编辑范围集合。
### **添加了 IWorkbookSettings::ClearPivottables 方法**
已将 ClearPivottables 方法添加到 IWorkbookSettings 类中，该方法有助于清除给定电子表格中的所有数据透视表。
### **添加了 IWorksheetCollection::CreateIRange 方法**
已将 CreateIRange 方法添加到 IWorksheetCollection 类中，该方法有助于通过字符串格式的单元格引用创建 IRange 对象。
### **添加了 IExternalLink::IsVisible 方法**
IsVisible 方法可获取 Excel 应用程序中外部链接的可见性状态。
### **添加了 GetScaleCrop 和 SetScaleCrop 方法**
Aspose.Cells for C++ 17.1.0 版本向 IBuiltInDocumentPropertyCollection 类公开了 GetScaleCrop 和 SetScaleCrop 方法。这些方法对于获取或设置 ScaleCrop 属性非常有用，该属性表示文档缩略图的显示模式。
### **添加了 GetLinksUpToDate 和 SetLinksUpToDate 方法**
Aspose.Cells for C++ 17.1.0 版本向 IBuiltInDocumentPropertyCollection 类公开了 GetLinksUpToDate 和 SetLinksUpToDate 方法。这些方法对于获取或设置 LinkUpToDate 属性非常有用，该属性指示文档中的超链接是否是最新的。
### **添加了 GetAbsolutePath 和 SetAbsolutePath 方法**
Aspose.Cells for C++ 17.1.0 版本向 IWorkbook 类公开了 GetAbsolutePath 和 SetAbsolutePath 方法。这些方法对于获取或设置文件的绝对路径非常有用，该路径只能用于外部链接。
### **添加了 GetFormula 和 SetFormula 方法**
此版本的 Aspose.Cells for C++ 已向 IListColumn 类公开了 GetFormula 和 SetFormula 方法。这些方法对于获取或设置列表列的公式非常有用。
### **添加了 GetCheckCompatibility 和 SetCheckCompatibility 方法**
此版本的 Aspose.Cells for C++ 已向 IWorkbookSettings 类公开了 GetCheckCompatibility 和 GetCheckCompatibility 方法。这些方法对于获取或设置兼容性检查属性非常有用，该属性指示 API 在保存工作簿时是否应检查兼容性。默认值为 true，如果应用程序要求不检查兼容性，则可以将其设置为 false。
### **添加了 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法**
Aspose.Cells for C++ 现已向 ILoadOptions 类公开了 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法。这些方法表示在读取模板文件时用于处理单元格数据的数据处理程序。
### **添加了 GetCultureInfo 和 SetCultureInfo 方法**
Aspose.Cells for C++ 现已向 ILoadOptions 类公开了 GetCultureInfo 和 SetCultureInfo 方法。这些方法能获取或设置文件加载时的系统区域信息。
## **删除了 API**
### **移除了 ICells::MaxDataRowInColumn 方法**
建议使用 ICells::GetLastDataRow 方法
### **移除了 ICell::GetConditionalIStyle 方法**
建议使用 ICell::GetIConditionalFormattingResult 方法
### **移除了 IPageSetup::GetDraft & SetDraft 方法**
建议使用 IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft 方法

{{% alert color="primary" %}} 

随着 Aspose.Cells for C++ 17.1.0 版本的发布，我们去除了一些未使用且被视为不必要的方法。以下是所有这些方法的列表。

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType 方法
- IRange::ToString 方法
- IRow::Equals 方法
- IWorkbook::SetISettings 方法
- ICell::ToString() 方法
- ICell::Equals(ObjectPtr) 方法
- ICell::GetHashCode 方法
- IWorksheet::ToString 方法

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}

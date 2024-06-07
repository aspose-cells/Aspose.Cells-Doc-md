---
title: Aspose.Cells 17.1.0 中的公共 API 变更
type: docs
weight: 20
url: /zh/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 变更，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括 Aspose.Cells 背后行为中的任何变化的描述。

{{% /alert %}} 
## **已添加API**
### **支持命名范围**
Aspose.Cells for C++现在支持创建和操作命名范围。以下代码片段展示了使用Aspose.Cells for C++ API来[在工作簿中创建命名范围](/cells/zh/cpp/create-named-range-in-a-workbook/)是多么简单。

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

除了创建新的命名范围，Aspose.Cells for C++ API还支持操作现有的命名范围。以下代码片段使用Aspose.Cells for C++ API来[操作现有的命名范围](/cells/zh/cpp/manipulate-named-range-in-a-workbook/)。

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
### **添加ICells::LinkToXmlMap方法**
已添加 LinkToXmlMap 方法到 ICells 类中，可用于将 XML 地图链接。
### **添加 ICells::ImportCSV 方法**
已添加 ImportCSV 方法到 ICells 类中，用于将 CSV 文件导入工作表的单元格中。
### **添加了 ICells::ImportTwoDimensionArray 方法**
已添加 GetIProtectedRangeCollection 方法到 ICells 类中，可用于将二维数据导入工作表。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
已添加 GetIProtectedRangeCollection 方法到 IWorksheet 类中，用于检索 IProtectedRange 对象集合。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
已添加 GetIProtectedRangeCollection 方法到 IWorksheet 类中，用于检索工作表中的编辑范围集合。
### **添加了 IWorkbookSettings::ClearPivottables 方法**
已添加 ClearPivottables 方法到 IWorkbookSettings 类中，可用于清除给定电子表格中的所有数据透视表。
### **添加了 IWorksheetCollection::CreateIRange 方法**
已添加 CreateIRange 方法到 IWorksheetCollection 类中，可用于通过传递字符串格式的单元格引用创建 IRange 对象。
### **添加了 IExternalLink::IsVisible 方法**
IsVisible 方法获取 Excel 应用程序中外部链接的可见性状态。
### **添加了 GetScaleCrop 和 SetScaleCrop 方法**
Aspose.Cells for C++ 17.1.0 已将 GetScaleCrop 和 SetScaleCrop 方法公开给 IBuiltInDocumentPropertyCollection 类。这些方法可用于获取或设置 ScaleCrop 属性，指示文档缩略图的显示模式。
### **添加了 GetLinksUpToDate 和 SetLinksUpToDate 方法**
Aspose.Cells for C++ 17.1.0 已向 IBuiltInDocumentPropertyCollection 类公开了 GetLinksUpToDate 和 SetLinksUpToDate 方法。这些方法用于获取或设置 LinkUpToDate 属性，指示文档中的超链接是否为最新。
### **添加了 GetAbsolutePath 和 SetAbsolutePath 方法**
Aspose.Cells for C++ 17.1.0 已向 IWorkbook 类公开了 GetAbsolutePath 和 SetAbsolutePath 方法。这些方法用于获取或设置文件的绝对路径，仅可用于外部链接。
### **添加了 GetFormula 和 SetFormula 方法**
Aspose.Cells for C++ 的此版本已向 IListColumn 类公开了 GetFormula 和 SetFormula 方法。这些方法用于获取或设置列表列的公式。
### **添加了 GetCheckCompatibility 和 SetCheckCompatibility 方法**
Aspose.Cells for C++ 的此版本已向 IWorkbookSettings 类公开了 GetCheckCompatibility 和 GetCheckCompatibility 方法。这些方法用于获取或设置兼容性检查属性，指示 API 保存工作簿时是否应检查兼容性。默认值为 true，如果应用程序要求不检查兼容性，则可以将其设置为 false。
### **添加了 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法**
Aspose.Cells for C++ 现在已向 ILoadOptions 类公开了 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法。这些方法表示在读取模板文件时处理单元格数据的数据处理程序。
### **添加了 GetCultureInfo 和 SetCultureInfo 方法**
Aspose.Cells for C++ 已向 ILoadOptions 类公开了 GetCultureInfo 和 SetCultureInfo 方法。这些方法可在加载文件时获取或设置系统区域设置信息。
## **已删除APIs**
### **删除了 ICells::MaxDataRowInColumn 方法**
建议使用ICells::GetLastDataRow方法。
### **移除ICell::GetConditionalIStyle方法**
建议使用ICell::GetIConditionalFormattingResult方法。
### **移除IPageSetup::GetDraft和SetDraft方法**
建议使用IPageSetup::GetPrintDraft和IPageSetup::SetPrintDraft方法。

{{% alert color="primary" %}} 

随着Aspose.Cells for C++ 17.1.0的发布，我们已删除了一些不再使用且被认为是不必要的方法。以下是所有此类方法的列表。

- IPaneCollection::GetAcitvePaneType和SetAcitvePaneType方法
- IRange::ToString方法
- IRow::Equals方法
- IWorkbook::SetISettings方法
- ICell::ToString()方法
- ICell::Equals(ObjectPtr)方法
- ICell::GetHashCode方法
- IWorksheet::ToString方法

{{% /alert %}}

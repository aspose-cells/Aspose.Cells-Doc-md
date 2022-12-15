---
title: 公共 API Aspose.Cells 17.1.0 的变化
type: docs
weight: 20
url: /zh/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 16.12.0 到 17.1.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持命名范围**
Aspose.Cells for C++ 现在支持命名范围的创建和操作。以下代码片段演示了使用 Aspose.Cells for C++ API 是多么简单[创建命名范围](/cells/zh/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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

除了创建新的命名范围外，Aspose.Cells for C++ API 还支持操作现有的命名范围。以下代码片段使用 Aspose.Cells for C++ API 来[操纵现有的命名范围](/cells/zh/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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
LinkToXmlMap 方法已添加到 ICells 类中，该方法在链接 XML 映射时很有用。
### **添加了 ICells::ImportCSV 方法**
ImportCSV 方法已添加到 ICells 类，这对于将 CSV 文件导入工作表的单元格非常有用。
### **添加了 ICells::ImportTwoDimensionArray 方法**
GetIProtectedRangeCollection 方法已添加到 ICells 类中，这对于将二维数据数组导入工作表非常有用。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
GetIProtectedRangeCollection 方法已添加到 IWorksheet 类中，该类可用于检索 IProtectedRange 对象的集合。
### **添加了 IWorksheet::GetIProtectedRangeCollection 方法**
GetIProtectedRangeCollection 方法已添加到 IWorksheet 类中，该类可用于从工作表中检索编辑范围集合。
### **添加了 IWorkbookSettings::ClearPivottables 方法**
ClearPivottables 方法已添加到 IWorkbookSettings 类，这对于从给定电子表格中清除所有数据透视表很有用。
### **添加了 IWorksheetCollection::CreateIRange 方法**
CreateIRange 方法已添加到 IWorksheetCollection 类，该类可用于通过传递字符串格式的单元格引用来创建 IRange 的对象。
### **添加了 IExternalLink::IsVisible 方法**
IsVisible 方法获取外部链接在 Excel 应用程序中的可见性状态。
### **添加了 GetScaleCrop 和 SetScaleCrop 方法**
Aspose.Cells for C++ 17.1.0 已将 GetScaleCrop 和 SetScaleCrop 方法公开给 IBuiltInDocumentPropertyCollection 类。这些方法对于获取或设置指示文档缩略图显示模式的 ScaleCrop 属性很有用。
### **添加了 GetLinksUpToDate 和 SetLinksUpToDate 方法**
Aspose.Cells for C++ 17.1.0 已将 GetLinksUpToDate 和 SetLinksUpToDate 方法公开给 IBuiltInDocumentPropertyCollection 类。这些方法对于获取或设置 LinkUpToDate 属性很有用，该属性指示文档中的超链接是否是最新的。
### **添加了 GetAbsolutePath 和 SetAbsolutePath 方法**
Aspose.Cells for C++ 17.1.0 已将 GetAbsolutePath 和 SetAbsolutePath 方法公开给 IWorkbook 类。这些方法对于获取或设置只能用于外部链接的文件的绝对路径很有用。
### **添加了 GetFormula 和 SetFormula 方法**
此版本 Aspose.Cells for C++ 公开了 IListColumn 类的 GetFormula 和 SetFormula 方法。这些方法对于获取或设置列表列的公式很有用。
### **添加了 GetCheckCompatibility 和 SetCheckCompatibility 方法**
此版本 Aspose.Cells for C++ 公开了 IWorkbookSettings 类的 GetCheckCompatibility 和 GetCheckCompatibility 方法。这些方法可用于获取或设置兼容性检查属性，指示 API 是否应在保存工作簿时检查兼容性。默认值为true，如果应用要求不需要检查兼容性，可以设置为false。
### **添加了 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法**
Aspose.Cells for C++ 现在公开了 ILoadOptions 类的 GetILightCellsDataHandler 和 SetILightCellsDataHandler 方法。这些方法表示在读取模板文件时处理单元格数据的数据处理程序。
### **添加了 GetCultureInfo 和 SetCultureInfo 方法**
Aspose.Cells for C++ 公开了 ILoadOptions 类的 GetCultureInfo 和 SetCultureInfo 方法。这些方法可以获取或设置文件加载时的系统文化信息。
## **删除的 API**
### **删除了 ICells::MaxDataRowInColumn 方法**
建议改用 ICells::GetLastDataRow 方法。
### **删除了 ICell::GetConditionalIStyle 方法**
建议改用 ICell::GetIConditionalFormattingResult 方法。
### **删除了 IPageSetup::GetDraft 和 SetDraft 方法**
建议改用 IPageSetup::GetPrintDraft 和 IPageSetup::SetPrintDraft 方法。

{{% alert color="primary" %}} 

随着 Aspose.Cells for C++ 17.1.0 的发布，我们删除了一些未使用的方法，因此被认为是不必要的。这是所有此类方法的列表。

- IPaneCollection::GetAcitvePaneType 和 SetAcitvePaneType 方法
- IRange::ToString 方法
- IRow::Equals 方法
- IWorkbook::SetISettings 方法
- ICell::ToString() 方法
- ICell::Equals(ObjectPtr) 方法
- ICell::GetHashCode 方法
- IWorksheet::ToString 方法

{{% /alert %}}

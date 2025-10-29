---
title: 智能导入带有智能标记的嵌套对象到Excel
type: docs
weight: 30
url: /zh/net/how-to-import-nested-objects-with-smart-markers/
---

## ** 为什么使用嵌套对象进行智能标记**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. 分层数据表示：实际数据本身就是嵌套的（例如，一个订单包含一个客户，客户有一个地址）。嵌套对象反映了这种结构，避免了扁平化/人工字段，如customer_city。
2. 避免命名冲突：扁平结构容易发生冲突（例如product_name与supplier_name）。嵌套保持命名自然：
<<product.name>> vs. <<supplier.name>>.
3. 模块化与重用：在不同场景中重用子对象，地址对象可以嵌入在客户、供应商或员工标记中。地址的更改会普遍传播。
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. 框架/工具支持：现代引擎（如Handlebars、React、FoxPro）自动解析嵌套路径。这与JSON/API中的嵌套数据标准一致。

## **如何使用智能标记导入匿名类型或自定义对象**
Aspose.Cells 还支持智能标记中的匿名类型或自定义对象。接下来的示例展示了这是如何工作的。如需使用智能标记从动态对象导入数据，请访问以下文章：

[将动态对象导入作为数据源](/cells/zh/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **如何使用智能标记导入嵌套对象**
Aspose.Cells支持智能标记中的嵌套对象，这些嵌套对象应该是简单的。我们使用一个简单的模板文件。查看包含一些嵌套智能标记的设计电子表格。

|**SM_NestedObjects.xlsx文件的第一个工作表显示嵌套智能标记。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下示例演示了其工作原理。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **如何使用智能标记将泛型列表作为嵌套对象导入**
Aspose.Cells现在还支持将通用列表用作嵌套对象。请查看生成的输出Excel文件的屏幕截图所用的代码。如屏幕截图所示，教师对象包含多个嵌套的学生对象。

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **如何批量导入非逐行的嵌套对象到Excel；使用智能标记**
当前默认的处理方法是逐行处理智能标记。但有时需要一起处理同一数据表的智能标记，无论它们是否在同一行中，那么在调用处理之前，您必须指定名称为“_CellsSmartMarkers”的命名范围，并将WorkbookDesigner.LineByLine指定为false。 
有时可能会需要在完成前获取有关正在处理的单元格引用或特定智能标记的通知。这可以通过WorkbookDesigner.CallBack属性和ISmartMarkerCallBack实现。

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}

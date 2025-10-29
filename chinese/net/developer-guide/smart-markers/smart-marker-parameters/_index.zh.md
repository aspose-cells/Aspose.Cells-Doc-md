---
title: 智能标记参数
type: docs
weight: 30
url: /zh/net/smart-marker-parameters/
---

## **设计器电子表格和智能标记**
设计者电子表格是包含可视格式、公式和智能标记的标准 Excel 文件。它们可以包含引用一个或多个数据源的智能标记，例如来自项目和相关联系人信息的信息。智能标记被写入您希望信息放入的单元格中。

所有智能标记都以 &= 开头。数据标记的示例是 &=Party.FullName。如果数据标记结果超过一个项，例如一个完整的行，则接下来的行会被自动移动下来以为新信息腾出空间。因此，可以在数据标记后的行上立即放置小计和总计，以便根据插入的数据进行计算。要在插入行上进行计算，使用**动态公式**。

智能标记由**数据源**和**字段名称**部分组成。还可以使用变量和变量数组传递特殊信息。变量始终只填充一个单元格，而变量数组可以填充多个单元格。每个单元格只使用一个数据标记。未使用的智能标记将被移除。

智能标记还可以包含参数。参数允许您修改信息的布局方式。它们以逗号分隔的列表形式附加在智能标记的末尾作为括号内。

## **智能标记选项**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **智能标记参数**
允许以下参数：

- **noadd** - 不添加额外的行以适应数据。
- **skip:n** - 跳过每个数据行的n行。
- **ascending:n** 或 **descending:n** - 对智能标记中的数据进行排序。如果 n 为 1，则该列是排序器的第一个关键。在处理数据源后对数据进行排序。例如：&=Table1.Field3(ascending:1)。
- **horizontal** - 将数据从左至右书写，而不是从上至下。
- **numeric** - 如果可能的话，将文本转换为数字。
- **shift** - 下移或右移，创建额外的行或列以适应数据。shift参数的工作方式与Microsoft Excel中相同。例如，在Microsoft Excel中，当您选择一系列单元格，右键单击并选择**插入**，然后指定**下移单元格**、**右移单元格**和其他选项。简言之，**shift**参数在垂直/正常（自上而下）或水平（从左到右）的智能标记中具有相同的功能。
- **copystyle** - 将基本单元格的样式复制到该列中的所有单元格。

参数 noadd 和 skip 可以组合在一起，以在交替行中插入数据。因为模板是从底部到顶部进行处理的，所以应在第一行上添加 noadd 以避免在交替行之前插入额外行。

如果有多个参数，请用逗号分隔它们，但不要有空格：parameterA,parameterB,parameterC

以下屏幕截图显示了如何在每隔一行插入数据。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **动态公式**
动态公式允许您将 Excel 公式插入单元格，即使公式引用在导出过程中将被插入的行。动态公式可以针对每个插入的行重复，或者仅使用数据标记所在的单元格。

动态公式允许以下附加选项：

- r - 当前行数。
- 2、-1 - 相对于当前行数的偏移量。

例如:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

在动态公式标记中，“-1” 表示设置 B 列和 C 列的当前行偏移量，用于除法操作，skip 参数为一行。此外，我们应该指定以下字符:

{{< highlight java >}}

 "~"

{{< /highlight >}}

作为分隔符使用，以应用动态公式中的进一步参数。

以下截图展示了一个重复的动态公式以及生成的 Excel 工作表。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
单元格"C1"包含公式 **= A1*B1**，单元格"C2"包含 **= A2*B2**，单元格"C3"包含 **= A3*B3**。

处理智能标记非常简单。以下示例代码展示了如何在智能标记中使用动态公式。我们加载[模板文件](templateDynamicFormulas.xlsx)并创建测试数据，处理标记以填充数据到与标记相对应的单元格中。 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **如何在智能标记中使用动态公式和变量**
有时，您需要在智能标记中使用动态公式和变量。对于动态公式，请添加特殊字符（~）作为分隔符。Aspose.Cells 让在智能标记中使用动态公式和变量成为可能。请查看[模板文件](template.xlsx)、[json文件](employees-data.json)，以及以下代码生成的输出Excel文件的截图。

|**显示模板.xlsx文件中第一个工作表的变量。**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**显示模板.xlsx文件中第二个工作表的智能标记。**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**输出Excel文件的截图。**|
| :- |
|![todo:image_alt_text](template_result.png)|

如下所示的Json数据：
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}

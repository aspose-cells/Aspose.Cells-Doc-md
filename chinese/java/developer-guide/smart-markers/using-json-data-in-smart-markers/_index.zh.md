---
title: 在智能标记中使用Json数据
type: docs
weight: 30
url: /zh/java/using-json-data-in-smart-markers/
---

## **为什么在智能标记中使用Json数据**
为什么将JSON数据作为智能标记的原始数据？
JSON（JavaScript对象表示法）是一种轻量级、可读性强的数据交换格式，非常适合构建层次结构数据。以下是它适合作为智能标记（自动填充电子表格、文档或仪表板的动态占位符）原始数据的原因：

1. 支持结构化和层次结构数据
JSON 原生支持嵌套对象和数组（例如 { "user": { "name": "Alice", "orders": [ ... ] } }）。智能标记可以遍历此层次结构（例如 {{user.orders[0].price}}），便于将复杂数据映射到模板。

2. 跨语言和平台兼容
几乎所有编程语言（Python、JavaScript、Java等）都支持JSON解析器。像Excel Power Query、Google Apps Script或无代码平台（如Airtable）都可以无缝导入JSON。

3. 兼容API
大多数现代API（如REST、GraphQL）返回JSON格式的数据。智能标记可以直接消费来自Web服务的实时JSON数据，实现实时更新（例如股票价格、天气)。

4. 结构清晰、易于调试
JSON的纯文本结构便于验证（例如使用JSONLint）、手动编辑或通过脚本编辑。在将数据映射到标记时也更易调试。

5. 可扩展性与灵活性
在JSON中添加/删除字段不会破坏现有的智能标记（如果可选字段处理得当）。支持多种数据类型：字符串、数字、布尔值、数组和对象。

6. 生态系统兼容性
支持现代数据工具：数据库（MongoDB、PostgreSQL（JSONB）等）、自动化工具（Zapier、Integromat）、数据管道（Apache NiFi、Talend）。

## **使用Excel嵌套模板结合JSON数据**
Aspose.Cells for Java支持在智能标记中使用json数据，json数据可以层次嵌套。请查看[模板文件](smartmarker.xlsx)、[json文件](smartmarker.json)和用以下代码生成的输出Excel文件的截图。

|**smartmarker.xlsx 文件中的第一个工作表显示智能标记。**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**输出Excel文件的截图。**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

如下所示的Json数据：
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **使用Excel小计模板结合JSON数据**
Aspose.Cells for Java支持在智能标记中使用json数据，json数据可以层次嵌套。模板中的小计用于数据统计。请查看[模板文件](jsonExcelTemplate.xlsx)、[json文件](jsonData.json)和用以下代码生成的输出Excel文件的截图。

|**jsonExcelTemplate.xlsx文件的第一个工作表显示智能标记。**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**输出Excel文件的截图。**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

如下所示的Json数据：
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}

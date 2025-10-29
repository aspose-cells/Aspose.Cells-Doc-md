---
title: Excel 文件与数据操作
linktitle: 文件与数据操作
type: docs
weight: 10
url: /zh/nodejs-cpp/mcp/file-operations
keywords: "Excel 文件操作，Excel 数据操作，创建 Excel 工作簿，Excel 工作表，读取 Excel 数据，写入 Excel 数据"
description: "Excel 文件与数据操作  创建工作簿，管理工作表，利用 AI 自动化读取和写入 Excel 数据"
---

# Excel 文件与数据操作

利用 AI 自动化管理**Excel 文件**和**数据操作**。创建**Excel 工作簿**，管理**工作表**，执行**Excel 数据**的读取/写入操作。

## 可用工具

- `create_workbook` - 使用**AI Excel**自动化创建新的**Excel 工作簿**
- `create_worksheet` - 在现有**Excel 工作簿**中添加**Excel 工作表**
- `get_workbook_info` - 获取**Excel 工作簿**的元数据和信息
- `read_data_from_excel` - 利用**AI 自动化**精准读取**Excel 工作表**中的数据
- `write_data_to_excel` - 通过**Excel MCP**写入数据到**Excel 工作表**

## 创建Excel工作簿

### 创建基本工作簿
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### 创建带定制工作表的工作簿
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## 管理工作表

### 添加新工作表
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### 获取工作簿信息
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## 写入Excel数据

### 写入标题与数据
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### 写入数据到自定义位置
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## 读取Excel数据

### 读取完整的已使用范围
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### 读取特定范围
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### 从默认位置读取
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## 完整工作流程示例

### 1. 创建您的第一个Excel报告
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. 添加摘要工作表
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. 写入销售数据
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. 验证数据
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. 检查工作簿结构
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## 最佳实践

1. **文件路径**：使用相对路径以提高可移植性
2. **工作表名称**：使用描述性名称命名工作表
3. **数据结构**：以清晰的标题组织数据
4. **范围读取**：为大型数据集指定范围
5. **错误处理**：在操作前验证文件是否存在

## 常用模板

### 数据导入模式
1. 创建工作簿
2. 编写原始数据
3. 读取以进行验证
4. 使用公式进行处理

### 多工作表报告
1. 创建带主表的工作簿
2. 添加摘要/分析表
3. 将数据写入各个工作表
4. 通过公式连接工作表

### 数据验证
1. 编写数据
2. 读取特定范围
3. 验证数据完整性
4. 处理缺失值 
{{< app/cells/assistant language="nodejs-cpp" >}}
